# zdobyte punkty: 5/5
# ✅ Doskonała implementacja NWD: rekurencja z abs() i poprawną obsługą przypadku b == 0
# ⚠️ Błąd w NWW: wynik = (a*b)/nwd(a,b) zwraca float zamiast int - powinno być // dzielenie całkowite
# ✅ Poprawna obsługa wartości bezwzględnych w obu funkcjach

def nwd(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return nwd(b, a % b)
def nww(a, b):
    a, b =abs(a), abs(b)
    wynik = (a*b)/nwd(a,b)
    return wynik
