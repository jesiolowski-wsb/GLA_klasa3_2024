liczby_pierwsze = [True for i in range(1, 1000000)]
liczby_pierwsze[0] = False
for i in range(2, 1000000):
    if i > 1000: break
    for j in range(2*i, 1000000, i):
        liczby_pierwsze[range(1, 1000000).index(j)] = False

def czy_pierwsza(liczba):
    if liczby_pierwsze[liczba - 1]:
        return 1
    else: return 0

suma = 0
with open("liczby_przyklad.txt", "r") as file:
    liczby = file.readlines()
for liczba in liczby:
    suma += czy_pierwsza(int(liczba.strip()) - 1)

print(suma)
