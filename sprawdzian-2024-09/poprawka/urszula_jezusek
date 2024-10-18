1 ZADANIE
def zlicz_samogloski(tekst):
    samogloski = "aeiou"
    licznik = 0

    for znak in tekst.lower():
        if znak in samogloski:
            licznik += 1

    return licznik

tekst = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

wynik = zlicz_samogloski(tekst)
print(f'Liczba wystąpień samogłosek: {wynik}')



2 ZADANIE

def rysuj_prostokat(szerokosc, wysokosc):
    for i in range(wysokosc):
        if szerokosc % 2 == 1:
            myslinik = '*' * (szerokosc // 2) + '-' + '*' * (szerokosc // 2)
            print(myslinik)
        else:
            print('*' * szerokosc)
szerokosc = int(input("Podaj szerokość prostokąta: "))
wysokosc = int(input("Podaj wysokość prostokąta: "))

rysuj_prostokat(szerokosc, wysokosc)



3 ZADANIE

def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    return podstawa * potega(podstawa, wykladnik - 1)

podstawa = float(input("Podaj podstawę: "))
wykladnik = int(input("Podaj wykładnik (nieujemny): "))

if wykladnik < 0:
    print("Wykładnik musi być liczbą nieujemną.")
else:
    wynik = potega(podstawa, wykladnik)
    print(f'{podstawa} do potęgi {wykladnik} wynosi: {wynik}')


4 ZADANIE
import random
import string

def generuj_haslo(dlugosc):
    male_litery = string.ascii_lowercase
    wielkie_litery = string.ascii_uppercase
    cyfry = string.digits
    znaki_specjalne = string.punctuation

    wszystkie_znaki = male_litery + wielkie_litery + cyfry + znaki_specjalne

    haslo = ''.join(random.choice(wszystkie_znaki) for _ in range(dlugosc))
    return haslo

def sprawdz_sile_hasla(haslo):
    sila = 0

    if len(haslo) >= 8:
        sila += 1

    if any(char.islower() for char in haslo):
        sila += 1
    if any(char.isupper() for char in haslo):
        sila += 1
    if any(char.isdigit() for char in haslo):
        sila += 1
    if any(char in string.punctuation for char in haslo):
        sila += 1

    return sila

dlugosc_hasla = int(input("Podaj długość hasła: "))
wygenerowane_haslo = generuj_haslo(dlugosc_hasla)
sila_hasla = sprawdz_sile_hasla(wygenerowane_haslo)

print(f"Wygenerowane hasło: {wygenerowane_haslo}")
print(f"Siła hasła (1-5): {sila_hasla}")

