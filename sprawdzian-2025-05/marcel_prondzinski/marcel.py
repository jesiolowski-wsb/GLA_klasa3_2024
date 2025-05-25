# zdobyte punkty: 4/5
# ✅ Doskonała iteracyjna implementacja NWD: while b!=0: a,b=b,a%b z prawidłową obsługą abs()
# ❌ Błąd w NWW: return abs(a*b/nwd(a,b)) zwraca float - powinno być // dla dzielenia całkowitego
# ✅ Poprawna obsługa przypadków brzegowych: if a==0 or b==0: return 0

# zad 2
def nwd(a,b):
    a,b= abs(a),abs(b)

    while b!=0:
      a,b=b,a%b
    return a



def nww(a,b):

    if a==0 or b==0:
        return 0

    return abs(a*b/nwd(a,b))



print(nwd(12, 18))  # 6
print(nwd(35, 14))  # 7
print(nwd(13, 7))   # 1

print(nww(12, 18))  # 36
print(nww(6, 8))    # 24
print(nww(7, 13))   # 91

#zdobyte punkty: 6/6
# ✅ Wzorcowa implementacja rekurencyjna z memoizacją: juz_obliczone = {0:0, 1:1} i funkcja pomocnicza
# ✅ Doskonała wersja iteracyjna z prawidłową obsługą przypadków brzegowych if n<=0 i if n==1
# ✅ Oba rozwiązania są bezbłędne i zgodne ze specyfikacją - pełna punktacja
# zad 3
# ----------------------------------iteracyjnie---------------------------------------------------
n=int(input("podaj liczbe"))
def fib_iteracyjnie(n):
    if n<=0:
        return[]
    if n==1:
        return[0]

    wyniki =[0, 1]

    for i in range(2,n):
        wyniki.append(wyniki[i-1]+ wyniki[i-2])
    return wyniki
print(fib_iteracyjnie(n))
# -----------------------------REKURENCYJNIE ------------------------------------------------------------
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

print(fib_rekurencyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
