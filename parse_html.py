from bs4 import BeautifulSoup
import pickle
from collections import defaultdict
from pprint import pprint


# parse matchup stats from html
def parse_html(f_in, f_out, p1id, p2id, matchup_stats):
	soup = BeautifulSoup(f_in, 'html.parser')

	for match_up in soup.find_all('tr')[2:]:
	    data_list = match_up.find_all('td')
	    # extract text and unpack
	    char1, char1wins, char2wins, char2 = list(map(lambda x: x.text, data_list))
	    f_out.write(char1 + ',' + char1wins + ',' + char2wins + ',' + char2 + ',' + p1id + ',' + p2id + '\n')
	    if char1 != char2:
	        matchup_stats[(char1, char2)] += int(char1wins)
	        matchup_stats[(char2, char1)] += int(char2wins)


if __name__ == '__main__':
	matchups = pickle.load(open('pickles/matchups.p', 'rb'))
	matchup_stats = defaultdict(int)

	f_out = open('matchup-data.csv', 'w')

	i = 0
	for p1id, p2id in matchups:
		html_file_name = 'html_data/%svs%s.html' % (p1id, p2id)
		with open(html_file_name, 'r') as f_in:
			parse_html(f_in, f_out, p1id, p2id, matchup_stats)
		i += 1
		print('%s/%s complete' % (i, len(matchups)))

	f_out.close()
	print(len(matchup_stats))
	pickle.dump(matchup_stats, open('pickles/matchup_stats.p', 'wb'))