'''
Implement GreedyMotifSearch
Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t). 
If at any step you find more than one Profile-most probable k-mer 
in a given string, use the one occurring first.
'''

import numpy as np
import distancepatterncollection
import profilemostprobable

nucleotides = {
	'A': 0,
	'C': 1,
	'G': 2,
	'T': 3
}

nucleotides_reverse = {
	0: 'A',
	1: 'C',
	2: 'G',
	3: 'T'
}


def find_consensus(motifs):
	profile = np.array(create_profile(motifs))
	consensus = ''

	for i in range(len(motifs[0])):
		count_num = np.argmax(profile[:,i])

		consensus += nucleotides_reverse[count_num]

	return consensus


def score(motifs):
	consensus = find_consensus(motifs)
	
	return distancepatterncollection.hamming_distance(consensus, motifs)


def create_profile(motifs):

	profile = np.zeros(shape = (4, len(motifs[0])))

	for i in  range(len(motifs[0])):
		for kmer in motifs:
			profile[nucleotides[kmer[i]], i] += 1

	profile = profile/len(motifs)

	return profile


def greedymotif(dna, k, t):


	BestMotifs = [string[:k] for string in dna]

	first_strand = dna[0]
	rest_strand = dna[1:t]

	for i in range(len(first_strand)-k+1):
		motif_first = [first_strand[i:i+k]]
		for strand in rest_strand:
			profile = create_profile(motif_first)
			motif_first.append(profilemostprobable.profilemost(strand, k, profile))

		if score(motif_first) < score(BestMotifs):
			BestMotifs = motif_first

	return ' '.join(BestMotifs)

a = greedymotif(['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG'],3,5)
print(a)


