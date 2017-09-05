# Some functions to query matchup stats

import pickle

MATCHUP_STATS = pickle.load(open('pickles/matchup_stats.p', 'rb'))

# params:
#	char1, char2: character names (strings)
def compute_character_matchup_percentage(char1, char2):
	wins = MATCHUP_STATS[ (char1, char2) ]
	losses = MATCHUP_STATS[ (char2, char1) ]
	total = wins + losses

	if wins > losses:
		percentage = wins / (losses + wins) * 100
		winning_char = char1
		losing_char = char2
	else:
		percentage = losses / (losses + wins) * 100
		winning_char = char2
		losing_char = char1

	percentage_str = '{0:.2f}'.format(percentage)
	print(winning_char + ' has won ' + percentage_str + '% of ' + str(total) + ' ' + winning_char + ' vs ' + losing_char + ' games in 2016')


if __name__ == '__main__':
	# test
	print()
	char1 = input('Enter first character: ')
	char2 = input('Enter second character: ')
	print()
	compute_character_matchup_percentage(char1, char2)
	print()