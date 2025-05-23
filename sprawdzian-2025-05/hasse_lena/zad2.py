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
