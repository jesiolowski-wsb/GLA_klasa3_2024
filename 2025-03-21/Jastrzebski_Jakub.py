import time
def wydaj_reszte_zachlanny(reszta, wielkosci):
    wyjscie = []
    wielkosci.sort(reverse=True)
    for nominal in wielkosci:
        a = reszta // nominal
        reszta -= a * nominal
        while a > 0:
            wyjscie.append(nominal)
            a -= 1
        if reszta == 0: break
    return reszta, wyjscie

def wydaj_reszte_optymalny(reszta, wielkosci):
    start = time.time()
    wyjscia = []
    temp_nominaly = []
    wielkosci.sort()
    for nominal in wielkosci:
        temp_nominaly.append(nominal)
        wyjscia.append(wydaj_reszte_zachlanny(reszta, temp_nominaly))
    wyjscia.sort(key=length)
    stop = time.time()
    return wyjscia[0], stop - start

def length(x): return len(x[1])

nominaly = [1, 3, 4]
kwota = 123450
a = wydaj_reszte_zachlanny(kwota, nominaly)
if a[0] > 0:  print(f"{a[1]}, ale zostało jeszcze {a[0]} do wydania, wydano {len(a[1])} monet/y/ę")
print(f"{a[1]}, wydano {len(a[1])} monet/y/ę")

b = wydaj_reszte_optymalny(kwota, nominaly)
if b[0][0] > 0:  print(f"{b[0][1]}, ale zostało jeszcze {b[0][0]} do wydania, wydano {len(b[0][1])} monet/y/ę")
print(f"{b[0][1]}, wydano {len(b[0][1])} monet/y/ę")
print(b[1])