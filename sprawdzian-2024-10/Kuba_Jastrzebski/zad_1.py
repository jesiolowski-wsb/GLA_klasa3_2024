# Zdobyte punkty: 4/6

def dec_to_bin(dec):
    bin = ""
    while True:
        if dec / 2 != 0:
            bin += str(dec % 2)
            dec -= dec % 2
            dec //= 2
        else: break
    # prawie dobrze, z czego jeśli wartość string= 0001, to po zarzutowaniu na INT będzie 1 :(
    # ustawienie str() rozwiązuje sprawę
    # dodatkowo, konwersja polega na czytaniu od tyłu, stąd więc [::-1]
    return str(bin)[::-1]

with open("liczby.txt", "r") as file:
    liczby = list(file.read().replace("\n", ""))

wyniki = []

for liczba in liczby:
    wynik = liczba
    wynik = dec_to_bin(int(wynik))
    wyniki.append(wynik)

with open("wyniki.txt", "w") as file:
    for i in range(len(liczby)):
        file.write(f"{liczby[i]} : {wyniki[i]}\n")