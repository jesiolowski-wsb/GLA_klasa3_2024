# Bramki logiczne - ćwiczenie wprowadzające (20 punktów)

## Wprowadzenie
Bramki logiczne to podstawowe elementy elektroniki cyfrowej. Działają na wartościach True (1) i False (0).
Zaimplementuj podstawowe bramki logiczne oraz przeprowadz ich testy.

## Zadanie 1: Podstawowe bramki (6 punktów)
Zaimplementuj funkcje dla trzech podstawowych bramek logicznych:
1. **AND** - zwraca True tylko gdy oba wejścia są True
2. **OR** - zwraca True gdy przynajmniej jedno wejście jest True
3. **NOT** - zwraca przeciwną wartość wejścia

```python
# Przykłady użycia:
print("Test bramki AND:")
print(f"AND(False, False) = {AND(False, False)}")  # False
print(f"AND(True, False) = {AND(True, False)}")    # False
print(f"AND(True, True) = {AND(True, True)}")      # True
```

## Zadanie 2: Tabela prawdy (6 punktów)
Napisz funkcję `wyswietl_tabele_prawdy()`, która pokaże działanie wszystkich zaimplementowanych bramek:

### Oczekiwany wynik:
```
a     b     AND    OR     NOT(a)
-----------------------------------
0     0     0      0      1
0     1     0      1      1
1     0     0      1      0
1     1     1      1      0
```

## Zadanie 3: Zaawansowana tabela prawdy (8 punktów)

Zaprojektuj i zaimplementuj funkcję COMPLEX, która symuluje działanie złożonej bramki logicznej zgodnie z poniższym opisem:

1. Funkcja `COMPLEX(a, b, c)` powinna przyjmować trzy wartości logiczne: `a`, `b`, `c`.
2. Bramka złożona działa według reguły `COMPLEX(a, b, c) = (a AND b) OR (NOT(c))`

Przetestuj działanie tej funkcji, wyświetlając tabelę prawdy dla wszystkich możliwych kombinacji wejść `a`, `b`, `c`

### Oczekiwany wynik:
```
a     b     c     COMPLEX(a,b,c)
------------------------------
0     0     0           1
0     0     1           0
0     1     0           1
0     1     1           0
1     0     0           1
1     0     1           0
1     1     0           1
1     1     1           1
```

## Kryteria oceny:
- Poprawna implementacja bramki AND (2 punkty)
- Poprawna implementacja bramki OR (2 punkty)
- Poprawna implementacja bramki NOT (2 punkty)
- Poprawne wyświetlanie tabeli prawdy (6 punktów)
- Poprawne wyświetlanie zaawansowanej tabeli prawdy (8 punktów)


## Podpowiedzi:
1. W Pythonie możesz używać operatorów `and`, `or` i `not`
2. Do konwersji bool na int użyj `int(wartość_logiczna)`
3. Parametr `end=""` w funkcji print() zapobiega przejściu do nowej linii
4. Do stworzenia tabelki w czytelnej formie możesz użyć wyrównań tekstu - wyciągnij odpowiednie wnioski z poniższego
```python
zmienna = "tekst"
print(f"{zmienna:15} inny_tekst")
print(f"{zmienna:<15} inny_tekst")
print(f"{zmienna:>15} inny_tekst")
print(f"{zmienna:^15} inny_tekst")
```

Powodzenia!
