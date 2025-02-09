# zadanie wykpnane w czasie: NIE

# zdobyte punkty: 4/4

# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:58
# oddano o: 16:22
# oddano o: 16:23
# czas potrzebny do realizacji: 98 min

with open("bin1.txt" , "r") as plik1, open("bin2.txt" , "r") as plik2:
    binn1 = [linia.strip() for linia in plik1]
    binn2 = [linia.strip() for linia in plik2]

suma = [int(bin1, 2) + int(bin2, 2) for bin1, bin2 in zip(binn1, binn2)]

with open("sum.txt", "w") as plik:
    for wynik in suma:
        plik.write(f"{wynik} \n")
