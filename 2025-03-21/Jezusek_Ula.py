nominaly = [2, 5, 10, 20, 50, 100, 200, 500]
kwota = 543

def wydaj_reszte(a, b):
    wynik = []
    i = len(b)-1
    while i >= 0:
        c = a // b[i]
        d = a % b[i]
        for _ in range(c):
            wynik.append(b[i])
        a = d
        i = i - 1
    if a == 0:
        return wynik
    else:
        print("nie można wydać reszty")
        return 0
wartosc = wydaj_reszte(kwota, nominaly)
print(wartosc)

def liczba_monet(w):
    if w == 0:
        return 0
    else:
        i = 0
        for x in w:
            if x < 10:
                i = i + 1
        return i
print(liczba_monet(wartosc))
