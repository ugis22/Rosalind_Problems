def reversed_complement(string):
    """Find the reverse complement of a DNA string.
    
    Given: A DNA string Pattern.

    Return: Pattern, the reverse complement of Pattern."""
    
    complements = {'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
    }
    
    return "".join([complements[string[i]] for i in range(len(string))][::-1])

def pattern_string_ocurrencies(pattern, string):
    """Find all occurrences of a pattern in a string.

    Given: Strings Pattern and Genome.
    
    Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing."""
    
    k = len(pattern)
    positions = []
    for i in range(len(string)-k+1):
        if string[i:i+k] == pattern: 
            positions.append(i)
    print(" ".join(map(str, positions)))
