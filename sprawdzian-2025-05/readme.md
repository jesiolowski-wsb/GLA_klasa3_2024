# Sprawdzian z podstawowych algorytmów w Pythonie
**Czas: 60 minut**  
**Maksymalna liczba punktów: 22**

> [!NOTE]
> - Dla każdego rozwiązania utwórz osobny plik w strukturze:
> ```
> \sprawdzian-2025-05\
>                     \nazwisko-imie\
>                                   \zad1.py
>                                   \zad2.py
>                                   \zad3.py
>                                   \zad4.py
> ```
> - Oceniane będą: poprawność działania, styl kodu oraz efektywność rozwiązania

---

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

### Przykład:
```python
print(znajdz_pierwsze(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(znajdz_pierwsze(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

> [!TIP]
> Zauważ, że wystarczy sprawdzać liczby do pierwiastka z n, oraz że wykreślanie wielokrotności możesz zacząć od `i*i`, a nie od `i*2`.

### Rozwiązanie:
```python
def znajdz_pierwsze(n):
    """
    Znajduje wszystkie liczby pierwsze nie większe od n
    za pomocą algorytmu Sita Eratostenesa.

    Args:
        n: górna granica zakresu poszukiwań

    Returns:
        lista liczb pierwszych nie większych od n
    """
    # Inicjalizacja tablicy wartości logicznych
    sito = [True] * (n + 1)
    # 0 i 1 nie są liczbami pierwszymi
    sito[0] = sito[1] = False

    # Wyznaczanie liczb pierwszych
    for i in range(2, int(n ** 0.5) + 1):
        if sito[i]:
            # Wykreślanie wielokrotności liczby i
            for j in range(i * i, n + 1, i):
                sito[j] = False

    # Zbieranie znalezionych liczb pierwszych
    pierwsze = [i for i in range(n + 1) if sito[i]]

    return pierwsze


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

### Rozwiązanie:
```python
def nwd(a, b):
    """
    Oblicza Największy Wspólny Dzielnik dwóch liczb
    metodą Euklidesa.

    Args:
        a, b: liczby całkowite

    Returns:
        Największy Wspólny Dzielnik a i b
    """
    # Obsługa wartości bezwzględnych
    a, b = abs(a), abs(b)

    # Warunek zakończenia rekurencji
    if b == 0:
        return a

    # Wywołanie rekurencyjne
    return nwd(b, a % b)


def nww(a, b):
    """
    Oblicza Najmniejszą Wspólną Wielokrotność dwóch liczb.

    Args:
        a, b: liczby całkowite

    Returns:
        Najmniejsza Wspólna Wielokrotność a i b
    """
    # Obsługa wartości zerowych
    if a == 0 or b == 0:
        return 0

    # NWW = |a * b| / NWD(a, b)
    return abs(a * b) // nwd(a, b)


# Testy NWD
print(nwd(12, 18))  # 6
print(nwd(35, 14))  # 7
print(nwd(13, 7))  # 1

# Testy NWW
print(nww(12, 18))  # 36
print(nww(6, 8))  # 24
print(nww(7, 13))  # 91
```

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

### Rozwiązanie:
```python
def fib_rekurencyjnie(n):
    """
    Generuje n pierwszych wyrazów ciągu Fibonacciego
    metodą rekurencyjną z zapamiętywaniem już obliczonych wartości.

    Args:
        n: liczba wyrazów ciągu do wygenerowania

    Returns:
        lista n pierwszych wyrazów ciągu Fibonacciego
    """
    # Słownik dla zapamiętywania już obliczonych wartości
    juz_obliczone = {0: 0, 1: 1}

    def fib_z_pamietaniem(k):
        if k in juz_obliczone:
            return juz_obliczone[k]
        # Obliczenie wartości F(k) i zapisanie w słowniku
        juz_obliczone[k] = fib_z_pamietaniem(k - 1) + fib_z_pamietaniem(k - 2)
        return juz_obliczone[k]

    # Generowanie listy wyrazów
    wynik = []
    for i in range(n):
        wynik.append(fib_z_pamietaniem(i))

    return wynik


def fib_iteracyjnie(n):
    """
    Generuje n pierwszych wyrazów ciągu Fibonacciego
    metodą iteracyjną.

    Args:
        n: liczba wyrazów ciągu do wygenerowania

    Returns:
        lista n pierwszych wyrazów ciągu Fibonacciego
    """
    if n <= 0:
        return []

    if n == 1:
        return [0]

    # Inicjalizacja pierwszych dwóch wyrazów ciągu
    wynik = [0, 1]

    # Generowanie pozostałych wyrazów
    for i in range(2, n):
        wynik.append(wynik[i - 1] + wynik[i - 2])

    return wynik


# Testy
print(fib_rekurencyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fib_iteracyjnie(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

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

### Rozwiązanie:
```python
def skroc_ulamek(licznik, mianownik):
    """
    Skraca ułamek do postaci nieskracalnej.
    
    Args:
        licznik: licznik ułamka
        mianownik: mianownik ułamka
        
    Returns:
        krotka (licznik, mianownik) w postaci nieskracalnej
    """
    if mianownik == 0:
        raise ValueError("Mianownik nie może być równy 0")
    
    # Określenie znaku ułamka
    znak = 1
    if (licznik < 0 and mianownik > 0) or (licznik > 0 and mianownik < 0):
        znak = -1
    
    # Wartości bezwzględne dla obliczeń
    licznik, mianownik = abs(licznik), abs(mianownik)
    
    # Obliczenie NWD i skrócenie ułamka
    dzielnik = nwd(licznik, mianownik)
    licznik = znak * (licznik // dzielnik)
    mianownik = mianownik // dzielnik
    
    return licznik, mianownik

def dodaj_ulamki(l1, m1, l2, m2):
    """
    Dodaje dwa ułamki.
    
    Args:
        l1, m1: licznik i mianownik pierwszego ułamka
        l2, m2: licznik i mianownik drugiego ułamka
        
    Returns:
        krotka (licznik, mianownik) sumy w postaci nieskracalnej
    """
    if m1 == 0 or m2 == 0:
        raise ValueError("Mianownik nie może być równy 0")
    
    # Obliczenie wspólnego mianownika (NWW)
    wspolny_mianownik = nww(m1, m2)
    
    # Obliczenie liczników po sprowadzeniu do wspólnego mianownika
    nowy_l1 = l1 * (wspolny_mianownik // m1)
    nowy_l2 = l2 * (wspolny_mianownik // m2)
    
    # Dodanie liczników
    suma_licznik = nowy_l1 + nowy_l2
    
    # Skrócenie wyniku
    return skroc_ulamek(suma_licznik, wspolny_mianownik)

def odejmij_ulamki(l1, m1, l2, m2):
    """
    Odejmuje drugi ułamek od pierwszego.
    
    Args:
        l1, m1: licznik i mianownik pierwszego ułamka
        l2, m2: licznik i mianownik drugiego ułamka
        
    Returns:
        krotka (licznik, mianownik) różnicy w postaci nieskracalnej
    """
    # Sprowadzamy odejmowanie do dodawania z przeciwnym znakiem
    return dodaj_ulamki(l1, m1, -l2, m2)

# Testy
print(skroc_ulamek(12, 18))         # (2, 3)
print(dodaj_ulamki(1, 2, 1, 3))     # (5, 6)
print(odejmij_ulamki(3, 4, 1, 2))   # (1, 4)
```


---

Powodzenia!
