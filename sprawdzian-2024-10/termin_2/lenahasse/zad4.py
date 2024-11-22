def osemkowy_binarny(liczba):
    wynik=int(liczba,8)
    return bin(int(wynik))[2:]
with open('oct.txt','r') as plik:
    tekst=plik.read()
lista=tekst.split()
with open('bin.txt','w') as wynik:
    for liczba in lista:
        if len(osemkowy_binarny(liczba))>3:
            wynik.write(osemkowy_binarny(liczba)+'\n')