# Sprawdzian uzupełniający z podstaw programowania i podstaw obsługi plików 
**Maksymalna liczba punktów: 22**

> [!NOTE]
> - Dla każdego rozwiązania poproszę osobny plik, tj struktura odpowiedzi powinna wyglądać tak:
> ```
> \sprawdzian-uzupelniajacy\
>                          \imie-nazwisko\
>                                        \zad1.py
>                                        \zad2.py
>                                        \zad3.py
>                                        \zad4.py
> ```
> - Oceniane będą: poprawność działania, styl kodu oraz efektywność rozwiązania

## Zadanie 1: Prosty kalkulator (6 punktów)
Napisz program, który:
1. Wczyta od użytkownika działanie matematyczne w formacie: `liczba1 operator liczba2` (np. `5 + 3`)
2. Obsłuży podstawowe operacje: `+` (dodawanie) i `*` (mnożenie)
3. Wyświetli wynik działania
4. Program kończy działanie gdy użytkownik wpisze `koniec`

Przykład działania:
```
> 2 + 3
Wynik: 5
> 4 * 5
Wynik: 20
> koniec
Do widzenia!
```

## Zadanie 2: Wizualizator cyfr (5 punktów)
Napisz program rysujący prostokąty z gwiazdek (*) o wymiarach odpowiadających podanej cyfrze.
Przykład: dla cyfry 3, program powinien narysować prostokąt 3x3:
```python
rysuj_cyfre(3)
```
Wynik:
```
***
***
***
```

## Zadanie 3: Lista parzysta/nieparzysta (5 punktów)
Napisz program, który:
1. Wczyta plik `liczby.txt` zawierający liczby (jedna w linii)
2. Zapisze do pliku `wyniki.txt` informację przy każdej liczbie czy jest parzysta czy nie

Przykładowa zawartość pliku `liczby.txt`:
```
4
7
2
9
```

Oczekiwana zawartość pliku `wyniki.txt`:
```
4 - parzysta
7 - nieparzysta
2 - parzysta
9 - nieparzysta
```

## Zadanie 4: Konwerter liczb (6 punktów)
Napisz program, który:
1. Wczyta z pliku `dane.txt` liczby dziesiętne (jedna w linii)
2. Przekonwertuje je na system binarny (możesz użyć wbudowanej funkcji `bin()`)
3. Zapisze wyniki do `bin.txt` w formacie: `[DEC] = [BIN]`

Przykładowa zawartość pliku `dane.txt`:
```
4
7
12
```

Oczekiwana zawartość pliku `bin.txt`:
```
4 = 100
7 = 111
12 = 1100
```

---

Powodzenia!