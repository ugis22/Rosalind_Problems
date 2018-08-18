'''
Implement GreedyMotifSearch
Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). 
If at any step you find more than one Profile-most probable k-mer 
in a given string, use the one occurring first.
'''

import numpy as np

nucleotides = {
	'A': 0,
	'C': 1,
	'G': 2,
	'T': 3
}


#def score():



def create_profile(motifs):

	profile = np.zeros(shape = (4, len(motifs[0])))

	for i in  range(len(motifs[0])):
		for kmer in motifs:
			profile[nucleotides[kmer[i]], i] += 1

	profile = profile/len(motifs)


def greedymotif(dna, k, t):


	BestMotifs = [string[i][:k] for string in dna]

	first_strand = dna[0]
	rest_strand = dna[1:]

	for i in range(len(first_strand)-k+1):
		motif_first = [first_strand[i:i+k]]
		for strand in rest_strand:
			profile = create_profile(motif_first)
			motif_first.append(kmer(strand, k, profile))

		if score(motif_first) < score(BestMotifs):
			BestMotifs = motif_first

	return ''.join(BestMotifs)





