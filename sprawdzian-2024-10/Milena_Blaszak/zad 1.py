# Zdobyte punkty: 3/6

# w zadaniu byla prosba o wczytanie innego pliku niz plik.txt
plik = open("plik.txt","r")
liczba = plik.read()

# algorytm prawie dobry, jednak z nieuzywanymi zmiennymi i z tego powodu nie dający dobrego wyniku
# po poprawkach działa poprawnie
def dziesietne_na_binarne(liczba):
    wynik = ''
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba //= 2
    return wynik

# funkcjonalnosc chyba nie dziala
dziesietne_na_binarne(liczba)

# brak zapisu do pliku
print(wynik)

