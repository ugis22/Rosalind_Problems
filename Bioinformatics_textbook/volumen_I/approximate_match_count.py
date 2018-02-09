import HammingDistance

file= open('rosalind_ba1h.txt', 'r')

pattern = file.readline().strip()
print(pattern)
text = file.readline().strip()
d = int(file.readline().strip())

file.close()




def approximate_match_positions(pattern, text, d):
	positions = []
	m = len(pattern)
	for i in range(len(text)- m + 1):
		pattern_current = text[i:i+m]
		if HammingDistance.hamming_distance(pattern, pattern_current) <= d:
			positions.append(str(i))
	return positions

print(' '.join(approximate_match_positions(pattern, text, d)))
