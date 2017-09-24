from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pickle
import time

URL = 'http://t5dev.smash4tips.com/pages/MatchHistory.cfm'
TAG_TO_ID = pickle.load(open('../pickles/tag_to_id.p', 'rb'))


# use selenium to get js generated html
def get_base_html(p1id, p2id, driver):
	select1 = Select(driver.find_element_by_id('p1id'))
	select1.select_by_value(p1id)

	select2 = Select(driver.find_element_by_id('p2id'))
	select2.select_by_value(p2id)

	submitButton = driver.find_element_by_id("sendplaydata") 
	submitButton.click()


def parse_html(driver, set_id, sets_out, games_out, p1id):
	# show 100 sets at a time
	select_show_entries = Select(driver.find_element_by_name("dataTables-example_length"))
	select_show_entries.select_by_value('100')

	table = driver.find_elements_by_xpath('//tbody')[3]
	

	for i, entry in enumerate(table.find_elements_by_xpath('tr')):
		button_list = driver.find_elements_by_xpath('//tbody/tr/td/button')

		if len(button_list) != 0:
			button_list[i].click()
			time.sleep(0.2)
			set_id += 1
			print(set_id)
			table_head = driver.find_elements_by_xpath('//thead')[4]
		set_info_list = []

		for info in entry.find_elements_by_xpath('td'):
			set_info_list.append(info.text)
		sets_out.write(str(set_id) + ',' + ','.join(set_info_list[:-1]) + '\n')


		# find out what order the players are listed in. if p1 comes before p2, we need
		# to reverse below
		reverse = False
		if TAG_TO_ID[table_head.find_elements_by_xpath('tr/th')[2].text] != p1id:
			reverse = True

		for game in table.find_elements_by_xpath('tr'):
			game_info_list = []
			for info in game.find_elements_by_xpath('td'):
				game_info_list.append(info.text)
			if reverse:
				p2char = game_info_list[2]
				del game_info_list[2]
				game_info_list.insert(3, p2char)
			# print(game_info_list)
			games_out.write(str(set_id) + ',' + ','.join(game_info_list) + '\n')
			# print('\t' + str(game_info_list))

	return set_id


if __name__ == '__main__':
	# use pickles/matchups_small.p for testing
	matchups = pickle.load(open('../pickles/matchups.p', 'rb'))
	driver = webdriver.Firefox()
	driver.get(URL)
	set_id = 0
	sets_out = open('sets.csv', 'w')
	games_out = open('games.csv', 'w')
	sets_out.write('set_id,date,tourney,set,p1,p2,winner\n')
	games_out.write('set_id,game,stage,p1char,p2char,winner,stock_diff\n')

	for i in range(0, len(matchups)):
		p1id, p2id = matchups[i]
		if i % 10 == 0 and i != 0:
			driver.close()
			driver = webdriver.Firefox()
			driver.get(URL)
		get_base_html(str(p1id), str(p2id), driver)
		# with open('test.html', 'w') as f:
		# 	f.write(source)
		set_id = parse_html(driver, set_id, sets_out, games_out, p1id)
		# with open('parse_test.html', 'w') as f:
		# 	f.write(str(source))
		# html_file_name = 'html_data/' + p1id + 'vs' + p2id + '.html'
		# with open(html_file_name, 'w') as f:
		# 	f.write(str(tourney_history))
		print('%s/%s complete' % (i, len(matchups)))
	print('Success')