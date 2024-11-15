zad. 2

szerokosc=int(input("Podaj szerokosc prostokąta:"))
wysokosc=int(input("Podaj wysokosc prostokata"))
srodkowa_kolumna = szerokosc // 2 if szerokosc % 2 != 1 else -1
for i in range(wysokosc):
    for j in range(szerokosc):
        if j == srodkowa_kolumna:
            print("-", end="")
        else:
            print("*", end="")
            print()




zad.3
def potega(podstawa, wykladnik):
    if wykladnik == -1:
        return 1 / podstawa
    else:
        return 1 / podstawa * potega(podstawa, wykladnik + 1)
podstawa = 2
wykladnik = -2
wynik = potega(podstawa, wykladnik)
print(f"{podstawa} do potegi {wykladnik} wynosi {wynik}")




zad.4

import random
import string
def generuj_haslo(dlugosc):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(random.choice(znaki) for _ in range(dlugosc))
    return haslo
def sprawdz_sile_hasla(haslo):
    dlugosc = len(haslo)
    sila = 0
    if dlugosc >= 8:
        sila += 1
    if dlugosc >= 12:
        sila += 1
    if dlugosc >= 16:
        sila += 1
    if any(char.islower() for char in haslo):
            sila += 1
    if any(char.isupper() for char in haslo):
        sila += 1
    if any(char.isdigit() for char in haslo):
        sila += 1
    if any(char in string.punctuation for char in haslo):
        sila += 1
    if sila <= 2:
        ocena = "Słabe"
    elif sila <= 4:
        ocena = "Średnie"
    elif sila <= 6:
        ocena = "Mocne"
    else:
        ocena = "Bardzo mocne"

    return ocena
if __name__ == "__main__":
  dlugosc = int(input("Podaj długość hasła: "))
  haslo = generuj_haslo(dlugosc)
  ocena_sily = sprawdz_sile_hasla(haslo)
  print(f"Wygenerowane hasło: {haslo}")
  print(f"Siła hasła: {ocena_sily}")

zad.1 
tekst = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

samogloski = "aeiou"
liczba_samoglosek = 0

for znak in tekst.lower():
    if znak in samogloski:
        liczba_samoglosek += 1

print(f"Liczba samogłosek w tekście wynosi: {liczba_samoglosek}")
