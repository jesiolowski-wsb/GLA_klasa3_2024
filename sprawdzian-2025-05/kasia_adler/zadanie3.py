# zdobyte punkty: 6/6
# ✅ Wzorcowa implementacja rekurencyjna z memoizacją: juz_obliczone = {0:0, 1:1} i sprawdzaniem if k in juz_obliczone
# ✅ Doskonała wersja iteracyjna z prawidłową obsługą: if n <= 0: return [] i if n == 1: return [0]
# ✅ Oba rozwiązania są eleganckie, wydajne i bezbłędne - dokładnie jak wzorcowe rozwiązanie
def fib_rekurencyjnie(n):
    juz_obliczone = {0:0, 1:1}

    def fib_z_zapamietywaniem(k):
        if k in juz_obliczone:
            return juz_obliczone[k]

        juz_obliczone[k] = fib_z_zapamietywaniem(k-1) + fib_z_zapamietywaniem(k-2)
        return juz_obliczone[k]
    wynik = []
    for i in range(n):
        wynik.append(fib_z_zapamietywaniem(i))

    return wynik

print(fib_rekurencyjnie(10))

def fib_iteracyjnie(n):
    if n <= 0:
        return[]
    if n == 1:
        return [0]

    wyniki = [0,1]

    for i in range(2,n):
        wyniki.append(wyniki[i-1]+wyniki[i-2])

    return wyniki

print(fib_iteracyjnie(10))

