# suma zdobytych punktow: 12/20
# zad.1: 6/6
# zad.2: 6/6
# zad.3: 0/8

# te a i b sa tutaj kompletnie niepotrzebne
a=1
b=2

# istnieje kilka konwencji pisania nazw zmiennych / funkcji
# https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/
# w pythonie popularne jest pisanie funkcji albo jako camelCase, albo jako snake_case
# więc tutaj widziałby albo bramka_and lub bramkaAnd
def bramkaand(a,b):
    return a and b

def bramkaor(a,b):
    return a or b

def bramkanot(a):
    return not a

# powtórzenie niepotrzebnych zmiennych a i b
a=1
b=2

# powtórzenie funkcji z zadania 1 -
# redefiniowanie funkcji nie jest dozwolone w zadnym z jezykow programowania
def bramkaand(a,b):
    return a and b

def bramkaor(a,b):
    return a or b

def bramkanot(a):
    return not a


def wyswietl_tabele_prawdy():
    print("a    b    and     or     not(a)")
    print('--------------------------------')
    # absolutnie gratuluje dobrego podejscia do listowania elementów listy
    for a in [False, True]:
        for b in[False, True]:
            print(int(a),int(b), int(bramkaand(a,b)),int(bramkaor(a,b)),int(bramkanot(a)))

wyswietl_tabele_prawdy()
