# Some functions to query matchup stats

import pickle
from collections import defaultdict
from pprint import pprint
from  statsmodels.stats.proportion import proportions_ztest

MATCHUP_STATS = pickle.load(open('pickles/matchup_stats.p', 'rb'))
CHARACTERS = pickle.load(open('pickles/character_list.p', 'rb'))

# params:
#	char1, char2: character names (strings)
def compute_character_matchup(char1, char2):
	wins = MATCHUP_STATS[char1, char2]
	losses = MATCHUP_STATS[char2, char1]
	total = wins + losses

	if wins > losses:
		percentage = wins / (losses + wins) * 100
		winning_char = char1
		losing_char = char2
	else:
		percentage = losses / (losses + wins) * 100
		winning_char = char2
		losing_char = char1

	test_is_significant(wins, total)

	percentage_str = '{0:.2f}'.format(percentage)
	print(winning_char + ' has won ' + percentage_str + '% of ' + str(total) + ' ' + winning_char + ' vs ' + losing_char + ' games in 2016')


# For this hypothesis test, we are using a two-tailed difference of proportions test.
# We use significance level of 0.05 
# parameters:
#	
# returns: 
#	True if a matchup's stats are significantly above or below 50/50, False otherwise
def is_significant(wins, total):
	return proportions_ztest(wins, total, value=0, alternative='two-sided', prop_var=False)


# don't think this is working
def compute_percentage_win_list():
	totals = defaultdict(int)
	wins = defaultdict(int)
	percents = {}

	for t, num in MATCHUP_STATS.items():
		char1, char2 = t
		totals[char1] += num
		totals[char2] += num
		wins[char1] += num

	for char in CHARACTERS:
		percents[char] = wins[char] / totals[char]
	pprint([(k, percents[k]) for k in sorted(percents, key=lambda x: percents[x], reverse=True)])


def test_is_significant(wins, total):
	stat, pval = is_significant(wins, total)
	print(stat)
	print(pval)


if __name__ == '__main__':
	print()
	char1 = input('Enter first character: ')
	char2 = input('Enter second character: ')
	print()
	compute_character_matchup(char1, char2)
	print()
	# compute_percentage_win_list()