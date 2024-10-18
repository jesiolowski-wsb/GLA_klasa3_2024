# Sprawdzian poprawkowy z rekurencji i podstaw algorytmów

## Zadanie 1: Zliczanie samogłosek (4 punkty)

Napisz program, który w tekście poniżej zlicza liczbę wystąpień samogłosek (tj. **a, e, i, o, u**) oraz wyświetla wynik.

tekst to przetestowania:
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

---

## Zadanie 2: Rysowanie prostokąta (5 punktów)

Napisz program, który:

- Pobiera od użytkownika szerokość i wysokość prostokąta.
- Rysuje prostokąt z gwiazdek (`*`), ALE w przypadku nieparzystej wartości zmiennej `szerokość`, w centralnej kolumnie zamiast gwiazdek umieszcza znak myślnika (`-`).

> [!TIP] 
> Przemyśl po czym można poznać czy jesteśmy na elemencie centralnym zbioru danych

---

## Zadanie 3: Rekurencyjne potęgowanie (5 punktów)

Napisz funkcję rekurencyjną `potega(podstawa, wykladnik)`, która oblicza wynik potęgowania `podstawa` do potęgi `wykladnik`. Załóż, że wykładnik jest liczbą nieujemną.


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

Powodzenia!
