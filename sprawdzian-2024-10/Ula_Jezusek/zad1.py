# Zdobyte punkty: 3/6

plik = open('liczby.txt', 'r')
wiersze = plik.readlines()
print(wiersze)
wynik = ""

# bardzo dobre podejscie - w dodatku dziala :d
def zamiana():
    while wiersz > 0:
        wynik = str(wiersz % 2) + wynik
        # sugerowałby dzielenie bez reszty tj // zamiast /
        wiersz = wiersz / 2

# brak zapisu do pliku
print(wynik)
