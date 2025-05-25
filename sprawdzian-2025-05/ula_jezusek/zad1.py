def znajdz_pierwsze(n):
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False
    for i in range(2, int(n**0.5) +1):
        if sito[i]:
            for j in range(i*i, n + 1, i):
                sito[j] = False
    pierwsze = []
    for i in range(2, n+1):
        if sito[i]:
            pierwsze.append(i)
    return pierwsze
