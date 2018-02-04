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

def faster_frequent_word(text, k):
	frequent_words = set()
	frequency_array = computing_frequencies(text, k).tolist()
	max_count = max(frequency_array)
	for i in range(4**k):
		if frequency_array[i] == max_count:
			pattern = NumberToPattern.number_to_pattern(i, k)
			frequent_words.add(pattern)
	return frequent_words

def results(text, k):
	result = faster_frequent_word(text, k)
	print(' '.join(sorted(result)))
