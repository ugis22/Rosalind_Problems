import numpy as np


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
    m = len(dna[0])
    consensus_dna = ''

    matrix_consensus = np.zeros(shape = (4, m), dtype = int)

    for i in range(m):
        nucle = []
        for j in range(len(dna)):
            nucle.append(dna[j][i])


        lista = [nucle.count('A'), nucle.count('C'), nucle.count('G'), nucle.count('T')]    
       
        matrix_consensus[0, i] = lista[0]
        matrix_consensus[1, i] = lista[1]
        matrix_consensus[2, i] = lista[2]
        matrix_consensus[3, i] = lista[3]
               
        maximo = lista.index(max(lista))

        if maximo == 0:
            consensus_dna += 'A'
        elif maximo == 1:
            consensus_dna += 'C'
        elif maximo == 2:
            consensus_dna += 'G'
        else:
            consensus_dna += 'T'

    assert len(consensus_dna) == len(dna[0])

    return consensus_dna, matrix_consensus

def write_file(names):
    results = consensus(names)
    
    consensus_final = str(results[0])
    #matrix_final = '\n'.join(map(str, results[1].tolist()))
    matrix_final = results[1].tolist()


    
    with open('results_rosalind_cons.txt', 'w') as final_file:

        final_file.write(consensus_final+'\n')
        for line in matrix_final:
            final_file.write(' '.join(map(str, line))+'\n')
    final_file.close()

write_file(names)










