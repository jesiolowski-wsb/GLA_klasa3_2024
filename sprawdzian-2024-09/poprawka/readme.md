# Sprawdzian poprawkowy z rekurencji i podstaw algorytmów

## Zadanie 1: Zliczanie samogłosek (3 punkty)

Napisz program, który w tekście poniżej zlicza liczbę wystąpień samogłosek (tj. **a, e, i, o, u**) oraz wyświetla wynik.

tekst to przetestowania:
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Rozwiązanie:

```python
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
samogloski = "aeiou"
liczba_samoglosek = 0

for litera in tekst:
    if litera.lower() in samogloski:
        liczba_samoglosek += 1

print("Liczba samogłosek:", liczba_samoglosek)
```

---

## Zadanie 2: Rysowanie prostokąta (5 punktów)

Napisz program, który:

- Pobiera od użytkownika szerokość i wysokość prostokąta.
- Rysuje prostokąt z gwiazdek (`*`), ALE w przypadku nieparzystej wartości zmiennej `szerokość`, w centralnej kolumnie zamiast gwiazdek umieszcza znak myślnika (`-`).

> [!TIP] 
> Przemyśl po czym można poznać czy jesteśmy na elemencie centralnym zbioru danych

### Rozwiązanie:

```python
szerokosc = int(input("Podaj szerokość prostokąta: "))
wysokosc = int(input("Podaj wysokość prostokąta: "))

for i in range(wysokosc):
    wiersz = ""
    for j in range(szerokosc):
        if szerokosc % 2 == 1 and j == szerokosc // 2:
            wiersz += "-"
        else:
            wiersz += "*"
    print(wiersz)
```

---

## Zadanie 3: Rekurencyjne potęgowanie (5 punktów)

Napisz funkcję rekurencyjną `potega(podstawa, wykladnik)`, która oblicza wynik potęgowania `podstawa` do potęgi `wykladnik`. Załóż, że wykładnik jest liczbą nieujemną.

### Rozwiązanie:

```python
def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    elif wykladnik == 1:
        return podstawa
    else:
        return podstawa * potega(podstawa, wykladnik - 1)

# Przykłady użycia:
print(potega(2, 3))  # Powinno zwrócić 8
print(potega(5, 2))  # Powinno zwrócić 25
print(potega(3, 0))  # Powinno zwrócić 1
```

---

## Zadanie 4: Generator i Analizator Haseł (7 punktów)

Napisz program, który będzie generował losowe hasła i oceniał ich siłę. Program powinien składać się z dwóch głównych funkcji:

1. `generuj_haslo(dlugosc)`: 
   - Funkcja ta powinna generować losowe hasło o podanej długości.
   - Hasło powinno zawierać małe i wielkie litery, cyfry oraz znaki specjalne.

2. `sprawdz_sile_hasla(haslo)`: 
   - Funkcja ta powinna oceniać siłę hasła, przyznając punkty za spełnienie różnych kryteriów.
   - Kryteria to długość hasła, oraz obecność różnych typów znaków (szczegóły poniżej)

### Główna część programu powinna:

- Poprosić użytkownika o podanie długości hasła.
- Wygenerować hasło o podanej długości.
- Sprawdzić siłę wygenerowanego hasła.
- Wyświetlić wygenerowane hasło i jego ocenę siły.

### Wskazówki:

- Użyj modułu `random` do generowania losowych znaków.
```python
import random
print(random.choice("asd")) # zwróci a, s lub d
```
- W funkcji `sprawdz_sile_hasla()`, przyznawaj po jednym punkcie za:
  - Długość hasła (1 punkt, jeśli długość >= 8)
  - Obecność małych liter (np poprzez użycie `.islower()`)
  - Obecność wielkich liter (np poprzez użycie `.isupper()`)
  - Obecność cyfr (np poprzez użycie `.isdigit()`)
  - Obecność znaków specjalnych (element listy - wybierz w oparciu o dane wejściowe do `random`)
- Możesz użyć pętli `for` do przejścia przez wszystkie znaki w haśle.
- Użyj prostych instrukcji warunkowych `if` do sprawdzenia typów znaków.

### Przykładowe użycie:

```python
dlugosc_hasla = int(input("Podaj długość hasła: "))     # 7
wygenerowane_haslo = generuj_haslo(dlugosc_hasla)       # Hge8jwa
sila_hasla = sprawdz_sile_hasla(wygenerowane_haslo)     # 3 (mała litera, duża litera, cyfra)

print(f"Wygenerowane hasło: {wygenerowane_haslo}")
print(f"Siła hasła (1-5): {sila_hasla}")
```

### Rozwiązanie

```python
import random

def generuj_haslo(dlugosc):
    znaki = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    haslo = ""
    for _ in range(dlugosc):
        haslo += random.choice(znaki)
    return haslo

def sprawdz_sile_hasla(haslo):
    wynik = 0
    if len(haslo) >= 8:
        wynik += 1
    
    ma_mala_litere = False
    ma_duza_litere = False
    ma_cyfre = False
    ma_znak_specjalny = False
    
    for znak in haslo:
        if znak.islower():
            ma_mala_litere = True
        elif znak.isupper():
            ma_duza_litere = True
        elif znak.isdigit():
            ma_cyfre = True
        elif znak in "!@#$%^&*":
            ma_znak_specjalny = True
    
    if ma_mala_litere:
        wynik += 1
    if ma_duza_litere:
        wynik += 1
    if ma_cyfre:
        wynik += 1
    if ma_znak_specjalny:
        wynik += 1
    
    return wynik

dlugosc_hasla = int(input("Podaj długość hasła: "))
wygenerowane_haslo = generuj_haslo(dlugosc_hasla)
sila_hasla = sprawdz_sile_hasla(wygenerowane_haslo)

print(f"Wygenerowane hasło: {wygenerowane_haslo}")
print(f"Siła hasła (1-5): {sila_hasla}")

```


```python
# alternatywne rozwiązanie 
def sprawdz_sile_hasla(haslo):
    wynik = 0
    if len(haslo) >= 8:
        wynik += 1
    if any(c.islower() for c in haslo):
        wynik += 1
    if any(c.isupper() for c in haslo):
        wynik += 1
    if any(c.isdigit() for c in haslo):
        wynik += 1
    if any(c in "!@#$%^&*" for c in haslo):
        wynik += 1
    return wynik
```

Powodzenia!
