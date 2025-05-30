# zdobyte punkty: 3.5/5
# ❌ Poważny błąd w skroc_ulamek: (licznik//dzielnik)//znak zamiast (licznik//dzielnik)*znak
# ❌ Błędna logika w dodaj_ulamki - sprawdza liczniki zamiast mianowników, nie używa NWW poprawnie
# ❌ Niepoprawne parametry w odejmij_ulamki - kolejność argumentów jest błędna

def nwd_it(a,b):
    a,b=abs(a), abs(b)
    while b:
        a,b=b,a%b
    return a

def skroc_ulamek(licznik,mianownik):
    znak=1
    if (licznik>0 and mianownik<0) or (licznik<0 and mianownik>0):
        znak=-1
    licznik,mianownik=abs(licznik),abs(mianownik)
    dzielnik=nwd_it(licznik,mianownik)
    return (licznik//dzielnik)//znak,mianownik//dzielnik

print(skroc_ulamek(-12,18))

def dodaj_ulamki(l1, m1, l2, m2):
    if l1==0 or l2==0:
        return ValueError, 'mianownik nie może być 0'
    e=l1*m2 + l2*m1
    f=m1*m2
    dzielnik=nwd_it(m1,m2)
    return e//dzielnik,f//dzielnik

print(dodaj_ulamki(1, 2, 1, 3))

def odejmij_ulamki(l1,l2,m1,m2):
    return dodaj_ulamki(l1,-l2,m1,m2)

print(odejmij_ulamki(3, 4, 1, 2))
