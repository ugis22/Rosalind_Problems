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


def better_clump_finding(genome, k, l, t):
	freq_pattern = set()
	clump = [0] * 4**k

	#Compute first the frequencies in the first l nucleotides of genome
	text = genome[0:l]
	freq_array = computing_frequencies(text, k).tolist()

	#Checks if in the 1st window the pattern appears >= t times
	for index in range(4**k):
		if freq_array[index] >= t:
			clump[index] = 1

	for i in range(len(genome) - l + 1):
		first_pattern = genome[i-1:i+k-1]
		index = PatternToNumber.pattern_to_number(first_pattern)
		freq_array[index] = freq_array[index] - 1
		last_pattern = genome[i+l-k:i+l]
		index = PatternToNumber.pattern_to_number(last_pattern)
		freq_array[index] = freq_array[index] + 1

		if freq_array[index] >= t:
			clump[index] = 1

	#Finds which pattern forms a clump
	for i in range(4**k):
		if clump[i] == 1:
			pattern = NumberToPattern.number_to_pattern(i, k)
			freq_pattern.add(pattern)

	print(' '.join(sorted(freq_pattern)))

