def dna(string):
    """
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective 
    number of times that the symbols 'A', 'C', 'G', and 'T' occur in s."""

    a = [string.count('A'), string.count('C'), string.count('G'), string.count('T')]
    print(" ".join(map(str, a)))

def trans(string):
    """
    Given: A DNA string t having length at most 1000 nt.

    Return: The transcribed RNA string of t."""
    return string.replace('T', 'U')

def reversed_complement(string):
    """
    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s."""
    complements = {'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
    }
    
    return "".join([complements[string[i]] for i in range(len(string))][::-1])

def hamming_distance(string1, string2):

    """
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

    Return: The Hamming distance dH(s,t)."""
    assert len(string1) == len(string2)

    distance = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    print(distance)


"""f= open('rosalind_gc.txt')
names = {}
for line in f.readlines():
    if line[0] == '>':
        la_key = line[1:].strip()
        names[la_key] = ''
    else:
        names[la_key] += line.strip()
f.close()"""

def count_gc(strings):
    maximo = 0
    ''' Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

    Return: The ID of the string having the highest GC-content, 

    followed by the GC-content of that string.''' 

    for name, string in strings.items():
        contenido = ((string.count('C')+string.count('G'))/len(string))*100
        if contenido > maximo:
            mayor_contenido_name = name
            maximo = contenido
    print(name)
    print(maximo) 

#count_gc(names)



    
        

