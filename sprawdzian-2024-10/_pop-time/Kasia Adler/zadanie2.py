# zadanie wykpnane w czasie: NIE

# zdobyte punkty: 5/5

# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:58
# oddano o: 16:17
# czas potrzebny do realizacji: 92 min

# w jakim celu ta funkcja?
def pingwin():
    with open("phones.txt", "r") as plik:
        numery = [linia.strip() for linia in plik]

    poprawne = [num for num in numery if len(num) == 9 and num[0] in ("5", "6")]

    with open("valid_phones.txt", "w") as plik:
        for num in poprawne:
            plik.write(f"{num} \n")




pingwin()

