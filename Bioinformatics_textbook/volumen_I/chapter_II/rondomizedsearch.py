import random
import greedypseudo
import profilemostprobable


with open('rosalind_ba2f.txt') as file:
	dna = []
	for line in file.read().splitlines():
		dna.append(line.strip())
file.close()

def create_motifs(dna, k, profile):
	motifs = []
	for string in dna:
		motifs.append(profilemostprobable.profilemost(string, k, profile))
	return motifs


def randomized_search(dna, k, t):
	motifs = []

	for string in dna:
		i = random.randint(0, len(dna[0])-k)
		motifs.append(string[i:i+k])

	BestMotifs = motifs

	while True:
		profile = greedypseudo.create_profile(motifs)
		motifs = create_motifs(dna, k, profile)

		if greedypseudo.score(motifs) < greedypseudo.score(BestMotifs):
			BestMotifs = motifs
		else:
			return BestMotifs

def run_1000(dna, k, t):
	best_score = k*t

	for i in range(1000):
		current_motifs = randomized_search(dna, k, t)
		current_score = greedypseudo.score(current_motifs)
		if current_score<best_score:
			best_score = current_score
			best_motifs = current_motifs

	return best_motifs

a = run_1000(dna, 15, 20)
for line in a:
	print(line)


