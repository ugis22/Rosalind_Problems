import NumberToPattern
import numpy as np
import PatternToNumber 

def computing_frequencies(text, k):
	m = 4**k  
	frequency_array = np.zeros(shape = (1, m), dtype = int)
	
	for i in range(len(text) - k + 1):
		pattern = text[i:i+k]
		j = PatternToNumber.pattern_to_number(pattern)
		frequency_array[0 , j] = frequency_array[0, j] + 1
	return frequency_array.flatten()


def clump_finding(genome, k, l, t):
	freq_pattern = set()
	clump = [0] * 4**k

	'''We slide a window of lenght l in the genome and compute freq array 
	for the patterns in that window'''
	for i in range(len(genome) - l + 1):
		text = genome[i:i+l]
		freq_array = computing_frequencies(text, k).tolist()
		for index in range(4**k):
			#Checks if in that windows the pattern appears >= t times
			if freq_array[index] >= t:
				clump[index] = 1

	#Finds which pattern forms a clump
	for i in range(4**k):
		if clump[i] == 1:
			pattern = NumberToPattern.number_to_pattern(i, k)
			freq_pattern.add(pattern)

	print(' '.join(freq_pattern))

clump_finding('CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC', 5, 75, 4)

