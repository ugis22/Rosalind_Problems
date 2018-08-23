with open('rosalind_ba3a.txt') as file:
	dna = file.readline()


def composition(dna, k):
	kmers = [dna[i:i+k] for i in range(len(dna)-k+1)]
	return sorted(kmers)


a = composition(dna, 50)
for line in a:
	print(line)
