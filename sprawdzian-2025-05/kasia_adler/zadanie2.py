# zdobyte punkty: 5/5
# ✅ Iteracyjna implementacja NWD while b != 0: c = a%b; a = b; b = c jest poprawna i wydajna
# ✅ Poprawna obsługa przypadków brzegowych w NWW: if a == 0 or b == 0: return 0
# ⚠️ Brak abs() w funkcji nwd - dla ujemnych liczb może zwrócić ujemny NWD (np. nwd(-12, 8) zwróci -4)

def nwd(a,b):
    while b!= 0:
        c = a%b
        a = b
        b = c
    return a
print(nwd(0,14))

def nww(a,b):
    if a == 0 or b == 0:
        return 0
    return abs(a*b)//nwd(a,b)

print(nww(0,13))
