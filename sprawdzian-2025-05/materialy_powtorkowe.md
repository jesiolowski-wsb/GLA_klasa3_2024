# Materiały powtórkowe przed sprawdzianem z podstawowych algorytmów

## 1. Sito Eratostenesa

Sito Eratostenesa to algorytm służący do znajdowania wszystkich liczb pierwszych nie większych od zadanej liczby n.

### 1.1 Opis algorytmu:
1. Tworzymy tablicę wartości logicznych (True/False) od 0 do n, początkowo wszystkie ustawione na True
2. Oznaczamy 0 i 1 jako False (nie są liczbami pierwszymi)
3. Przechodzimy przez kolejne liczby, zaczynając od 2:
   - Jeśli liczba jest oznaczona jako True (jest pierwsza), to wszystkie jej wielokrotności oznaczamy jako False
   - Wystarczy sprawdzić liczby do pierwiastka z n
   - Wykreślanie wielokrotności zaczynamy od kwadratu liczby (np. dla 2 zaczynamy od 4, nie od 2)

### 1.2 Przykładowa implementacja:

```python
def sito_eratostenesa(n):
    # Inicjalizacja tablicy
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False  # 0 i 1 nie są pierwsze
    
    # Główna pętla sita
    for i in range(2, int(n**0.5) + 1):
        if sito[i]:
            # Wykreślanie wielokrotności
            for j in range(i*i, n + 1, i):
                sito[j] = False
    
    # Zbieranie wyników
    pierwsze = []
    for i in range(2, n + 1):
        if sito[i]:
            pierwsze.append(i)
    
    return pierwsze

# Przykład użycia:
print(sito_eratostenesa(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
```

### 1.3 Ważne optymalizacje:
- Sprawdzanie liczb tylko do pierwiastka z n (bo jeśli liczba n ma dzielnik większy od √n, to ma też odpowiadający mu dzielnik mniejszy od √n)
- Rozpoczynanie wykreślania wielokrotności od i*i (bo mniejsze wielokrotności zostały już wykreślone)
- Można także zauważyć, że wystarczy sprawdzać tylko liczby nieparzyste powyżej 2

## 2. Algorytm Euklidesa (NWD)

Algorytm Euklidesa służy do znajdowania Największego Wspólnego Dzielnika (NWD) dwóch liczb.

### 2.1 Opis algorytmu:
- Jeśli a i b są liczbami całkowitymi dodatnimi, to NWD(a, b) = NWD(b, a % b)
- Warunkiem zakończenia jest osiągnięcie b = 0, wtedy NWD(a, 0) = a

### 2.2 Implementacja rekurencyjna:

```python
def nwd(a, b):
    # Obsługa wartości bezwzględnych
    a, b = abs(a), abs(b)
    
    # Warunek zakończenia rekurencji
    if b == 0:
        return a
    
    # Wywołanie rekurencyjne
    return nwd(b, a % b)

# Przykłady:
print(nwd(12, 18))  # 6
print(nwd(35, 14))  # 7
print(nwd(13, 7))   # 1
```

### 2.3 Implementacja iteracyjna:

```python
def nwd_iteracyjny(a, b):
    # Obsługa wartości bezwzględnych
    a, b = abs(a), abs(b)
    
    # Pętla - zamiennik rekurencji
    while b != 0:
        a, b = b, a % b
    
    return a

# Przykłady:
print(nwd_iteracyjny(12, 18))  # 6
print(nwd_iteracyjny(35, 14))  # 7
print(nwd_iteracyjny(13, 7))   # 1
```

### 2.4 Zastosowania NWD:
- Skracanie ułamków
- Znajdowanie liczb względnie pierwszych
- Rozwiązywanie równań diofantycznych (tak, wiem że to dziwne określenie, ale chodzi o równanie z dwiema lub więcej niewiadomymi, w którym szukamy rozwiązań w liczbach całkowitych)

## 3. Najmniejsza Wspólna Wielokrotność (NWW)

Najmniejsza Wspólna Wielokrotność (NWW) to najmniejsza liczba, która jest wielokrotnością dwóch (lub więcej) liczb.

### 3.1 Związek z NWD:
NWW można obliczyć korzystając z właściwości:
NWW(a, b) = (a * b) / NWD(a, b)

### 3.2 Implementacja:

```python
def nww(a, b):
    # Obsługa przypadków szczególnych
    if a == 0 or b == 0:
        return 0
    
    # NWW = |a * b| / NWD(a, b)
    # Używamy dzielenia całkowitego (//) bo wynik zawsze będzie liczbą całkowitą
    return abs(a * b) // nwd(a, b)

# Przykłady:
print(nww(12, 18))  # 36
print(nww(6, 8))    # 24
print(nww(7, 13))   # 91
```

### 3.3 Zastosowania NWW:
- Sprowadzanie ułamków do wspólnego mianownika
- Problemy związane z cyklicznością zdarzeń

## 4. Ciąg Fibonacciego

Ciąg Fibonacciego to ciąg liczb, w którym każdy element jest sumą dwóch poprzednich.

### 4.1 Definicja ciągu:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) dla n > 1

### 4.2 Implementacja rekurencyjna:

