# zdobyte punkty: 4/5
# ✅ Kreatywne rozwiązanie normalizacji znaku: if licznik * mianownik > 0 sprawdza czy znaki są zgodne
# ❌ Nieefektywność: nwd(licznik, mianownik) wywoływane dwukrotnie w skroc_ulamek, nww(m1, m2) aż 4 razy w dodawaniu
# ❌ Te same błędy w NWD/NWW co w zadaniu 2

def nwd(a:int,b:int):
    if a < 1 and b < 1: return 0
    if a > 0 and b < 1: return a
    return nwd(b, a % b)

def nww(a:int, b:int):
    if a < 1 and b < 1: return 0
    return (a * b) // nwd(a, b)


def skroc_ulamek(licznik, mianownik):
    if licznik * mianownik > 0: licznik, mianownik = abs(licznik), abs(mianownik)
    else: licznik, mianownik = -abs(licznik), abs(mianownik)
    return licznik // nwd(licznik, mianownik), mianownik // nwd(licznik, mianownik)

def dodaj_ulamki(l1, m1, l2, m2):
    l1 *= (nww(m1, m2) // m1)
    l2 *= (nww(m1, m2) // m2)
    m1, m2 = nww(m1, m2), nww(m1, m2)
    return skroc_ulamek(l1+l2, m1)

def odejmij_ulamki(l1, m1, l2, m2):
    l1 *= (nww(m1, m2) // m1)
    l2 *= (nww(m1, m2) // m2)
    m1, m2 = nww(m1, m2), nww(m1, m2)
    return skroc_ulamek(l1-l2, m1)


