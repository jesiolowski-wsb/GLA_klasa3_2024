# POP-time Sprawdzianu z podstawowych algorytmów w Pythonie (tak, naprawdę :) )
**Czas: 60 minut**  
**Maksymalna liczba punktów: 22**


## Zadanie 1: Sito Eratostenesa (6 punktów)

Zaimplementuj funkcję `znajdz_pierwsze(n)`, która za pomocą algorytmu Sita Eratostenesa znajdzie wszystkie liczby pierwsze nie większe od n.

### Opis działania Sita Eratostenesa:
1. Utwórz tablicę wartości logicznych od 0 do n, zainicjalizowaną wartościami True
2. Oznacz 0 i 1 jako False (nie są liczbami pierwszymi)
3. Dla każdej liczby i od 2 do sqrt(n):
   - Jeśli sito[i] == True (liczba jest pierwsza)
   - Oznacz wszystkie wielokrotności i jako False, zaczynając od i*i

### Funkcja powinna:
- Zwracać listę liczb pierwszych ≤ n
- Działać z optymalną złożonością czasową

> [!TIP]
> Zauważ, że wystarczy sprawdzać liczby do pierwiastka z n, oraz że wykreślanie wielokrotności możesz zacząć od `i*i`, a nie od `i*2`.

```python
# Testy
print(znajdz_pierwsze(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(znajdz_pierwsze(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## Zadanie 2: NWD i NWW (5 punktów)

Zaimplementuj dwie funkcje:

1. `nwd(a, b)` - obliczającą Największy Wspólny Dzielnik dwóch liczb metodą Euklidesa
2. `nww(a, b)` - obliczającą Najmniejszą Wspólną Wielokrotność dwóch liczb

### Metoda Euklidesa (NWD):
Jeśli a i b są liczbami całkowitymi dodatnimi, to `NWD(a, b) = NWD(b, a % b)`.
Warunkiem zakończenia rekurencji jest osiągnięcie `b = 0`, wtedy `NWD(a, 0) = a`.

### Najmniejsza Wspólna Wielokrotność (NWW):
NWW można obliczyć według wzoru: `NWW(a, b) = (a * b) / NWD(a, b)`

### Przykłady:
```python
print(nwd(12, 18))  # 6
print(nwd(35, 14))  # 7
print(nwd(13, 7))   # 1

print(nww(12, 18))  # 36
print(nww(6, 8))    # 24
print(nww(7, 13))   # 91
```

> [!TIP]
> - Pamiętaj o obsłudze przypadków brzegowych (np. gdy jedna z liczb jest zerem)
> - Uważaj na potencjalne przepełnienia przy obliczaniu NWW

---

## Zadanie 3: Generator liczb Fibonacciego (6 punktów)

Zaimplementuj dwie wersje funkcji generującej n pierwszych wyrazów ciągu Fibonacciego:

1. `fib_rekurencyjnie(n)` - wersja rekurencyjna
2. `fib_iteracyjnie(n)` - wersja iteracyjna

### Definicja ciągu Fibonacciego:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) dla n > 1

### Wymagania:
- Każda funkcja powinna zwracać listę n pierwszych wyrazów ciągu
- W rozwiązaniu rekurencyjnym zastosuj optymalizację za pomocą zapamiętywania już obliczonych wartości (można użyć słownika)
- W rozwiązaniu iteracyjnym użyj tylko stałej ilości zmiennych pomocniczych

### Przykład:
```python
print(fib_rekurencyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib_iteracyjnie(10))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

> [!TIP]
> - Prosta implementacja rekurencyjna ma złożoność wykładniczą - zastosuj technikę zapamiętywania już obliczonych wartości, aby uniknąć ponownego obliczania tych samych elementów
> - W wersji iteracyjnej wystarczą dwie zmienne do przechowywania poprzednich wartości

---

## Zadanie 4: Operacje na ułamkach (5 punktów)

Korzystając z funkcji NWD, zaimplementuj kalkulator operacji na ułamkach zwykłych. Napisz funkcje:

1. `skroc_ulamek(licznik, mianownik)` - skraca ułamek do nieskracalnej postaci
2. `dodaj_ulamki(l1, m1, l2, m2)` - dodaje dwa ułamki l1/m1 + l2/m2
3. `odejmij_ulamki(l1, m1, l2, m2)` - odejmuje ułamek l2/m2 od l1/m1

### Wymagania:
- Funkcje powinny korzystać z wcześniej zaimplementowanej funkcji NWD
- Każda funkcja zwraca wynik w postaci krotki (licznik, mianownik)
- Wynik powinien być zawsze w postaci nieskracalnej
- Obsłuż przypadki specjalne (np. ujemne liczniki/mianowniki)

### Przykład:
```python
print(skroc_ulamek(12, 18))         # (2, 3)
print(dodaj_ulamki(1, 2, 1, 3))     # (5, 6)
print(odejmij_ulamki(3, 4, 1, 2))   # (1, 4)
```

> [!TIP]
> - Przy dodawaniu/odejmowaniu ułamków o różnych mianownikach, użyj NWW do znalezienia wspólnego mianownika
> - Pamiętaj, że ułamek w postaci kanonicznej ma mianownik dodatni
> - Sprawdź przypadki brzegowe, np. jak obsłużyć dzielenie przez 0


---

Powodzenia!