```python
def fib_rekurencyjnie_prosty(n):
    # Przypadki bazowe
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Wywołanie rekurencyjne
    return fib_rekurencyjnie_prosty(n-1) + fib_rekurencyjnie_prosty(n-2)

# Uwaga: ta implementacja jest nieefektywna dla większych n!
```

### 4.3 Implementacja rekurencyjna z zapamiętywaniem:

```python
def fib_rekurencyjnie(n):
    # Słownik do zapamiętywania już obliczonych wartości
    juz_obliczone = {0: 0, 1: 1}
    
    def fib_z_pamietaniem(k):
        # Sprawdzamy, czy już obliczyliśmy tę wartość
        if k in juz_obliczone:
            return juz_obliczone[k]
        
        # Obliczamy nową wartość i zapisujemy ją w słowniku
        juz_obliczone[k] = fib_z_pamietaniem(k-1) + fib_z_pamietaniem(k-2)
        return juz_obliczone[k]
    
    # Generowanie listy n pierwszych wyrazów
    wyniki = []
    for i in range(n):
        wyniki.append(fib_z_pamietaniem(i))
    
    return wyniki

# Przykład:
print(fib_rekurencyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 4.4 Implementacja iteracyjna:

```python
def fib_iteracyjnie(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    # Pierwsze dwa wyrazy ciągu
    wyniki = [0, 1]
    
    # Generowanie kolejnych wyrazów
    for i in range(2, n):
        wyniki.append(wyniki[i-1] + wyniki[i-2])
    
    return wyniki

# Przykład:
print(fib_iteracyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 4.5 Zastosowania ciągu Fibonacciego:
- Modelowanie wielu zjawisk przyrodniczych
- Problemy związane z rekurencją i dynamicznym programowaniem
- Złota proporcja (stosunek kolejnych wyrazów dąży do liczby φ ≈ 1.618)

## 5. Operacje na ułamkach

Operacje na ułamkach często wykorzystują algorytmy NWD i NWW.

### 5.1 Skracanie ułamka:

```python
def skroc_ulamek(licznik, mianownik):
    if mianownik == 0:
        raise ValueError("Mianownik nie może być równy zero")
    
    # Wyznaczenie znaku
    znak = 1
    if (licznik < 0 and mianownik > 0) or (licznik > 0 and mianownik < 0):
        znak = -1
    
    # Wartości bezwzględne do obliczeń
    licznik, mianownik = abs(licznik), abs(mianownik)
    
    # Skrócenie przez NWD
    dzielnik = nwd(licznik, mianownik)
    licznik = znak * (licznik // dzielnik)
    mianownik = mianownik // dzielnik
    
    return (licznik, mianownik)

# Przykład:
print(skroc_ulamek(12, 18))  # (2, 3)
```

### 5.2 Dodawanie ułamków:

```python
def dodaj_ulamki(l1, m1, l2, m2):
    if m1 == 0 or m2 == 0:
        raise ValueError("Mianowniki nie mogą być równe zero")
    
    # Wyznaczenie wspólnego mianownika (NWW)
    wspolny_mianownik = nww(m1, m2)
    
    # Obliczenie licznika po sprowadzeniu do wspólnego mianownika
    licznik = l1 * (wspolny_mianownik // m1) + l2 * (wspolny_mianownik // m2)
    
    # Skrócenie wyniku
    return skroc_ulamek(licznik, wspolny_mianownik)

# Przykład:
print(dodaj_ulamki(1, 2, 1, 3))  # (5, 6) = 1/2 + 1/3 = 3/6 + 2/6 = 5/6
```

### 5.3 Odejmowanie ułamków:

```python
def odejmij_ulamki(l1, m1, l2, m2):
    # Odejmowanie to dodawanie z przeciwnym znakiem drugiego ułamka
    return dodaj_ulamki(l1, m1, -l2, m2)

# Przykład:
print(odejmij_ulamki(3, 4, 1, 2))  # (1, 4) = 3/4 - 1/2 = 3/4 - 2/4 = 1/4
```

## 6. Przykładowe zadania

### Zadanie 1: Znajdź wszystkie liczby pierwsze od 1 do 50
```python
# Rozwiązanie:
liczby_pierwsze = sito_eratostenesa(50)
print(liczby_pierwsze)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Zadanie 2: Oblicz NWD i NWW dla liczb 24 i 36
```python
# Rozwiązanie:
print(f"NWD(24, 36) = {nwd(24, 36)}")  # 12
print(f"NWW(24, 36) = {nww(24, 36)}")  # 72
```

### Zadanie 3: Podaj siódmy wyraz ciągu Fibonacciego
```python
# Rozwiązanie:
fib = fib_iteracyjnie(10)
print(f"F(7) = {fib[7]}")  # F(7) = 13
```

### Zadanie 4: Skróć ułamek 48/60 do najprostszej postaci
```python
# Rozwiązanie:
print(skroc_ulamek(48, 60))  # (4, 5)
```

### Zadanie 5: Oblicz sumę ułamków 2/5 + 3/7
```python
# Rozwiązanie:
suma = dodaj_ulamki(2, 5, 3, 7)
print(f"2/5 + 3/7 = {suma[0]}/{suma[1]}")  # 2/5 + 3/7 = 29/35
```
