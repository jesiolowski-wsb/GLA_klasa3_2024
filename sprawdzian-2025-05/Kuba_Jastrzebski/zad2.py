#zdobyte punkty: 3/5
# ✅ Rekurencyjna struktura NWD jest poprawna: return nwd(b, a % b)
# ❌ Błędna logika warunków: if a < 1 and b < 1 i if a > 0 and b < 1 - nie obsługuje wartości ujemnych ani przypadku b=0
# ❌ Brak obsługi abs() - funkcje mogą zwracać ujemne wartości

def nwd(a:int,b:int):
    if a < 1 and b < 1: return 0
    if a > 0 and b < 1: return a
    return nwd(b, a % b)

def nww(a:int, b:int):
    if a < 1 and b < 1: return 0
    return (a * b) // nwd(a, b)


print(nwd(13, 17))
print(nww(7, 13))