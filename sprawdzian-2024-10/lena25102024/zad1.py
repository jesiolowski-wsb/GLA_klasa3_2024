plik= open('liczby.txt', 'r')
zawartosc=plik.read()
dane=zawartosc.split('\n')
def dziesietny(liczba):
    wynik=''
    while liczba>0:
        wynik+=str(liczba%2)+wynik
        liczba= liczba//2
    return wynik
for x in dane:
    print(dziesietny(int(x)))

