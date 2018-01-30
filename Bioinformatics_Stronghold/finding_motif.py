f = open('rosalind_motif.txt')
a = []
for line in f.readlines():
	a.append(line.strip())
dna1, dna2 = a[0], a[1]
f.close()

def find_motif(dna1, dna2):
	k = len(dna2)
	indexes = []
	for i in range(len(dna1)-k+1):
		if dna1[i:i+k] == dna2:
			indexes.append(str(i+1))
	print(" ".join(indexes))

find_motif(dna1, dna2)
