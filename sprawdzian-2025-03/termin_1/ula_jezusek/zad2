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
