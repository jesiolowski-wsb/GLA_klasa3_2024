zad 1
plik = open('plik.txt', 'r')
zapis = plik.read()
def binaryzacja(zapis):
    wynik = ''
    while zapis > 0:
        wynik = str(zapis % 2) + wynik
        zapis //= 2
    return wynik
zad 2
ligma=open("tekscik.txt", 'w')
sigma=("Ania i Tomek poszli do kina . Potem kupili lody.")
x=sigma.split()

nowa_lista = []


for element in x:

    if len(element) > 3 and element[0].isupper():
        nowa_lista.append(element)
wynik = "\n".join(nowa_lista)
print(wynik)
ligma.write(wynik)
ligma.close()
zad 3
import random
def generuj_id():
    litery = ''.join(random.choices('ABCDE', k=2))
    cyfry = ''.join(random.choices('0123456789', k=3))
    nowe_id = litery + cyfry
    with open('id.txt', 'a') as plik:
        plik.write(nowe_id + '\n')
    return nowe_id
print(generuj_id())
zad4
with (open ("dane.txt","r") as plik):
 binarne= plik.read().splitlines()
 parzyste=[int(b, 2) for b in binarne if int(b, 2)]
 o="\n".join(parzyste)
print(o)
f = open("dane.txt", "w")
f.write(o)
