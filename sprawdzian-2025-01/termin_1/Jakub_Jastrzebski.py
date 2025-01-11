# suma zdobytych punktow: 21/20
# zad.1: 6/6
# zad.2: 6/6
# zad.3: 9/8

# wystarczyłoby 'return a and b' :)
def AND(a, b):
    if a and b:
        return True
    return False

# wystarczyłoby 'return a or b' :)
def OR(a, b):
    if a or b:
        return True
    return False

def NOT(a):
    return not a

def wyswietl_tabele_prawdy():
    print("a     b     AND    OR     NOT(a)\n"
          "-----------------------------------")
    # troszkę czytelniej byłoby po prostu 'in [False, True]'
    # range(2) wymaga pomyślenia że:
    # - liczymy od 0, wiec bedzie 0 i 1
    # - 0 i 1 to integer, ale gdy spojrze w funkcje AND czy OR to tam sa wartosci boolowe
    # - czyli tutaj pewnie chodzi o rzutowanie 0 i 1 na wartosci boolowe
    # kupa roboty dla mózgu
    # w wolnej chwili rzuc okiem na artykul https://minds.md/zakirullin/cognitive
    # to o innym jezyku, ale samo pojęcie 'cognitive load' jest tu istotne
    for a in range(2):
        for b in range(2):
            print(f"{a}{b:6}{AND(a,b):6}{OR(a,b):7}{NOT(a):7}")

def COMPLEX(a, b, c):
    # swietnie przyuwazone ze nie trzeba `return (a and b) or (not c)` :)
    # gratki
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
