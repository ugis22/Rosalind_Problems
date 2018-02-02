def mendel(k, m, n):
	'''Given: Three positive integers k, m, and n, 
	representing a population containing k+m+n organisms: 
	k individuals are homozygous dominant for a factor, 
	m are heterozygous, and n are homozygous recessive.

	Return: The probability that two randomly selected mating 
	organisms will produce an individual possessing a dominant 
	allele (and thus displaying the dominant phenotype). 
	Assume that any two organisms can mate.'''

	#We need float numbers so:
	k, m, n = float(k), float(m), float(n)

	#Calculate the total population
	population = k + m + n

	#Calculate the probability of two homozygous recesive matting
	r_r = (n / population) * (n-1) / (population -1)

	#Calculate the probability of two heterozygous matting

	h_h = (m / population) * (m-1) / (population - 1)

	#Calculate probability of one heterozygous and one recesive matting

	h_r = (m/population) * (n/(population-1)) + (n/population) * (m/(population-1))

	recesive_total = r_r + h_h * 0.25 + h_r * 0.5

	return 1 - recesive_total






