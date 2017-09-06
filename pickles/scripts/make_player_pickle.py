import pickle
from pprint import pprint

f = open('players.txt', 'r')
player_dict = {}

for i, l in enumerate(f):
	if l != '\n':
		splt = l.split('"')
		player_id = splt[1]
		player_tag = splt[2].split('>')[1].split('<')[0]
		player_dict[player_id] = player_tag	

pickle.dump(player_dict, open('player_dict.p', 'wb'))
print('Success')