import NumberToPattern
import PatternToNumber 

def freqwordbysorting(text, k):
	#Initialize sets and list that are requiered
	freq_pattern = set()
	indexes = []
	count = []

	'''For every pattern that we found in text, we applied pattern to number 
	and add 1 to count to record that that pattern appeared one time'''

	for i in range(len(text) - k + 1):
		pattern = text[i:i+k]
		indexes.append(PatternToNumber.pattern_to_number(pattern))
		count.append(1)

	#Index list is sorted
	sorted_index = sorted(indexes)

	'''We slice the two lists sorted index to see if 
	there is more that one occurrences of the same pattern'''

	for i in range(len(text) - k + 1):
		if sorted_index[i] == sorted_index[i-1]:
			count[i] = count[i-1] + 1

	#We check which is the maximum number of time that any pattern appeared in text
	max_count = max(count)

	#We slice the count list to check which is the pattern that appears the max num time
	for i in range(len(text) - k + 1):
		if count[i] == max_count:
			pattern = NumberToPattern.number_to_pattern(sorted_index[i], k)
			freq_pattern.add(pattern)

	return freq_pattern

#freqwordbysorting('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)