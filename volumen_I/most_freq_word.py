from six import iteritems

def freq_word(text, k):
    #Create a dictionary and store the kmers in text
    kmers ={}
    for i in range(len(text)-k+1):
        kmers[text[i:i+k]] = kmers.get(text[i:i+k], 0) + 1 
    #calculate the maximum number of occurences of the most frequent word
    maximo = max(kmers.values())
    #Obtain the frequent words
    print(" ".join(sorted([x for x, y in list(iteritems(kmers)) if y == maximo])))
