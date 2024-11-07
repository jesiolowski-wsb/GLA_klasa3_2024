# suma: 15pkt ALE:
# -1pkt za wszystkie odpowiedzi do zadań w jednym pliku

# Zdobyte punkty: 3/6
# zad 1
# błędna nazwa pliku - powinien nazywać się 'liczby.txt'
plik = open('liczby.txt', 'r')
zapis = plik.read()

# algorytm zadziała, ale nie widzę nigdzie jego wywołania z danymi z pliku
def binaryzacja(zapis):
    wynik = ''
    while zapis > 0:
        wynik = str(zapis % 2) + wynik
        zapis //= 2
    return wynik


# Zdobyte punkty: 3/5
# zad 2
# błędna nazwa pliku - powinien nazywać się tekst.tst
ligma=open("tekst.txt", 'w')
# nie rozumiem powodu dla którego to zmienna z wartością a nie treść pliku
sigma=("Ania i Tomek poszli do kina . Potem kupili lody.")
x=sigma.split()
nowa_lista = []

for element in x:
    if len(element) > 3 and element[0].isupper():
        nowa_lista.append(element)
wynik = "\n".join(nowa_lista)
# brak zapisu do pliku
print(wynik)
ligma.write(wynik)
ligma.close()


# Zdobyte punkty: 4/4
# zad 3
import random
def generuj_id():
    litery = ''.join(random.choices('ABCDE', k=2))
    cyfry = ''.join(random.choices('0123456789', k=3))
    nowe_id = litery + cyfry
    with open('id.txt', 'a') as plik:
        plik.write(nowe_id + '\n')
    return nowe_id
print(generuj_id())


# Zdobyte punkty: 5/7
# zad4
with (open ("dane.txt","r") as plik):
 # swietny sposob na wrzucenie elementów do listy
 binarne= plik.read().splitlines()

 # fajny sposób umieszczenia wyrażenia listy, ale w sprawdzeniu czy liczba jest parzysta, brakuje faktycznego sprawdzenia
 # int(b,2) zwroti true dla kazdej wartosci jako sukces wykonania operacji rzutowania na wartosc binarna
 parzyste=[int(b, 2) for b in binarne if int(b, 2)]

 # niestety join łączy elementy string a nie int:(
 o="\n".join(parzyste)
print(o)
f = open("dane.txt", "w")
f.write(o)
