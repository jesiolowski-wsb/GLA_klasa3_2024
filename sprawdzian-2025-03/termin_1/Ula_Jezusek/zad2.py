#zdobyte punkty 4.5/5
# ✅ Poprawne sortowanie nominałów malejąco
# ✅ Poprawna implementacja algorytmu zachłannego
# ✅ Poprawne użycie operatorów dzielenia całkowitego (//) i modulo (%)
# ✅ Sprawdzenie czy udało się wydać całą resztę
# ❌ Zwracanie stringa zamiast None przy niemożności wydania reszty (niezgodne z treścią zadania)

nominaly = [1, 5, 10, 25, 100]
kwota = 142
def wydaj_reszte(kwota, nominaly):
    wynik = {}
    for nominal in sorted(nominaly, reverse=True):
        if kwota >= nominal:
            ilosc = kwota // nominal
            wynik[nominal] = ilosc
            kwota = kwota % nominal

    if kwota == 0:
        return wynik
    else:
        return "nie można wydać reszty"

print(wydaj_reszte(kwota, nominaly))
