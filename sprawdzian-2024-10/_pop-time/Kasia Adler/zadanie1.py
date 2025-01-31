# zadanie wykpnane w czasie: NIE

# zdobyte punkty: 6/6

# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 16:07
# czas potrzebny do realizacji: 82 min

with open("decimal.txt",  "r") as plik:
    liczby_dziesietne = [int(linia.strip()) for linia in plik]

def zamiana(num,koncowa):
    if num == 0:
        return "0"
    kaczka = []
    while num> 0:
        kaczka.append(num % koncowa)
        num //= koncowa
    return "".join(str(n) for n in reversed(kaczka))

liczby_trojkowe = [(indeks, zamiana(indeks, 3)) for indeks in liczby_dziesietne]

with open("ternary.txt" , "w") as plik:
    for liczba_dziesietna, liczba_trojkowa in liczby_trojkowe:
        plik.write(f"{liczba_dziesietna}:{liczba_trojkowa} \n")
