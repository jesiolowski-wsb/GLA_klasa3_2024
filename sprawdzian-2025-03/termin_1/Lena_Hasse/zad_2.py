# zdobyte punkty: 4/5

# ✅ Poprawne sortowanie nominałów malejąco
# ✅ Poprawna implementacja głównej logiki algorytmu zachłannego
# ✅ Poprawne użycie operatora dzielenia całkowitego (//) i modulo (%)
# ❌ Błędna logika sprawdzania niemożności wydania reszty - funkcja zwraca komunikat już przy pierwszym nominale większym od kwoty
# ❌ Format komunikatu o błędzie nie jest zgodny z wymaganiami

def wydaj_reszte(kwota,nominaly):
    nominaly.sort()
    nominaly.reverse()
    wynik={}
    for nominal in nominaly:
        if kwota>=nominal:
            wynik[nominal]=kwota//nominal
            kwota = kwota % nominal
        else:
            return f'Dla {kwota} nie można wydać reszty'
    return wynik
nominaly = [1, 5, 10, 25, 100]
wynik = wydaj_reszte(142, nominaly)
print(wynik)
nominaly2 = [5, 10, 25]
wynik2 = wydaj_reszte(8, nominaly2)
print(wynik2)
