def nwd(a:int,b:int):
    if a < 1 and b < 1: return 0
    if a > 0 and b < 1: return a
    return nwd(b, a % b)

def nww(a:int, b:int):
    if a < 1 and b < 1: return 0
    return (a * b) // nwd(a, b)


print(nwd(13, 17))
print(nww(7, 13))