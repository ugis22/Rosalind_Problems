def freq_word(text, pattern):
    k = len(pattern)
    count = 0
    for i in range(len(text)-k+1):
        if text[i:i+k] == pattern: 
            count += 1
    return count