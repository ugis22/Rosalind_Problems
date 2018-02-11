from HammingDistance import hamming_distance

def neighbors(pattern, d):
	nucleotides = ['A', 'C', 'G', 'T']
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return nucleotides

	neighborhood = set()
	#we generate all the neighbors for (k-1)mer pattern
	suffix_neig = neighbors(pattern[1:], d)

	for text in suffix_neig:
		#IF the hamming distance is less than d add any symbol in first position
		if hamming_distance(pattern[1:], text) < d:
			for i in nucleotides:
				neighborhood.add(i+text)
		#If hamming distance is exactly d add the first symbol of pattern
		else:
			neighborhood.add(pattern[0]+text)
			
	return neighborhood

