.# [POP-time] Poprawka sprawdzianu - Sito Eratostenesa (20 punktów)
**Czas: 45 minut**

## Wprowadzenie
Twoim zadaniem jest zaimplementowanie ulepszonej wersji Sita Eratostenesa i przeanalizowanie jego działania na różnych zbiorach danych.

## Zadanie 1: Implementacja podstawowa (8 punktów)
Zaimplementuj funkcję `znajdz_pierwsze(n)`, która:
1. Tworzy tablicę wartości logicznych dla liczb od 0 do n
2. Znajduje wszystkie liczby pierwsze metodą Sita Eratostenesa
3. Zlicza znalezione liczby pierwsze
4. Zwraca krotkę: (liczby_pierwsze, ile_znaleziono)

```python
# Przykład użycia:
pierwsze, ile = znajdz_pierwsze(20)
print(f"Znaleziono {ile} liczb pierwszych: {pierwsze}")
# Powinno zwrócić np.: "Znaleziono 8 liczb pierwszych: [2, 3, 5, 7, 11, 13, 17, 19]"
```

### Rozwiązanie:
```python
def znajdz_pierwsze(n):
    # Tworzymy tablicę wartości logicznych
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False
    
    # Lista na znalezione liczby pierwsze
    pierwsze = []
    
    # Główna pętla sita
    for i in range(2, int(n ** 0.5) + 1):
        if sito[i]:
            # Wykreślamy wielokrotności
            for j in range(i * i, n + 1, i):
                sito[j] = False
    
    # Zbieramy znalezione liczby pierwsze
    for i in range(2, n + 1):
        if sito[i]:
            pierwsze.append(i)
    
    return pierwsze, len(pierwsze)

# Test funkcji
pierwsze, ile = znajdz_pierwsze(20)
print(f"Znaleziono {ile} liczb pierwszych: {pierwsze}")
```

## Zadanie 2: Analiza przedziałów (6 punktów)
Napisz funkcję `analiza_przedzialow(start, end, krok)`, która:
1. Analizuje kolejne przedziały liczbowe o zadanej wielkości
2. Dla każdego przedziału liczy liczby pierwsze
3. Wyświetla statystyki w formie tabelki

```python
# Przykład użycia:
analiza_przedzialow(1, 100, 20)

# Oczekiwany format wyniku:
# Przedział      Ile pierwszych    Przykłady
# 1-20          8                 2,3,5,7...
# 21-40         4                 23,29,31,37
# ...
```

### Rozwiązanie:
```python
def analiza_przedzialow(start, end, krok):
    # Znajdujemy wszystkie liczby pierwsze do end
    wszystkie_pierwsze, _ = znajdz_pierwsze(end)
    
    print(f"{'Przedział':<15} {'Ile pierwszych':<15} {'Przykłady':<20}")
    print("-" * 50)
    
    for i in range(start, end, krok):
        przedzial_start = i
        przedzial_end = min(i + krok - 1, end)
        
        # Filtrujemy liczby pierwsze dla aktualnego przedziału
        pierwsze_w_przedziale = [p for p in wszystkie_pierwsze 
                                if przedzial_start <= p <= przedzial_end]
        
        # Formatujemy przykłady (pierwsze 4 liczby lub mniej)
        przyklady = ",".join(map(str, pierwsze_w_przedziale[:4]))
        if len(pierwsze_w_przedziale) > 4:
            przyklady += "..."
        
        print(f"{f'{przedzial_start}-{przedzial_end}':<15} "
              f"{len(pierwsze_w_przedziale):<15} {przyklady:<20}")

# Test funkcji
analiza_przedzialow(1, 100, 20)
```

## Zadanie 3: Parzyste = Pierwsze + Pierwsze? (4 punkty)
Napisz funkcję `hipoteza_goldbacha(n)`, która:
1. Przyjmuje parzystą liczbę n > 2
2. Sprawdza, czy można ją przedstawić jako sumę dwóch liczb pierwszych
3. Zwraca listę wszystkich możliwych par liczb pierwszych

```python
# Przykład:
print(hipoteza_goldbacha(10))
# Powinno zwrócić: [(3,7), (5,5)]
# bo 10 = 3+7 = 5+5
```

### Rozwiązanie:
```python
def hipoteza_goldbacha(n):
    if n <= 2 or n % 2 != 0:
        return []
    
    # Znajdujemy wszystkie liczby pierwsze do n
    pierwsze, _ = znajdz_pierwsze(n)
    pary = []
    
    # Sprawdzamy wszystkie możliwe pary
    for p1 in pierwsze:
        if p1 > n/2:  # Optymalizacja - wystarczy sprawdzić do połowy
            break
        
        p2 = n - p1  # Druga potencjalna liczba pierwsza
        if p2 in pierwsze:
            pary.append((p1, p2))
    
    return pary

# Test funkcji
for n in [10, 20, 30]:
    print(f"\nLiczba {n} jako suma liczb pierwszych:")
    print(hipoteza_goldbacha(n))
```

## Zadanie 4: Pytanie teoretyczne (2 punkty)
Wyjaśnij w komentarzu:
- Dlaczego w oryginalnym algorytmie zaczynamy wykreślanie od i*i, a nie od i*2?
- Co by się stało, gdybyśmy zaczęli od i*2?

### Rozwiązanie:
```python
"""
Wykreślanie zaczynamy od i*i (zamiast od i*2) z dwóch powodów:

1. Wszystkie mniejsze wielokrotności zostały już wcześniej wykreślone:
   - Dla i = 2: wykreślamy 4,6,8,10,...
   - Dla i = 3: 6,9,12,... (ale 6 już wykreślone)
   - Dla i = 4: nie sprawdzamy (4 już wykreślone)
   - Dla i = 5: zaczynamy od 25, bo 5*2=10, 5*3=15, 5*4=20 już wykreślone

2. Jest to optymalizacja wydajności:
   - Mniej niepotrzebnych operacji wykreślania
   - Te same liczby nie są wykreślane wielokrotnie
   
Gdybyśmy zaczynali od i*2:
- Algorytm działałby poprawnie (wynik byłby ten sam)
- Ale wykonywałby niepotrzebne operacje wykreślania
- Np. liczba 12 byłaby wykreślana przez 2 (jako 2*6) i przez 3 (jako 3*4)
"""
```

## Kryteria oceny:
- Poprawna implementacja podstawowa (8 punktów)
- Poprawna analiza przedziałów (6 punktów)
- Poprawna implementacja hipotezy Goldbacha (4 punkty)
- Poprawna odpowiedź teoretyczna (2 punkty)

> [!TIP]
> 1. Pamiętaj o inicjalizacji sita odpowiednimi wartościami
> 2. Użyj f-stringów do formatowania wyników
> 3. Możesz użyć metody .center() do wyrównania tekstu w tabeli
> 4. Do pierwiastka możesz użyć `n ** 0.5` lub `math.sqrt(n)`

Powodzenia!