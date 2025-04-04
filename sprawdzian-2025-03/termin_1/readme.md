# Sprawdzian z podstaw programowania i algorytmów w Pythonie
**Czas: 60 minut**  
**Maksymalna liczba punktów: 22**

> [!NOTE]
> - Dla każdego rozwiązania poproszę osobny plik, tj struktura odpowiedzi powinna wyglądać tak:
> ```
> \sprawdzian-2025-03\
>                   \nazwisko-imie\
>                                 \zad1.py
>                                 \zad2.py
>                                 \zad3.py
>                                 \zad4.py
> ```
> - Oceniane będą: poprawność działania, styl kodu oraz efektywność rozwiązania

## Zadanie 1: Analiza tekstu z szyfrem (6 punktów)

Plik `tajny_przekaz.txt` zawiera linie tekstu. Każda linia zawiera jedno słowo składające się z małych i wielkich liter alfabetu angielskiego. Napisz program, który wykona następujące operacje:

1. Wczyta zawartość pliku
2. Znajdzie i wypisze słowo, które zawiera największą liczbę wielkich liter. Jeśli wynikiem będzie więcej niż jedno słowo, wypisz tylko pierwsze z nich
3. Wypisze tajną wiadomość, która powstanie z połączenia 5. litery co 10. słowa (zaczynając od 10. słowa - pamiętaj o indeksach w tablicy i liczeniu od 0)
4. Zapisze wyniki do pliku `wyniki1.txt`

### Oczekiwane rozwiązanie:
```
Zadanie 1.1:
UvWxY (3 wielkie litery)

Zadanie 1.2:
LAMPKA
```

Uwaga: Zakładamy, że każde słowo występujące co 10 pozycji ma co najmniej 5 liter.

## Zadanie 2: Algorytm wydawania reszty (5 punktów)

Napisz funkcję `wydaj_reszte(kwota, nominaly)`, która:

1. Przyjmuje kwotę do wydania oraz listę dostępnych nominałów
2. Implementuje algorytm zachłanny wydawania reszty
3. Zwraca słownik, gdzie kluczem jest nominał, a wartością liczba użytych monet
4. Dodatkowo sprawdza, czy wydanie reszty jest możliwe (jeśli najmniejszy nominał nie jest 1)

Twoja funkcja powinna działać według następujących kroków:
- Posortuj dostępne nominały od największego do najmniejszego
- Wybieraj największy nominał, który nie przekracza pozostałej do wydania kwoty
- Powtarzaj, aż cała kwota zostanie wydana lub nie można już wydać więcej

```python
# Przykład użycia:
nominaly = [1, 5, 10, 25, 100]
wynik = wydaj_reszte(142, nominaly)
# Oczekiwany wynik: 
# {100: 1, 25: 1, 10: 1, 5: 1, 1: 2}

# Przykład gdy nie można wydać reszty
nominaly2 = [5, 10, 25]
wynik2 = wydaj_reszte(8, nominaly2)
# Oczekiwany wynik: 
# Nie można wydać reszty 8 przy użyciu podanych nominałów.


```

## Zadanie 3: Poruszanie się pionka na planszy (6 punktów)

Mamy planszę o wymiarach 5x5, reprezentowaną jako tablica dwuwymiarowa. Wartość `0` oznacza puste pole, wartość `1` oznacza przeszkodę. Pionek może poruszać się tylko po pustych polach.

Napisz funkcję `sprawdz_ruch(plansza, start_x, start_y, cel_x, cel_y)`, która:

1. Sprawdza czy z punktu startowego (start_x, start_y) można dotrzeć do punktu docelowego (cel_x, cel_y) wykonując dokładnie **jeden ruch**
2. Pionek może poruszać się tylko o jedno pole w kierunkach: góra, dół, lewo, prawo (nie na ukos)
3. Funkcja zwraca wartość logiczną: True, jeśli ruch jest możliwy, False w przeciwnym wypadku

```python
# Przykład planszy:
plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Przykład użycia:
print(sprawdz_ruch(plansza, 0, 0, 0, 1))  # True - można się poruszyć w prawo
print(sprawdz_ruch(plansza, 0, 0, 1, 0))  # True - można się poruszyć w dół
print(sprawdz_ruch(plansza, 0, 0, 0, 2))  # False - pole (0,2) to przeszkoda
print(sprawdz_ruch(plansza, 0, 0, 1, 1))  # False - ruch na ukos jest niedozwolony
```

Wymagane sprawdzenia to:
- czy wpółrzędne są w granicach planszy
- czy punkt startowy i docelowy to puste pola
- czy ruch jest dozwolony (tylko o jedno pole w kierunku góra, dół, lewo, prawo)

## Zadanie 4: Systemy liczbowe i statystyki (5 punktów)

Plik `liczby.txt` zawiera 100 liczb całkowitych (po jednej w wierszu). Napisz program, który:

1. Wczyta wszystkie liczby z pliku
2. Dla każdej liczby określi i zapisze jej reprezentację:
   - w systemie binarnym
   - w systemie szesnastkowym (hex)
3. Obliczy i wypisze następujące statystyki:
   - średnią wartość wszystkich liczb
   - medianę (wartość środkową po posortowaniu)
   - liczbę wystąpień każdej cyfry w zapisie dziesiętnym wszystkich liczb

Wyniki zapisz do pliku `wyniki_liczby.txt`.

### Przykład:
Dla liczb [120, 255, 10]:
```
Zadanie 4.1:
120 -> binarnie: 1111000, hex: 78
255 -> binarnie: 11111111, hex: FF
10 -> binarnie: 1010, hex: A

Zadanie 4.2:
Średnia: 128.33
Mediana: 120
Statystyki cyfr:
0: 2
1: 4
2: 1
5: 2
```

## Powodzenia!
