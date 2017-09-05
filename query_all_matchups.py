from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pickle
from collections import defaultdict
from pprint import pprint

URL = 'http://t5dev.smash4tips.com/pages/MatchHistory.cfm'

MATCHUP_STATS = defaultdict(int)

# use selenium to get js generated html
def get_html(p1id, p2id, driver):
	select1 = Select(driver.find_element_by_id('p1id'))
	select1.select_by_value(p1id)

	select2 = Select(driver.find_element_by_id('p2id'))
	select2.select_by_value(p2id)

	submitButton = driver.find_element_by_id("sendplaydata") 
	submitButton.click()

	source = driver.page_source
	return source


# parse matchup stats from html
def parse_html(source, f, p1id, p2id):
	soup = BeautifulSoup(source, 'html.parser')

	# get to 'Character Use' section
	character_use = soup.find_all('div', {'class': 'col-lg-4'})[2]

	for match_up in character_use.find_all('tr')[2:]:
	    data_list = match_up.find_all('td')
	    # extract text and unpack
	    char1, char1wins, char2wins, char2 = list(map(lambda x: x.text, data_list))
	    f.write(char1 + ',' + char1wins + ',' + char2wins + ',' + char2 + ',' + p1id + ',' + p2id + '\n')
	    if char1 != char2:
	        MATCHUP_STATS[(char1, char2)] += int(char1wins)
	        MATCHUP_STATS[(char2, char1)] += int(char2wins)
	return character_use


if __name__ == '__main__':
	# use pickles/matchups_small.p for testing
	matchups = pickle.load(open('pickles/matchups.p', 'rb'))
	driver = webdriver.Firefox()
	driver.get(URL)
	matchup_data_file = open('matchup-data.csv', 'w')
	matchup_data_file.write('char1,char1wins,char2wins,char2,p1id,p2id\n')
	for i in range(0, len(matchups)):
		p1id, p2id = matchups[i]
		if i % 100 == 0 and i != 0:
			driver.close()
			driver = webdriver.Firefox()
			driver.get(URL)
		source = get_html(str(p1id), str(p2id), driver)
		# print('HTML for %s vs %s retrieved' % (p1id, p2id))
		character_use = parse_html(source, matchup_data_file, str(p1id), str(p2id))
		html_file_name = 'html_data/' + p1id + 'vs' + p2id + '.html'
		with open(html_file_name, 'w') as f:
			f.write(str(character_use))
		# print('HTML for %s vs %s parsed' % (p1id, p2id))
		print('%s/%s complete' % (i, len(matchups)))
	pickle.dump(MATCHUP_STATS, open('pickles/matchup_stats.p', 'wb'))
	print('Success')
	matchup_data_file.close()
	pprint(MATCHUP_STATS)