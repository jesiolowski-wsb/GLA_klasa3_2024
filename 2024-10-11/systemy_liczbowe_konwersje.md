
# Zadania dotyczące konwersji systemów liczbowych w Pythonie

## Zadanie 1: Konwersja z systemu dziesiętnego na binarny

### Wersja z użyciem wbudowanej funkcji:
```python
def dziesietny_na_binarny(liczba):
    return bin(liczba)[2:]  # [2:] usuwa prefiks '0b'

# Przykład
liczba = 25
print(dziesietny_na_binarny(liczba))  # Wyjście: 11001
```

### Wersja bez wbudowanych funkcji:
```python
def dziesietny_na_binarny_manualnie(liczba):
    wynik = ''
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba //= 2
    return wynik

# Przykład
liczba = 25
print(dziesietny_na_binarny_manualnie(liczba))  # Wyjście: 11001
```

---

## Zadanie 2: Konwersja z systemu binarnego na dziesiętny

### Wersja z użyciem wbudowanej funkcji:
```python
def binarny_na_dziesietny(bin_str):
    return int(bin_str, 2)

# Przykład
bin_str = '1010'
print(binarny_na_dziesietny(bin_str))  # Wyjście: 10
```

### Wersja bez wbudowanych funkcji:
```python
def binarny_na_dziesietny_manualnie(bin_str):
    wynik = 0
    potega = 0
    for cyfra in reversed(bin_str):
        wynik += int(cyfra) * (2 ** potega)
        potega += 1
    return wynik

# Przykład
bin_str = '1010'
print(binarny_na_dziesietny_manualnie(bin_str))  # Wyjście: 10
```

---

## Zadanie 3: Konwersja z systemu dziesiętnego na szesnastkowy

### Wersja z użyciem wbudowanej funkcji:
```python
def dziesietny_na_szesnastkowy(liczba):
    return hex(liczba)[2:].upper()  # [2:] usuwa prefiks '0x'

# Przykład
liczba = 255
print(dziesietny_na_szesnastkowy(liczba))  # Wyjście: FF
```

### Wersja bez wbudowanych funkcji:
```python
def dziesietny_na_szesnastkowy_manualnie(liczba):
    cyfry = '0123456789ABCDEF'
    wynik = ''
    while liczba > 0:
        wynik = cyfry[liczba % 16] + wynik
        liczba //= 16
    return wynik

# Przykład
liczba = 255
print(dziesietny_na_szesnastkowy_manualnie(liczba))  # Wyjście: FF
```

---

## Zadanie 4: Konwersja z systemu szesnastkowego na dziesiętny

### Wersja z użyciem wbudowanej funkcji:
```python
def szesnastkowy_na_dziesietny(hex_str):
    return int(hex_str, 16)

# Przykład
hex_str = 'A1'
print(szesnastkowy_na_dziesietny(hex_str))  # Wyjście: 161
```

### Wersja bez wbudowanych funkcji:
```python
def szesnastkowy_na_dziesietny_manualnie(hex_str):
    cyfry = '0123456789ABCDEF'
    wynik = 0
    potega = 0
    for cyfra in reversed(hex_str.upper()):
        wynik += cyfry.index(cyfra) * (16 ** potega)
        potega += 1
    return wynik

# Przykład
hex_str = 'A1'
print(szesnastkowy_na_dziesietny_manualnie(hex_str))  # Wyjście: 161
```

---

## Zadanie 5: Konwersja z systemu dziesiętnego na system ósemkowy

### Wersja z użyciem wbudowanej funkcji:
```python
def dziesietny_na_osemkowy(liczba):
    return oct(liczba)[2:]  # [2:] usuwa prefiks '0o'

# Przykład
liczba = 100
print(dziesietny_na_osemkowy(liczba))  # Wyjście: 144
```

### Wersja bez wbudowanych funkcji:
```python
def dziesietny_na_osemkowy_manualnie(liczba):
    wynik = ''
    while liczba > 0:
        wynik = str(liczba % 8) + wynik
        liczba //= 8
    return wynik

# Przykład
liczba = 100
print(dziesietny_na_osemkowy_manualnie(liczba))  # Wyjście: 144
```
