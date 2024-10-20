#zadanie1 
def zlicz_samogloski(tekst):
    samogloski = 'aeiouAEIOU'
    licznik = 0

    for znak in tekst:
        if znak in samogloski:
            licznik += 1

    return licznik

tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

wynik = zlicz_samogloski(tekst)
print(f"Liczba wystąpień samoglosek {wynik}")

#zadanie2
def rysuj_prostokat(szerokosc, wysokosc):
    for i in range(wysokosc):
        if szerokosc % 2 == 1:
            myslnik = '*' * (szerokosc//2) + '-' + '*' * (szerokosc//2)
            print(myslnik)
        else:
            print('*' * szerokosc)


szerokosc = int(input("Podaj szerokosc prostokąta:" ))
wysokosc = int(input("Podaj wysokosc prostokąta:"))

rysuj_prostokat(szerokosc, wysokosc )

#zad3
def potega(podstawa , wykladnik):
    if wykladnik == 0:
        return 1
    else:
        return podstawa * potega(podstawa, wykladnik - 1)

podstawa = float(input("Podaj podstawę: "))
wykladnik = int(input("Podaj wykladnik(liczba nieujemna): "))

if wykladnik <0:
    print("wykladnik musi byc liczba nieujemną")
else:
    wynik = potega(podstawa, wykladnik)
    print(f"{podstawa} do potegi {wykladnik} wynosi: {wynik}")

#zad4
import random
import string


def generuj_haslo(dlugosc):
    if dlugosc < 1:
        return ""


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


