def dziesietny_na_osemkowy(liczba):
    wynik = ''
    while liczba > 0:
        wynik = str(liczba % 8) + wynik
        liczba //= 8
    return wynik

with open('dec.txt','r') as plik:
    tekst=plik.read()
lista=tekst.split()

with open('wyniki.txt','a+') as wyniki:
    for i in lista:
        wyniki.write(f'{i} : {dziesietny_na_osemkowy(int(i))} \n')