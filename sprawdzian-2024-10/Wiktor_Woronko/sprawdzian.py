# Zdobyte punkty: 5/7
# sporo niedopowiedzen, literówek i z potrzeba poprawek aby zaczelo dzalac

# Zad.4
# wczytywanie 2 razy tego samego pliku? Zdaje się byc nadmiarowe
plik= open('dane.txt' , 'r')
with open( 'dane.txt' ,'r') as file:
    binarne= [line.strip() for line in file]
    parzyste_dziesiete= [int(liczba, 2) for liczba in binarne if int(liczba, 2) % 2== 0]

with open('wyniki.txt', 'w') as file:
    # literowka w nazwie
    for liczba in parzyste_dziesiete:
        file.write(f"{liczba}\n")

# Zdobyte punkty: 2/5
# zad.2
import random
# w jakim celu ten nieuzywany import?
import string
def generuj_id():
    litery = ''.join(random.choices('ABCDE', k=2))
    # literówka - brakujace zamkniecie '
    cyfry = ''.join(random.choices('123456789', k=3))
    # literówka - za duzo o jedno e w nazwie
    nowe_id = litery + cyfry

with open('id.txt', 'w') as file:
    # ta linia nie ma jak dzialac - nie jest czescia funkcji
    return nowe_id
    print(generuj_id())
