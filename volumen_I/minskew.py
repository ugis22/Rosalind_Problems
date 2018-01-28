def skew(genome):
    cg = 0
    list_cg = []
    for i in range(len(genome)):
        if genome[i] == 'C':
            cg-= 1
        if genome[i] == 'G':
            cg += 1
        list_cg.append(cg)
    return list_cg

def min_skew(genome):
    skew_rel = skew(genome)
    minimo = min(skew_rel)
    a = [i+1 for i in range(len(skew_rel)) if skew_rel[i] == minimo]
    print(" ".join(map(str, a)))