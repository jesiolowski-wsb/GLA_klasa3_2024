# Zdobyte punkty: 5/6

#ZADANIE 1
with open('liczby.txt', 'r') as plik:
    zawartosc = plik.read()

def dziesietny_na_binarny(liczba):
    wynik = ''
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba //= 2
    return wynik

dane = zawartosc.split("\n")
for d in dane:
    # super, prawie pełen sukces - zabrakło małego elementu tj. write()
    print(dziesietny_na_binarny(int(d)))
