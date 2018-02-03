import numpy as np

#Open File and read the strings
f= open('rosalind_cons.txt')
names = []
i = -1

for line in f.readlines():
    if line[0] == '>':       
        i += 1
        names.append('')
    else:
        names[i] += line.strip()
f.close()

def consensus(dna):

    """Given: A collection of at most 10 DNA strings of equal length 
    (at most 1 kbp) in FASTA format.

    Return: A consensus string and profile matrix for the collection. 
    If several possible consensus strings exist, then you may return any one of them."""

    #We initialize m = lenght of n string, consensus_dna as an empty string
    m = len(dna[0])
    nucleotides_list = ['A', 'C', 'G', 'T']
    consensus_dna = ''

    matrix_consensus = np.zeros(shape = (4, m), dtype = int)

    #Get the first nucleotide in each string
    for i in range(m):
        nucle_at_curr_position = []
        for j in range(len(dna)):
            #append to list 
            nucle_at_curr_position.append(dna[j][i])

        #count how many A, C, G and T are in that position

        lista = [nucle_at_curr_position.count('A'), nucle_at_curr_position.count('C'), nucle_at_curr_position.count('G'), 
                nucle_at_curr_position.count('T')]    
       
        #Add this count to the matrix
        matrix_consensus[0, i] = lista[0]
        matrix_consensus[1, i] = lista[1]
        matrix_consensus[2, i] = lista[2]
        matrix_consensus[3, i] = lista[3]

        #Get the nucleotide with maximum count       
        consensus_dna += nucleotides_list[lista.index(max(lista))]

    #check if the length consensus found match length of strings given
    assert len(consensus_dna) == len(dna[0])

    return consensus_dna, matrix_consensus

def write_file(names):
    results = consensus(names)
    
    consensus_final = str(results[0])
    matrix_final = results[1].tolist()


    with open('results_rosalind_cons.txt', 'w') as final_file:

        final_file.write(consensus_final+'\n')
        for line in matrix_final:
            final_file.write(' '.join(map(str, line))+'\n')
    final_file.close()

write_file(names)










