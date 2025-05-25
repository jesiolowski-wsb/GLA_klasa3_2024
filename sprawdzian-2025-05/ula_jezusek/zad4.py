def skroc_ulamek(licznik, mianownik):
    if mianownik ==0:
        raise ValueError("nie można dzielić przez zero")
    znak = 1
    if (licznik < 0 and mianownik > 0) or (licznik > 0 and mianownik < 0):
        znak = -1
    dzielnik = nwd(licznik, mianownik)
    nowy_licznik = licznik/dzielnik
    nowy_mianownik= mianownik/dzielnik
    return nowy_licznik, nowy_mianownik
def dodaj_ulamki(l1,m1,l2,m2):
    if m1 == 0 or m2 == 0:
        raise ValueError("Nie można dzielić przez zero")
    wspolny_mianownik = nww(m1,m2)
    nowy_licznik = l1*(wspolny_mianownik // m1) + l2*(wspolny_mianownik//m2)
    return skroc_ulamek(nowy_licznik, wspolny_mianownik)
def odejmowanie_ulamkow(l1,m1,l2,m2):
    return dodaj_ulamki(l1, m1,-l2, m2)
