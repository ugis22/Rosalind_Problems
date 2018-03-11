import neighboors
import PatternToNumber
import NumberToPattern

def freqwordmiss_sorting(text, k, d):
	freq_pattern = set()
	neighborhoods = []
	neighborhoods_array = []
	index = []
	count = []

	for i in range(len(text)-k+1):
		neighborhoods.append(neighboors.neighbors(text[i:i+k], d))

	for l in neighborhoods:
		for j in l:
			neighborhoods_array.append(j)

	for i in range(len(neighborhoods_array)):
		pattern = neighborhoods_array[i]
		index.append(PatternToNumber.pattern_to_number(pattern))
		count.append(1)

	sortedindex = sorted(index)

	for i in range(len(neighborhoods_array)):
		if sortedindex[i] == sortedindex[i-1]:
			count[i] = count[i-1] + 1

	maxcount = max(count)

	for i in range(len(neighborhoods_array)):
		if count[i] == maxcount:
			pattern = NumberToPattern.number_to_pattern(sortedindex[i], k)
			freq_pattern.add(pattern)
	print(' '.join(freq_pattern))

freqwordmiss_sorting('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)