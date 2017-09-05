from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pickle


URL = 'http://t5dev.smash4tips.com/pages/MatchHistory.cfm'

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
def parse_html(source):
	soup = BeautifulSoup(source, 'html.parser')

	# get to 'Character Use' section
	character_use = soup.find_all('div', {'class': 'col-lg-4'})[2]
	return character_use


if __name__ == '__main__':
	# use pickles/matchups_small.p for testing
	matchups = pickle.load(open('pickles/matchups.p', 'rb'))
	driver = webdriver.Firefox()
	driver.get(URL)
	for i in range(4738, len(matchups)):
		p1id, p2id = matchups[i]
		if i % 100 == 0 and i != 0:
			driver.close()
			driver = webdriver.Firefox()
			driver.get(URL)
		source = get_html(str(p1id), str(p2id), driver)
		character_use = parse_html(source, matchup_data_file, str(p1id), str(p2id))
		html_file_name = 'html_data/' + p1id + 'vs' + p2id + '.html'
		with open(html_file_name, 'w') as f:
			f.write(str(character_use))
		print('%s/%s complete' % (i, len(matchups)))
	print('Success')
	matchup_data_file.close()