import numpy as np

def number_to_symbol(index):
	symbols_list = {
		0 : 'A',
		1 : 'C',
		2 : 'G',
		3 : 'T',
	}
	return symbols_list[index]


def numbertopattern(index, k):
	if k == 1:
		return number_to_symbol(index)
	prefix_index = index // 4
	rest = index % 4
	symbol = number_to_symbol(rest)
	prefix_pattern = numbertopattern(prefix_index, k-1)
	return prefix_pattern + symbol	


def distance_ha(a,b):
	distance = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			distance += 1
	return distance

def hamming_distance(pattern, dna):
	k = len(pattern)
	distance = 0

	for string in dna:
		hamming = np.inf
		for i in range(len(string)-k+1):
			pattern_prima = string[i:i+k]
			a = distance_ha(pattern, pattern_prima)
			if hamming > a:
				hamming = a
		distance += hamming
	return distance


def medianstring(dna, k):
	distance = np.inf

	for i in range((4**k) - 1):
		pattern = numbertopattern(i, k)

		dis_now = hamming_distance(pattern, dna)

		if distance > dis_now:
			distance = dis_now
			median = pattern

	return median
