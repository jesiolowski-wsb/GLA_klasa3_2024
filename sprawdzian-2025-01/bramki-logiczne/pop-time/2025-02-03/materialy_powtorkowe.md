# Ćwiczenia z bramek logicznych

## Bramki podstawowe (poziom ⭐)

### Zadanie 1: Bramka AND
Napisz funkcję symulującą bramkę AND i przetestuj wszystkie kombinacje.

```python
# Oczekiwane działanie:
# False AND False = False
# False AND True = False
# True AND False = False
# True AND True = True

# Rozwiązanie:
def bramka_and(a, b):
    return a and b

# Test
print(f"False AND False = {bramka_and(False, False)}")
print(f"False AND True = {bramka_and(False, True)}")
print(f"True AND False = {bramka_and(True, False)}")
print(f"True AND True = {bramka_and(True, True)}")
```

### Zadanie 2: Bramka OR
Napisz funkcję symulującą bramkę OR.

```python
# Oczekiwane działanie:
# False OR False = False
# False OR True = True
# True OR False = True
# True OR True = True

# Rozwiązanie:
def bramka_or(a, b):
    return a or b

# Test
print(f"False OR False = {bramka_or(False, False)}")
print(f"False OR True = {bramka_or(False, True)}")
```

### Zadanie 3: Bramka NOT
Napisz funkcję odwracającą wartość logiczną.

```python
# Oczekiwane działanie:
# NOT False = True
# NOT True = False

# Rozwiązanie:
def bramka_not(a):
    return not a

# Test
print(f"NOT False = {bramka_not(False)}")
print(f"NOT True = {bramka_not(True)}")
```

## Wyświetlanie wyników (poziom ⭐)

### Zadanie 4: Prosta tabela prawdy
Napisz program wyświetlający tabelę prawdy dla jednej bramki.

```python
# Oczekiwany wynik:
# A     B     AND
# ---------------
# 0     0     0
# 0     1     0
# 1     0     0
# 1     1     1

# Rozwiązanie:
def pokaz_tabele_and():
    print("A     B     AND")
    print("-" * 15)
    for a in [False, True]:
        for b in [False, True]:
            print(f"{int(a):<5} {int(b):<5} {int(a and b)}")

pokaz_tabele_and()
```

## Bramki złożone (poziom ⭐⭐)

### Zadanie 5: Bramka NAND
Napisz funkcję symulującą bramkę NAND (NOT AND).

```python
# NAND to odwrotność AND
# Oczekiwane działanie:
# False NAND False = True
# False NAND True = True
# True NAND False = True
# True NAND True = False

# Rozwiązanie:
def bramka_nand(a, b):
    return not (a and b)

# Test
print(f"False NAND False = {bramka_nand(False, False)}")
print(f"True NAND True = {bramka_nand(True, True)}")
```

### Zadanie 6: Bramka XOR
Napisz funkcję symulującą bramkę XOR (eXclusive OR).

```python
# XOR zwraca True tylko gdy wejścia są różne
# Oczekiwane działanie:
# False XOR False = False
# False XOR True = True
# True XOR False = True
# True XOR True = False

# Rozwiązanie:
def bramka_xor(a, b):
    return (a or b) and not (a and b)

# Test
print(f"False XOR False = {bramka_xor(False, False)}")
print(f"False XOR True = {bramka_xor(False, True)}")
```

## Praktyczne zastosowania (poziom ⭐⭐)

### Zadanie 7: System kontroli dostępu
Napisz funkcję sprawdzającą, czy można otworzyć drzwi (potrzebna karta i kod PIN).

```python
# Drzwi otworzą się tylko gdy mamy kartę I znamy PIN
# Rozwiązanie:
def sprawdz_dostep(karta, pin):
    return karta and pin

# Test
print("Próba wejścia:")
print(f"Brak karty, zły PIN: {sprawdz_dostep(False, False)}")
print(f"Jest karta, dobry PIN: {sprawdz_dostep(True, True)}")
```

### Zadanie 8: System awaryjny
Napisz funkcję włączającą alarm gdy którykolwiek z czujników wykryje problem.

```python
# Alarm włącza się gdy czujnik dymu LUB temperatury wykryje zagrożenie
# Rozwiązanie:
def sprawdz_alarm(czujnik_dymu, czujnik_temp):
    return czujnik_dymu or czujnik_temp

# Test
print("Test systemu:")
print(f"Wykryto dym: {sprawdz_alarm(True, False)}")
print(f"Wszystko OK: {sprawdz_alarm(False, False)}")
```

### Zadanie 9: Wykrywanie błędów
Napisz funkcję sprawdzającą poprawność danych z dwóch czujników.

```python
# Błąd występuje gdy czujniki pokazują różne wartości
# Rozwiązanie:
def wykryj_blad(czujnik1, czujnik2):
    return czujnik1 != czujnik2  # to samo co XOR

# Test
print("Test czujników:")
print(f"Różne odczyty: {wykryj_blad(True, False)}")
print(f"Zgodne odczyty: {wykryj_blad(True, True)}")
```

## Wskazówki do zapamiętania:
- Bramka AND zwraca True tylko gdy oba wejścia są True
- Bramka OR zwraca True gdy przynajmniej jedno wejście jest True
- Bramka NOT odwraca wartość logiczną
- Bramka NAND to zaprzeczenie AND
- Bramka XOR zwraca True tylko gdy wejścia są różne
- Używaj `int()` do konwersji True/False na 1/0 w wyświetlaniu
- Wyrównuj kolumny w tabelach używając `print(f"{wartość:<5}")`