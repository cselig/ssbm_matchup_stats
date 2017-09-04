import pickle
from pprint import pprint

players = pickle.load(open('player_dict.p', 'rb'))

# list of tuple of player ids: no duplicates, order doesn't matter
matchups = []

ids = list(players.keys())

# get all id pairs
for i in range(0, len(ids)):
	for j in range(i + 1, len(ids)):
		matchups.append( (ids[i], ids[j]) ) 

pickle.dump(matchups, open('matchups.p', 'wb'))
print('Success')