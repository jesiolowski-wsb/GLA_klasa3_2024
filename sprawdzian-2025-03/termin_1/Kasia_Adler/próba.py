# zdobyte punkty 1/6

# ✅ Poprawne otwarcie pliku
# ❌ Błąd w odczytywaniu zawartości pliku - read() wczytuje cały plik jako jeden string, podczas gdy zadanie wymaga przetwarzania linii osobno
# ❌ Błędna logika sprawdzania wielkich liter
# ❌ Błąd w implementacji funkcji co_n_ty_znak - próba użycia zamkniętego już pliku
# ❌ Brak zapisu wyników do pliku (zakomentowany kod)
# ❌ Ogólna niekompletność rozwiązania

with open("tajny_przekaz.txt", "r") as plik:
    # Użyj readlines() aby wczytać plik jako listę linii:
    # slowa = [line.strip() for line in plik.readlines()]
    slowo = plik.read().strip()

najwiecej = []
if slowo.isupper():
    duzel = slowo

    # do zliczania wielkich liter użyj:
    # max_wielkich = 0
    # slowo_z_max = ""
    # for slowo in slowa:
    #     wielkie = sum(1 for znak in slowo if znak.isupper())
    #     if wielkie > max_wielkich:
    #         max_wielkich = wielkie
    #         slowo_z_max = slowo

    if len(duzel)> len(najwiecej):
        najwiecej = duzel
        print(najwiecej[0])


#############################################################
litery = ""
def co_n_ty_znak(plik,n,start = 9):
    print(plik)
    return plik[start::n]

dziesiate = co_n_ty_znak(plik,10,9)




    #with open("wyniki1.txt", "w") as kaczka:
        #kaczka.append(pingwin)
