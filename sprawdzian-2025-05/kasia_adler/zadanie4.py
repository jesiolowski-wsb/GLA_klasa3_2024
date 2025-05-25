# zdobyte punkty: 4/5
# ❌ Błąd na poziomie rozumienia: wspólny_dzielnik = nww(m1,m2) - NWW mianowników to wspólny mianownik, nie dzielnik!
# ✅ Algorytmy są merytorycznie poprawne: normalizacja znaku, użycie NWD do skracania, dodawanie przez wspólny mianownik

def nwd(a,b):
    while b!= 0:
        c = a%b
        a = b
        b = c
    return a

def nww(a,b):
    if a == 0 or b == 0:
        return 0
    return abs(a*b)//nwd(a,b)

def skróć_ułamki(licznik, mianownik):
    if mianownik == 0:
        raise ValueError("Mianownik nie może być 0")
    znak = 1
    if (licznik < 0 and mianownik > 0) or (licznik > 0 and mianownik < 0):
        znak = -1

    licznik, mianownik = abs(licznik), abs(mianownik)

    dzielnik = nwd(licznik,mianownik)
    licznik = znak*(licznik//dzielnik)
    mianownik = mianownik//dzielnik

    return(licznik,mianownik)

print(skróć_ułamki(12,18))

def dodaj_ułamki(l1,m1,l2,m2):
    if m1 == 0  or m2 == 0:
        raise ValueError("Mianowniki nie mogą być zerami")

    wspólny_dzielnik = nww(m1,m2)
    licznik = l1*(wspólny_dzielnik//m1) + l2*(wspólny_dzielnik//m2)

    return skróć_ułamki(licznik,wspólny_dzielnik)

print(dodaj_ułamki(1,2,1,3))

def odejmij_ułamki(l1,m1,l2,m2):
    return dodaj_ułamki(l1,m1,-l2,m2)

print(odejmij_ułamki(3,4,1,2))



