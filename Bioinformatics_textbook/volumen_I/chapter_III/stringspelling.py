with open('rosalind_ba3b.txt') as file:
	kmers = [line.strip() for line in file.readlines()]

def spelling(kmers):
	string = kmers[0]

	for i in range(1, len(kmers)):
		string += kmers[i][-1]

	return string

print(spelling(kmers))