# clean and redump player_dict.p, tag_to_rank.p, and rank_to_tag.p to make sure the tags match

import pickle
from pprint import pprint

player_dict = pickle.load(open('player_dict.p', 'rb'))
tag_to_rank = pickle.load(open('tag_to_rank.p', 'rb'))
rank_to_tag = pickle.load(open('rank_to_tag.p', 'rb'))

correct = ['$Mike','4percent','Chillindude','Connor','DarkAtma','DruggedFox','Esam',
'Infinite Numbers','Ka-Master','s2j','Rishi','Trifasia','Drunk Sloth','Llod']

incorrect = ['$mike','4%','Chillin','CDK','Darkatma','Druggedfox','ESAM','InfiniteNumbers',
'Ka-master','S2J','SmashG0D','Trif','drunksloth','lloD']

correction_dict = {}
for i in range(0, len(correct)):
	correction_dict[incorrect[i]] = correct[i]

for tag in tag_to_rank:
	if tag in incorrect:
		rank = tag_to_rank[tag]
		tag_to_rank.pop(tag)
		tag_to_rank[correction_dict[tag]] = rank

for rank in rank_to_tag:
	if rank_to_tag[rank] in incorrect:
		rank_to_tag[rank] = correction_dict[rank_to_tag[rank]]

pprint(tag_to_rank)
print()
pprint(rank_to_tag)

pickle.dump(tag_to_rank, open('tag_to_rank_corrected.p', 'wb'))
pickle.dump(rank_to_tag, open('rank_to_tag_corrected.p', 'wb'))