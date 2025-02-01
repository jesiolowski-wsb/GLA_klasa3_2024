# Materiały powtórkowe - Sito Eratostenesa

## Podstawowe operacje (poziom ⭐)

### Zadanie 1: Inicjalizacja tablicy
Napisz funkcję, która utworzy tablicę wartości logicznych.

```python
# Oczekiwany wynik dla n = 5:
# [False, False, True, True, True, True]

# Rozwiązanie:
def utworz_sito(n):
    sito = [True] * (n + 1)  # +1 bo chcemy indeksy 0..n
    sito[0] = sito[1] = False  # 0 i 1 nie są pierwsze
    return sito

# Test
print(utworz_sito(5))
```

### Zadanie 2: Wyświetlanie liczb pierwszych
Napisz funkcję wyświetlającą liczby pierwsze z tablicy logicznej.

```python
# Dla tablicy [False, False, True, True, True, False]
# Powinno wyświetlić: 2, 3, 4

# Rozwiązanie:
def pokaz_pierwsze(sito):
    for i in range(len(sito)):
        if sito[i]:
            print(i, end=", ")
    print()

# Test
sito = [False, False, True, True, True, False]
pokaz_pierwsze(sito)
```

## Operacje na przedziałach (poziom ⭐)

### Zadanie 3: Liczenie w przedziale
Napisz funkcję liczącą ilość liczb pierwszych w przedziale.

```python
# Dla przedziału 10-20 powinno znaleźć 4 liczby: 11,13,17,19

# Rozwiązanie:
def licz_w_przedziale(sito, start, koniec):
    ile = 0
    for i in range(start, koniec + 1):
        if sito[i]:
            ile += 1
    return ile

# Test
sito = utworz_sito(20)  # używamy funkcji z zadania 1
print(f"W przedziale 10-20 jest {licz_w_przedziale(sito, 10, 20)} liczb pierwszych")
```

### Zadanie 4: Znajdowanie największej
Znajdź największą liczbę pierwszą mniejszą od n.

```python
# Dla n = 20 powinno znaleźć 19

# Rozwiązanie:
def znajdz_najwieksza(sito):
    for i in range(len(sito)-1, 1, -1):
        if sito[i]:
            return i
    return None

# Test
sito = utworz_sito(20)
print(f"Największa liczba pierwsza: {znajdz_najwieksza(sito)}")
```

## Implementacja sita (poziom ⭐⭐)

### Zadanie 5: Wykreślanie wielokrotności
Napisz funkcję wykreślającą wielokrotności danej liczby.

```python
# Dla liczby 3 i n = 10 powinno wykreślić: 6, 9

# Rozwiązanie:
def wykresl_wielokrotnosci(sito, liczba):
    for i in range(liczba * liczba, len(sito), liczba):
        sito[i] = False

# Test
sito = utworz_sito(10)
wykresl_wielokrotnosci(sito, 3)
print(sito)
```

### Zadanie 6: Proste sito
Zaimplementuj prostą wersję sita Eratostenesa.

```python
# Dla n = 10 powinno znaleźć: 2,3,5,7

# Rozwiązanie:
def proste_sito(n):
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sito[i]:
            for j in range(i * i, n + 1, i):
                sito[j] = False
    return sito

# Test
print([i for i in range(10) if proste_sito(10)[i]])
```

## Analiza wyników (poziom ⭐⭐)

### Zadanie 7: Statystyki przedziałów
Napisz funkcję analizującą rozkład liczb pierwszych.

```python
# Dla n = 20 powinno pokazać ile liczb pierwszych w każdej dziesiątce

# Rozwiązanie:
def statystyki(n, przedzial=10):
    sito = proste_sito(n)
    for start in range(0, n, przedzial):
        koniec = min(start + przedzial - 1, n)
        ile = sum(1 for i in range(start, koniec + 1) if sito[i])
        print(f"Przedział {start}-{koniec}: {ile} liczb pierwszych")

# Test
statystyki(20)
```

### Zadanie 8: Sprawdzanie sumy
Sprawdź, czy liczba jest sumą dwóch liczb pierwszych.

```python
# Dla 10 powinno znaleźć: 3+7, 5+5

# Rozwiązanie:
def znajdz_sumy(n):
    sito = proste_sito(n)
    pary = []
    for i in range(2, n//2 + 1):
        if sito[i] and sito[n-i]:
            pary.append((i, n-i))
    return pary

# Test
print(f"10 można przedstawić jako: {znajdz_sumy(10)}")
```

## Wskazówki do zapamiętania:
- Sito zawsze inicjalizujemy tablicą wartości `True`
- 0 i 1 nie są liczbami pierwszymi
- Wykreślanie zaczynamy od kwadratu liczby (i*i)
- Wystarczy sprawdzać do pierwiastka z n
- Używaj `n ** 0.5` do obliczenia pierwiastka
- Pamiętaj o właściwym zakresie indeksów w tablicy
- Optymalizacja: wykreślanie zaczynamy od i*i, nie od i*2

## Typowe pułapki:
1. Brak ustawienia 0 i 1 jako nie-pierwsze
2. Zły zakres w pętli (n vs n+1)
3. Rozpoczynanie wykreślania od i*2 zamiast i*i
4. Brak sprawdzenia czy liczba nie została już wykreślona
5. Niewłaściwe użycie indeksów przy dostępie do tablicy