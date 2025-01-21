# zad 1 i 2
a=1
b=2
def bramkaAND(a,b):
    return a and b

def bramkaOR(a,b):
    return a or b

def bramkaNOT(a):
    return not a

def wyswietl_tabele_prawdy():
    print("a    b    AND     OR     NOT(a)")
    print('--------------------------------')
    for a in [True, False]:
        for b in[True, False]:
            print(int(a),int(b),int(bramkaAND(a,b)),int(bramkaOR(a,b)),int(bramkaNOT(a)))

wyswietl_tabele_prawdy()
