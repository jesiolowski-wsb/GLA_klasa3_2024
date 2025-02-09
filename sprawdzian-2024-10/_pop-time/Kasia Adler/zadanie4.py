# zadanie wykpnane w czasie: NIE

# zdobyte punkty: 7/7

# rozpoczęto o: 14:45
# planowane zakończenie: 15:30

# oddano o: 15:59
# oddano o: 16:34
# czas potrzebny do realizacji: 109 min

with open("text.txt" , "r") as plik:
    tekst = plik.read()

slowa = tekst.split()
liczba_slow = len(slowa)
srednia_dlugosc_slowa = round(sum(len(slowo) for slowo in slowa) / liczba_slow if liczba_slow > 0 else 0 , 1)

# split podzieli na slowa a potem zliczy slowa konczace sie na znak interpunkcyjny - wynik caly czas poprawny
liczba_zdan = len([zdanie for zdanie in tekst.split() if zdanie.endswith((".","!","?"))])

with open("stats.txt", "w") as plik:
        plik.write(f"Liczba slow : {liczba_slow} \n")
        plik.write(f"Srednia dlugosc slowa : {srednia_dlugosc_slowa} \n")
        plik.write(f"Liczba zdan : {liczba_zdan}")

