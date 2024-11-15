def dec_to_bin(dec):
    bin = ""
    while True:
        if dec / 2 != 0:
            bin += str(dec % 2)
            dec -= dec % 2
            dec //= 2
        else: break
    return int(bin)

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