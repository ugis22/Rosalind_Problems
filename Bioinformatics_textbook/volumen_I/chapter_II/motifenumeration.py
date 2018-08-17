def hamming_distance(a,b):
	distance = 0

	for i in range(len(a)):
		if a[i] != b[i]:
			distance += 1
	return distance


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

def motifenumeration(dna, k, d):
	patterns = set()
	kmers =[]

	for pattern in dna:
		for i in range(len(pattern)-k+1):
			kmers += list(neighbors(pattern[i:i+k], d))


	for kmer in kmers:
		mydict = {}
		for pattern in dna:
			for i in range(len(pattern)-k+1):
				if hamming_distance(kmer, pattern[i:i+k]) <= d:
					mydict.setdefault(pattern, []).append(kmer)
		if len(mydict.keys()) == len(dna):
			patterns.add(kmer)
	return ' '.join(patterns)



