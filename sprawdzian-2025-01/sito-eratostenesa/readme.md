## Materiały powtórkowe do sprawdzianu z sita Eratostenesa:

### Zadanie 1: Tabliczka mnożenia
Napisz program, który wyświetla tabliczkę mnożenia dla liczb od 1 do 10.
Wyjście programu powinno wyglądać jak poniżej (wyrównanie nie jest wymagane):

```
1  2   3   4   5   6   7   8   9   10
2  4   6   8   10  12  14  16  18  20
3  6   9   12  15  18  21  24  27  30
...
10 20  30  40  50  60  70  80  90  100
```

#### Rozwiązanie:
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
```

### Zadanie 2: Wzór z gwiazdek
Napisz program, który rysuje prostokąt z gwiazdek. Wymiary prostokąta (liczba wierszy i kolumn) wprowadza użytkownik.
Przykład dla wierszy = 4 i kolumn = 6:

```
******
******
******
******
```

#### Rozwiązanie:
```python
wiersze = int(input("Podaj liczbę wierszy: "))
kolumny = int(input("Podaj liczbę kolumn: "))

for i in range(wiersze):
    for j in range(kolumny):
        print("*", end="")  # Nie przechodzimy do nowej linii po każdej gwiazdce
    print()  # Przejście do nowej linii po każdej iteracji wiersza
```

### Zadanie 3: Liczby pierwsze w prostokącie
Napisz program, który wypisuje prostokąt z liczb, gdzie każda liczba to suma wiersza i kolumny.
Przykład dla wierszy = 4 i kolumn = 5:

```
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
```

Ulepsz program, aby otoczył liczby pierwsze nawiasami kwadratowymi.

```
0  1  [2] [3] 4
1  [2] [3] 4  [5]
[2] [3] 4  [5] 6
[3] 4  [5] 6  7
```

#### Rozwiązanie:
```python
# Funkcja sprawdzająca, czy liczba jest pierwsza
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
    # for i in range(2, n + 1):
        if n % i == 0:
            return False
    return True

# Prostokąt liczb
wiersze = int(input("Podaj liczbę wierszy: "))
kolumny = int(input("Podaj liczbę kolumn: "))

for i in range(wiersze):
    for j in range(kolumny):
        liczba = i + j
        if czy_pierwsza(liczba):
            print(f"[{liczba}]", end=" ")  # Liczby pierwsze w nawiasach
        else:
            print(f" {liczba} ", end=" ")  # Pozostałe liczby
    print()  # Przejście do nowej linii po każdym wierszu

```
