# make small matchup combinations for testing

import pickle

matchups_small = [
	(8, 9),
	(9, 6),
	(5, 9), 
	(5, 6),
	(1, 5), 
	(1, 6)
	]

pickle.dump(matchups_small, open('matchups_small.p', 'wb'))