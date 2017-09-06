import pickle
from pprint import pprint

rank_to_tag = {}
tag_to_rank = {}

with open('rankings.txt', 'r') as f:
	next(f)
	for l in f:
		splt = l.split()
		rank = int(splt[0])
		try:
			int(splt[3])
			tag = splt[2]
		except:
			tag = splt[2] + ' ' + splt[3]
		if tag[-1] == '—':
			tag = tag[:-1]
		tag = tag.strip()
		rank_to_tag[rank] = tag
		tag_to_rank[tag] = rank

pickle.dump(rank_to_tag, open('rank_to_tag.p', 'wb'))
pickle.dump(tag_to_rank, open('tag_to_rank.p', 'wb'))

pprint(rank_to_tag)
print()
pprint(tag_to_rank)