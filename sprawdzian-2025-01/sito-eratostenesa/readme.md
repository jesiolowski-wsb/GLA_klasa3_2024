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
