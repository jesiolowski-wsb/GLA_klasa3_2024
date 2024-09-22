# Silnia to iloczyn wszystkich liczb naturalnych od 1 do n (tylko liczby dodatnie oraz 0)
# n! = n×(n−1)×⋯×1
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Masz 5 różnych książek i chcesz je ustawić w różnej kolejności na półce.
# Ile różnych sposobów ustawienia tych książek istnieje?
#
# Odpowiedź to liczba permutacji, czyli ilość sposobów, w jakie można ustawić
# n elementów, a to właśnie wyraża silnia!


def silnia(n):
    # Przypadek bazowy: silnia z 0 to 1
    if n == 0:
        return 1
    # Rekurencyjnie obliczaj silnię
    else:
        return n * silnia(n - 1)

# Przykład użycia
print(silnia(5))  # Wynik: 120
