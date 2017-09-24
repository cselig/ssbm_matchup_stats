import pickle

player_dict = pickle.load(open('player_dict.p', 'rb'))
id_to_tag = {}
tag_to_id = {}

for x in player_dict:
	id_ = int(x)
	tag = player_dict[x]
	id_to_tag[id_] = tag
	tag_to_id[tag] = id_

pickle.dump(id_to_tag, open('id_to_tag.p', 'wb'))
pickle.dump(tag_to_id, open('tag_to_id.p', 'wb'))