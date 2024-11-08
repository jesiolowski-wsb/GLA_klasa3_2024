# Zdobyte punkty: 3/6
# brak zapisu do pliku
# brak wywołania dla danych wczytanych z pliku

plik = open('liczby.txt', 'r')
zawartosc = plik.read()
plik.close()

# super! sam algorytm jak najbardziej działa!
def dziesietny_na_binarny(liczba):
    wynik = ''
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba //= 2
    return wynik

# nie rozumiem tej wartości
liczba = 123561351728352719356729683167891638714923687901748324903184714791804687648790168471904849016841064874091784164901649061489106481634906482164891206481902648164810964891649016841648096184036189461461064106541
print(dziesietny_na_binarny(liczba))
