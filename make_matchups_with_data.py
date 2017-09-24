# Filter matchups.p to only matchups with sets in 2016

import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import Select


URL = 'http://t5dev.smash4tips.com/pages/MatchHistory.cfm'
ID_TO_TAG = pickle.load(open('pickles/id_to_tag.p', 'rb'))


# use selenium to get js generated html
def is_history(p1id, p2id, driver):
	select1 = Select(driver.find_element_by_id('p1id'))
	select1.select_by_value(p1id)

	select2 = Select(driver.find_element_by_id('p2id'))
	select2.select_by_value(p2id)

	submitButton = driver.find_element_by_id("sendplaydata") 
	submitButton.click()

	if driver.find_elements_by_xpath('//tbody')[1].find_elements_by_xpath('tr'):
		return True


if __name__ == '__main__':
	matchups = pickle.load(open('pickles/matchups.p', 'rb'))
	driver = webdriver.Firefox()
	driver.get(URL)

	matchups_with_history = open('matchups_with_history2.csv', 'w')
	matchups_with_history.write('p1id,p2id\n')

	for i in range(4076, len(matchups)):
		if i % 50 == 0 and i != 1:
			driver.close()
			driver = webdriver.Firefox()
			driver.get(URL)
		p1id, p2id = matchups[i]
		if is_history(str(p1id), str(p2id), driver):
			matchups_with_history.write(p1id + ',' + p2id + '\n')
			print(str(i) + ': ' + ID_TO_TAG[int(p1id)] + ' and ' + ID_TO_TAG[int(p2id)] + ' have sets in 2016')
		else:
			print(str(i) + ': ' + ID_TO_TAG[int(p1id)] + ' and ' + ID_TO_TAG[int(p2id)] + ' do not has sets in 2016')
	
	driver.close()
	matchups_with_history.close()