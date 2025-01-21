def AND(a, b):
    if a and b:
        return True
    return False

def OR(a, b):
    if a or b:
        return True
    return False

def NOT(a):
    return not a

def wyswietl_tabele_prawdy():
    print("a     b     AND    OR     NOT(a)\n"
          "-----------------------------------")
    for a in range(2):
        for b in range(2):
            print(f"{a}{b:6}{AND(a,b):6}{OR(a,b):7}{NOT(a):7}")

def COMPLEX(a, b, c):
    return OR(AND(a,b), NOT(c))


def complex_chart():
    print("a     b     c     COMPLEX(a,b,c)\n"
          "------------------------------")
    for a in range(2):
        for b in range(2):
            for c in range(2):
                print(f"{a}{b:6}{c:6}{int(COMPLEX(a, b , c)):6}")

wyswietl_tabele_prawdy()
print("\n"*2)
complex_chart()
