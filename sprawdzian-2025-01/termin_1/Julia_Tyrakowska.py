# suma zdobytych punktow: 8/20
# zad.1: 6/6
# zad.2: 2/6
# zad.3: 0/8

def bramki_and(a,b):
    return a and b

print(bramki_and(True, False ))

def bramki_or(a,b):
    return a or b
print(bramki_or(True, False))

def bramki_not(a):
    return not a
print(bramki_not(True))

# szkoda że zabrakło implementacji pętli która by odpalała tabelę
# rzuć okiem na sugerowane rozwiązanie na https://github.com/jesiolowski-wsb/GLA_klasa3_2024/blob/main/sprawdzian-2025-01/termin_1/readme.md
def wyswietl_tabele_prawdy():
    print("a    b    AND    OR     NOT(a)")
    print("-----------------------------------")

    wartosc_logiczna = [True, False]
