# zdobyte punkty: 6/6
# ✅ Algorytm jest poprawny i elegancko napisany z enumerate w list comprehension
# ⚠️ Niepotrzebny import floor - int(sqrt(n)) wystarczy, ale kod działa poprawnie

from math import sqrt, floor

def znajdz_pierwsze(n):
    IsPrimary = [True for i in range(n+1)]
    IsPrimary[0] = False
    IsPrimary[1] = False
    for i in range(2, floor(sqrt(n)) + 1):
        if IsPrimary[i]:
            for j in range(i**2, n, i):
                IsPrimary[j] = False
    return [index for index, i in enumerate(IsPrimary) if i]

print(znajdz_pierwsze(47))