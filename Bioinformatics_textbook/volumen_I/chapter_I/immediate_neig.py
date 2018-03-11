def immediate_neig(pattern):
	nucleotides = ['A', 'C', 'G', 'T']
	neighborhood = set(pattern)
	for i in range(len(pattern)):
		symbol = pattern[i]
		for j in nucleotides:
			if j != symbol:
				neighborhood.add(pattern[:i]+j+[pattern[i+1:]])
	return neighborhood
