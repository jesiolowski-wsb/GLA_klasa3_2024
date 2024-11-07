# 17 pkt ALE:
# -1pkt za wszystkie odpowiedzi do zadań w jednym pliku

# Zdobyte punkty: 3/6
# zad 1
# polecenie prosiło o inna nazwe pliku
plik = open('plik.txt', 'r')
zawartosc = plik.read()
plik.close()
def dziesietny_na_binarny_manualnie(zawartosc):
    wynik = ''
    while zawartosc > 0:
        wynik = str(zawartosc % 2) + wynik
        zawartosc //= 2
    return wynik

# nie rozumiem skąd ta wartosc?
liczba = 30
# brak zapisu do pliku
print(dziesietny_na_binarny_manualnie(zawartosc))

# Zdobyte punkty: 5/5
# zad2
with open("tekst.txt", "r", ) as file:
    content = file.read()

words = [word for word in content.split() if len(word) > 3 and word[0].isupper()]
with open("analiza.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

# Zdobyte punkty: 2/4
# zad3
import random
def generuj_id():
    letters = ''.join(random.choice('ABCDE') for _ in range(2))
    numbers = ''.join(random.choice('0123456789') for _ in range(3))
# zabraklo definicji new_id - nie mamy mozliwosci zapisu nieistniejacej zmiennej
with open("id.txt", "w") as file: file.write(new_id)

# Zdobyte punkty: 7/7
# zad4
dane  = open('dane.txt', 'r')
lines = dane.readlines()
dane.close()
dec_d = [str(int(l, base=2)) for l in lines if int(l, base=2)%2==0]
dane = open('wyniki.txt', 'w')
dane.write('\n'.join(dec_d))
dane.close()
