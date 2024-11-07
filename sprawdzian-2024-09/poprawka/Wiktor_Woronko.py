# zad. 2
# zdobyte punkty: 2/5
szerokosc=int(input("Podaj szerokosc prostokąta: "))
wysokosc=int(input("Podaj wysokosc prostokata: "))
# odwrotna kolejność w definicji zmiennej 'srodkowa kolumna'
# j w IF oczekuje wartości True
# przy zalozeniu ze 'szerokosc' = 4
# print(4 % 2) # 0 tj. False
# print(4 % 2 != 1) # True (negacja False)
# print(4 // 2) # 2
# print(4 // 2 if 4 % 2 != 1 else -1) # zwróci 2 (lewa strona) tj True
#
# przy zalozeniu ze 'szerokosc' = 5
# print(5 % 2) # 1 tj. True
# print(5 % 2 != 1) # False (negacja True)
# print(5 // 2) # 2
# print(5 // 2 if 5 % 2 != 1 else -1) # zwróci -1 (prawa strona) tj False
srodkowa_kolumna = -1 if szerokosc % 2 != 1 else szerokosc // 2

for i in range(wysokosc):
    for j in range(szerokosc):
        # czy nie byloby latwiej sprawdzic czy:
        # - reszta z dzielenia to True (1)
        # - obecny element j = szerokosc // 2
        # tj: if szerokosc % 2 == 1 and j == szerokosc // 2
        if j == srodkowa_kolumna:
            print("-", end="")
        else:
            print("*", end="")
    # dla kazdego znaku w obrębie 'else' doklejany był na koncu 'enter'
    # teraz 'enter' jest nie dla kazdego elementu j, lecz kazdego i
    print()


# zad.3
# zdobyte punkty: 5/6
# ale naprawdę WARUNKOWO - zadanie dotyczyło liczb NIEUJEMNYCH
# a rozwiązanie jesty tylko dla liczb ujemnych
def potega(podstawa, wykladnik):
    if wykladnik == -1:
        return 1 / podstawa
    else:
        return 1 / podstawa * potega(podstawa, wykladnik + 1)
podstawa = 2
wykladnik = -2
wynik = potega(podstawa, wykladnik)
print(f"{podstawa} do potegi {wykladnik} wynosi {wynik}")


# zad.4
# zdobyte punkty: 4/7, ale potencjalnie 7/7
# Obawiam się ze ta odpowiedź byla mocno wspomagana pomocami typu chatGPT
# pogadajmy proszę o tym kodzie na zajęciach i jeśli będziesz w stanie wytlumaczyc
# jak działa - podbiję ocenę o 7pkt
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


# zad.1
# zdobyte punkty: 4/4
tekst = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

samogloski = "aeiou"
liczba_samoglosek = 0

for znak in tekst.lower():
    if znak in samogloski:
        liczba_samoglosek += 1

print(f"Liczba samogłosek w tekście wynosi: {liczba_samoglosek}")
