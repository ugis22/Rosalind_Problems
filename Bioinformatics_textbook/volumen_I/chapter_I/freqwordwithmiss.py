import neighboors
import PatternToNumber
import NumberToPattern
import HammingDistance


def approximate_match_count(pattern, text, d):
	count = 0
	m = len(pattern)
	for i in range(len(text)- m + 1):
		pattern_current = text[i:i+m]
		if HammingDistance.hamming_distance(pattern, pattern_current) <= d:
			count += 1
	return count



def freq_word_missmatches(text, k, d):
	freq_pattern = set()
	close = [0]*4**k
	freq_array = [0] * 4**k

	for i in range(len(text) - k + 1):
		neighborhood = neighboors.neighbors(text[i:i+k], d)
		for pattern in neighborhood:
			index = PatternToNumber.pattern_to_number(pattern)
			close[index] = 1

	for i in range(4**k):
		if close[i] == 1:
			pattern = NumberToPattern.number_to_pattern(i, k)
			freq_array[i] = approximate_match_count(pattern, text, d)
	max_count = max(freq_array)
	for i in range(4**k):
		if freq_array[i] == max_count:
			freq_pattern.add(NumberToPattern.number_to_pattern(i, k))
	return freq_pattern

def results(text, k, d):
	print(' '.join(freq_word_missmatches(text, k, d)))

#results('ACGTTGCATGTCGCATGATGCATGAGAGCT',4,1)





