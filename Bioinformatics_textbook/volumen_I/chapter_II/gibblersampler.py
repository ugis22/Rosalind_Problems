import random
import greedypseudo
import profilemostprobable

with open('rosalind_ba2g.txt') as file:
	dna = []
	for line in file.read().splitlines():
		dna.append(line.strip())
file.close()



def gibbs(dna, k, t, N):
	motifs = []

	for string in dna:
		i = random.randint(0, len(dna[0])-k)
		motifs.append(string[i:i+k])

	BestMotifs = motifs

	for j in range(N):
		i = random.randint(0, t-1)

		del motifs[i]

		profile = greedypseudo.create_profile(motifs)
		motifs.insert(i, profilemostprobable.profilemost(dna[i], k, profile))


		if greedypseudo.score(motifs) < greedypseudo.score(BestMotifs):
			BestMotifs = motifs
		else:
			return BestMotifs

def repgibbs(dna, k, t, N):
	best_score = k*t

	for i in range(1000):
		current_motifs = gibbs(dna, k, t, N)
		current_score = greedypseudo.score(current_motifs)
		if current_score<best_score:
			best_score = current_score
			best_motifs = current_motifs

	return best_motifs

a = repgibbs(dna, 15, 20,2000)
for line in a:
	print(line)


