# Algorytm Euklidesa, NWD i NWW 

## Spis treści
- [Zadanie 1: Implementacja Algorytmu Euklidesa](#zadanie-1-implementacja-algorytmu-euklidesa)
- [Zadanie 2: Najmniejsza Wspólna Wielokrotność](#zadanie-2-najmniejsza-wspólna-wielokrotność)
- [Zadanie 3: Operacje na Ułamkach](#zadanie-3-operacje-na-ułamkach)
- [Zadanie 4: Kalkulator Ułamków](#zadanie-4-kalkulator-ułamków)

## Zadanie 1: Implementacja Algorytmu Euklidesa
Zaimplementuj algorytm Euklidesa do znajdowania Największego Wspólnego Dzielnika (NWD) dwóch liczb całkowitych.

> [!TIP]
> Podstawowa zasada algorytmu Euklidesa to:
> 
> Jeśli mamy dwie liczby a i b (gdzie a ≥ b > 0), to `NWD(a, b) = NWD(b, a mod b)`. 
> Proces kontynuujemy rekurencyjnie, aż otrzymamy resztę równą 0.
> Ostatnia niezerowa reszta jest szukanym NWD

### Zadanie 1.1: Wersja Iteracyjna
Napisz funkcję `nwd_iteracyjny(a, b)`, która:
- Znajduje NWD liczb a i b metodą iteracyjną
- Obsługuje poprawnie liczby ujemne
- Zwraca wynik jako liczbę nieujemną

### Zadanie 1.2: Wersja Rekurencyjna
Napisz funkcję `nwd_rekurencyjny(a, b)`, która:
- Znajduje NWD liczb a i b metodą rekurencyjną
- Obsługuje poprawnie liczby ujemne
- Zwraca wynik jako liczbę nieujemną

### Przypadki testowe dla Zadania 1:

| Para liczb | Oczekiwany NWD |
|------------|----------------|
| 48, 18     | 6              |
| 125, 75    | 25             |
| 0, 5       | 5              |
| -48, 18    | 6              |

> [!NOTE]
> #### Kroki obliczeń dla NWD(48, 18):
>
> **Iteracyjnie:**
> 1. a=48, b=18
> 2. a=18, b=48%18=12
> 3. a=12, b=18%12=6
> 4. a=6, b=12%6=0
> 5. Wynik: 6
>
> **Rekurencyjnie:**
> 1. nwd(48, 18) → nwd(18, 48%18) = nwd(18, 12)
> 2. nwd(18, 12) → nwd(12, 18%12) = nwd(12, 6)
> 3. nwd(12, 6) → nwd(6, 12%6) = nwd(6, 0)
> 4. nwd(6, 0) → return 6

## Zadanie 2: Najmniejsza Wspólna Wielokrotność
Zaimplementuj funkcję do znajdowania Najmniejszej Wspólnej Wielokrotności (NWW) dwóch liczb całkowitych.

> [!TIP]
> NWW to **najmniejsza** liczba dodatnia, która jest wielokrotnością podanych liczb. Na przykład NWW(4, 6) = 12, ponieważ 12 jest najmniejszą liczbą, która jest jednocześnie podzielna przez 4 i przez 6.

### Zadanie 2.1: Implementacja NWW
Napisz funkcję `nww(a, b)`, która:
- Oblicza NWW liczb a i b, wykorzystując zaimplementowany wcześniej algorytm NWD
- Obsługuje poprawnie przypadki szczególne (np. gdy jedna z liczb jest równa 0)
- Zwraca wynik jako liczbę nieujemną

### Przypadki testowe dla Zadania 2:

| Para liczb | NWD   | Oczekiwane NWW |
|------------|-------|----------------|
| 48, 18     | 6     | 144            |
| 12, 8      | 4     | 24             |
| 7, 13      | 1     | 91             |
| 0, 5       | 5     | 0              |

#### Sprawdzenie dla NWW(48, 18):
- NWD(48, 18) = 6
- NWW(48, 18) = (48 * 18) / 6 = 864 / 6 = 144


## Zadanie 3: Operacje na Ułamkach
Zaimplementuj funkcje do wykonywania podstawowych operacji arytmetycznych na ułamkach, wykorzystując NWD i NWW.

### Zadanie 3.1: Skracanie Ułamków
Napisz funkcję `skroc_ulamek(licznik, mianownik)`, która:
- Skraca ułamek poprzez dzielenie licznika i mianownika przez ich NWD
- Obsługuje poprawnie ułamki ujemne (znak powinien być przy liczniku)
- Zwraca krotkę (licznik, mianownik), gdzie mianownik jest zawsze dodatni

### Zadanie 3.2: Dodawanie Ułamków
Napisz funkcję `dodaj_ulamki(l1, m1, l2, m2)`, która:
- Dodaje dwa ułamki l1/m1 i l2/m2
- Wykorzystuje NWW do znalezienia wspólnego mianownika
- Skraca wynik do postaci nieskracalnej
- Zwraca krotkę (licznik, mianownik) wyniku

### Zadanie 3.3: Odejmowanie Ułamków
Napisz funkcję `odejmij_ulamki(l1, m1, l2, m2)`, która:
- Odejmuje ułamek l2/m2 od ułamka l1/m1
- Wykorzystuje funkcję dodawania (możesz sprowadzić odejmowanie do dodawania)
- Zwraca krotkę (licznik, mianownik) wyniku w postaci nieskracalnej

### Zadanie 3.4: Mnożenie Ułamków
Napisz funkcję `pomnoz_ulamki(l1, m1, l2, m2)`, która:
- Mnoży dwa ułamki l1/m1 i l2/m2
- Skraca wynik do postaci nieskracalnej
- Zwraca krotkę (licznik, mianownik) wyniku

### Zadanie 3.5: Dzielenie Ułamków
Napisz funkcję `podziel_ulamki(l1, m1, l2, m2)`, która:
- Dzieli ułamek l1/m1 przez ułamek l2/m2
- Wykorzystuje funkcję mnożenia (dzielenie to mnożenie przez odwrotność)
- Obsługuje poprawnie przypadki szczególne (np. dzielenie przez 0)
- Zwraca krotkę (licznik, mianownik) wyniku w postaci nieskracalnej

### Przypadki testowe dla Zadania 3:

#### 3.1 Skracanie ułamków:

| Ułamek | Skrócony ułamek |
|--------|-----------------|
| 24/36  | 2/3             |
| -8/12  | -2/3            |
| 0/5    | 0/1             |

#### 3.2 Dodawanie ułamków:

| Ułamek 1 | Ułamek 2 | Suma     |
|----------|----------|----------|
| 1/4      | 2/3      | 11/12    |
| 1/2      | 3/4      | 5/4      |

#### 3.3 Odejmowanie ułamków:

| Ułamek 1 | Ułamek 2 | Różnica  |
|----------|----------|----------|
| 3/4      | 1/4      | 1/2      |
| 1/2      | 3/4      | -1/4     |

#### 3.4 Mnożenie ułamków:

| Ułamek 1 | Ułamek 2 | Iloczyn  |
|----------|----------|----------|
| 2/3      | 3/4      | 1/2      |
| -2/3     | -5/6     | 5/9      |

#### 3.5 Dzielenie ułamków:

| Ułamek 1 | Ułamek 2 | Iloraz   |
|----------|----------|----------|
| 2/3      | 3/4      | 8/9      |
| 3/4      | 1/2      | 3/2      |

## Zadanie 4: Kalkulator Ułamków
Napisz program "Kalkulator Ułamków", który:
- Pozwala użytkownikowi na wprowadzenie dwóch ułamków (licznik i mianownik dla każdego)
- Wyświetla menu z dostępnymi operacjami (dodawanie, odejmowanie, mnożenie, dzielenie, skracanie)
- Wykonuje wybraną operację i wyświetla wynik
- Obsługuje podstawowe błędy (np. dzielenie przez zero)

### Przykładowy scenariusz użycia:
1. Wprowadź pierwszy ułamek: 3/4
2. Wprowadź drugi ułamek: 1/2
3. Wybierz operację:
   - Dodawanie: 3/4 + 1/2 = 5/4 = 1 1/4
   - Odejmowanie: 3/4 - 1/2 = 1/4
   - Mnożenie: 3/4 * 1/2 = 3/8
   - Dzielenie: 3/4 ÷ 1/2 = 3/2 = 1 1/2
   - Skracanie: pierwszy ułamek: 3/4 (już w postaci nieskracalnej)
                drugi ułamek: 1/2 (już w postaci nieskracalnej)
