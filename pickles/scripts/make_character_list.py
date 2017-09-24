import pickle

matchup_stats = pickle.load(open('matchup_stats.p', 'rb'))

chars = set()

for t in matchup_stats:
    char1, char2 = t
    chars.add(char1)
    chars.add(char2)

pickle.dump(chars, open('character_list.p', 'wb'))