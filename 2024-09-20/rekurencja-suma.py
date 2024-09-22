# Napisz funkcję rekurencyjną o nazwie suma_od_1_do_n, która przyjmuje jedną liczbę
# całkowitą n i zwraca sumę wszystkich liczb całkowitych od 1 do n.
#
# Na przykład:
# Dla n = 5, suma_od_1_do_n(5) powinno zwrócić 15 (1 + 2 + 3 + 4 + 5).
# Dla n = 3, suma_od_1_do_n(3) powinno zwrócić 6 (1 + 2 + 3).

def suma_od_1_do_n(n):
    # Przypadek bazowy 1: Gdy n wynosi 0, suma wynosi 0.
    if n == 0:
        return 0
    # Przypadek bazowy 2: Gdy n wynosi 1, suma wynosi 1.
    elif n == 1:
        return 1
    # Przypadek ogólny: Suma od 1 do n to suma od 1 do (n-1) plus n.
    else:
        return n + suma_od_1_do_n(n - 1)

# Testy działania funkcji
print(suma_od_1_do_n(5))  # Powinno zwrócić 15
print(suma_od_1_do_n(3))  # Powinno zwrócić 6
