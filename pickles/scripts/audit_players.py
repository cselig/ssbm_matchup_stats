# test to see if all players in player_dict.p are in 2016 top 100 rankings

import pickle
from pprint import pprint

player_dict = pickle.load(open('player_dict.p', 'rb'))
tag_to_rank = pickle.load(open('tag_to_rank.p', 'rb'))

mismatch1 = []
for pid in player_dict:
	tag = player_dict[pid]
	if tag not in tag_to_rank:
		mismatch1.append(tag)

mismatch2 = []
for tag in tag_to_rank:
	if tag not in player_dict.values():
		mismatch2.append(tag)

pprint(sorted(mismatch1))

print()
print()

pprint(sorted(mismatch2))