# zdobyte punkty: 4.5/6
# ✅ Doskonała implementacja rekurencyjna z pamięcią
# ❌ Wersja iteracyjna zwraca 1 zamiast [0] dla n=1 - powinno być return [0]
# ⚠️ Brak obsługi przypadku n=0 w wersji iteracyjnej

def fib_rek(n):
    obliczone = {0: 0, 1: 1}
    def fib_pamiec(k):
        if k in obliczone:
            return obliczone[k]

        obliczone[k]=fib_pamiec(k-1)+fib_pamiec(k-2)
        return obliczone[k]

    tablica=[]
    for i in range(n):
        tablica.append(fib_pamiec(i))

    return tablica



def fib_it(n):
    if n<=0:
        return []
    if n==1:
        return 1
    ciag=[0,1]
    for i in range(2,n):
        ciag.append(ciag[i-1]+ciag[i-2])
    return ciag

print(fib_it(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib_rek(10))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
