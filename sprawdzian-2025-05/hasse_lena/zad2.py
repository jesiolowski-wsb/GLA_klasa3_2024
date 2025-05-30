# zdobyte punkty: 4/5
# ✅ Rekurencyjna implementacja NWD jest poprawna
# ❌ Brak obsługi wartości bezwzględnych w funkcji nwd - może dawać błędne wyniki dla liczb ujemnych
# ⚠️ nadmiarowe abs() w NWW - liczby są już dodatnie po pierwszym abs()

def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)


def nww(a,b):
    a,b=abs(a),abs(b)
    return (abs(a)*abs(b))//nwd(a,b)

print(nwd(12, 18))  # 6
print(nwd(35, 14))  # 7
print(nwd(13, 7))   # 1
print()
print(nww(12, 18))  # 36
print(nww(6, 8))    # 24
print(nww(7, 13))   # 91
