# suma zdobytych punktów: 15 (6+3+2+4)
# zadania wykpnane w czasie: 0/4
# ===================================

# zdobyte punkty: 6/6

# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:45
# czas potrzebny do realizacji: 60 min

# zad1
def dec_to_ter(liczba):
    if liczba == 0:
        return "0"
    liczba = int(liczba)
    wynik = ""
    while liczba > 0:
        reszta = liczba % 3
        wynik = str(reszta) + wynik
        liczba = liczba // 3
    return wynik
with open('decimal.txt', 'r') as plik:
    liczby = plik.read().splitlines()
with open('ternary.txt', 'w') as plik:
    for liczba in liczby:
        ter_num = dec_to_ter(liczba)
        plik.write(f"{liczba} : {ter_num}\n")


# zdobyte punkty: 3/5
# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:45
# oddano o: 16:04
# czas potrzebny do realizacji: 79 min
# delta pomiedzy realizacja 1 a 2: 19 min

# zad 2
def telefony():
    with open('phones.txt', 'r') as plik:
        zbior_num = plik.read()

    numery = [numer for numer in zbior_num.split()
              # numer[0] in ("5", "6")
              # obecne rozwiazanie sprawdza czy numer znajduje sie w stringu 56
              if len(numer) == 9 and  numer in '56']
    with open('valid_phones.txt', 'w') as plik:
        for numer in numery:
            plik.write(numer + '\n')

# zdobyte punkty: 2/4

# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:45
# oddano o: 16:04
# oddano o: 16:22
# czas potrzebny do realizacji: 97 min
# delta pomiedzy realizacja 2 a 3: 18 min

# zad 3
with open('bin1.txt', 'r') as plik1, open('bin2.txt', 'r') as plik2:
    bin1_numbers = [line.strip() for line in plik1.readlines()]
    bin2_numbers = [line.strip() for line in plik2.readlines()]

sumy = [int(b1, 2) + int(b2, 2) for b1, b2 in zip(bin1_numbers, bin2_numbers)]

with open('sum.txt', 'w') as plik:
    for suma in sumy:
        # dlaczgo dodajesz stringa do inta?
        plik.write(suma + '\n')

# zdobyte punkty: 4/7
# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:45
# oddano o: 16:04
# oddano o: 16:22
# oddano o: 16:40
# czas potrzebny do realizacji: 115 min
# delta pomiedzy realizacja 3 a 4: 18 min

# zad 4
def analiza_tekstu():
    with open('text_txt', 'r') as plik:
        text = plik.read()
    slowa = text.split()
    slowa_count = len(slowa)
    # to suma długości a nie średnia
    sr_dl_slow = sum(len(slowa) for slowo in slowa)
    zdania_count = sum(1 for char in text if char in ".?!")

    with open('stats.txt', 'w') as plik:
        plik.write(f"Liczba słów: {slowa_count}\n")
        plik.write(f"Srednia długość słowa: {sr_dl_slow}\n")
        plik.write(f"Liczba zdań: {zdania_count}\n")

