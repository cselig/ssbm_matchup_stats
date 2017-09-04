from bs4 import BeautifulSoup
from collections import defaultdict
from pprint import pprint

soup = BeautifulSoup(open('selenium_test.html', 'r'), 'html.parser')

# get to 'Character Use' section
character_use = soup.find_all('div', {'class': 'col-lg-4'})[2]

p1id = '1'
p2id = '2'
matchup_stats = defaultdict(int)

# get character match-up data
for match_up in character_use.find_all('tr')[2:]:
    data_list = match_up.find_all('td')
    # extract text and unpack
    char1, char1wins, char2wins, char2 = list(map(lambda x: x.text, data_list))
    if char1 != char2:
        matchup_stats[(char1, char2)] += int(char1wins)
        matchup_stats[(char2, char1)] += int(char2wins)

pickle.dump(matchup_stats, open('matchup_stats.p', 'wb'))
print('Success')