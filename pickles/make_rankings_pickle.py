import pickle


rankings = {}

with open('rankings.txt', 'r') as f:
	next(f)
	for l in f:
		splt = l.split()
		rank = splt[0]
		try:
			int(splt[3])
			tag = splt[2]
		except:
			tag = splt[2] + ' ' + splt[3]
		print(rank + ': ' + tag)