# wynik: 2/3

# zadanie 3
def rysuj_prostokat(wysokosc, szerokosc):
    # to nie najlepszy pomysł tworzyć zmienne o nazwie funkcji
    # proponowałbym jakąś unikalną nazwę zmiennej np rzędy lub kolumny
    for rysuj_prostokat in range (wysokosc):
        print ('#'* szerokosc)

# coś tu chyba nie poszło zgodnie z planem :)
# pozwolę sobie dodać wartości aby zobaczyć czy program działa
szerokosc_prostokata = 2
wysokosc_prostokata = 5
rysuj_prostokat(szerokosc_prostokata, wysokosc_prostokata)

# w wyniku wywołania dostałem kształt wysokość 2 i szerokość 5
# wg nazw zmiennych powinno być odwrotnie :)
 #####
 #####