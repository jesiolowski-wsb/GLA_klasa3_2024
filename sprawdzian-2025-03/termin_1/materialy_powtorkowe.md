# Materiały powtórkowe przed sprawdzianem

## 1. Operacje na tekście i plikach

### Zadanie 1.1: Zliczanie wielkich liter
Napisz funkcję, która zlicza wielkie litery w tekście.

```python
def licz_wielkie_litery(tekst):
    return sum(1 for znak in tekst if znak.isupper())

# Przykład:
print(licz_wielkie_litery("Ala Ma KOTA"))  # Wynik: 5
```

### Zadanie 1.2: Pobieranie co n-tego znaku
Napisz funkcję, która zwraca co n-ty znak ze stringa.

```python
def co_n_ty_znak(tekst, n, start=0):
    return tekst[start::n]

# Przykład:
print(co_n_ty_znak("abcdefghij", 2, 0))  # Wynik: "acegi"
print(co_n_ty_znak("abcdefghij", 3, 2))  # Wynik: "cf"
```

### Zadanie 1.3: Wczytywanie pliku i znajdowanie słowa
Odczytaj plik tekstowy i znajdź najdłuższe słowo.

```python
def znajdz_najdluzsze_slowo(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            slowa = plik.read().split()
            najdluzsze = ""
            for slowo in slowa:
                if len(slowo) > len(najdluzsze):
                    najdluzsze = slowo
            return najdluzsze
    except FileNotFoundError:
        return "Plik nie istnieje"

# Przykład:
# Najpierw utwórz plik "slowa.txt" z kilkoma słowami
with open("slowa.txt", "w") as plik:
    plik.write("python programowanie komputery algorytmy")

print(znajdz_najdluzsze_slowo("slowa.txt"))  # Wynik: "programowanie"
```

## 2. Algorytm wydawania reszty

### Zadanie 2.1: Proste wydawanie reszty
Napisz funkcję, która oblicza, ile monet o danym nominale potrzeba do wydania określonej kwoty.

```python
def ile_monet(kwota, nominal):
    return kwota // nominal, kwota % nominal

# Przykład:
ilosc, reszta = ile_monet(48, 10)
print(f"Potrzeba {ilosc} monet o nominale {nominal}, zostaje {reszta}")
# Wynik: "Potrzeba 4 monet o nominale 10, zostaje 8"
```

### Zadanie 2.2: Wydawanie reszty jednym nominałem
Napisz funkcję, która sprawdza, czy da się wydać dokładną kwotę używając tylko jednego rodzaju monet.

```python
def czy_mozna_wydac(kwota, nominal):
    return kwota % nominal == 0

# Przykład:
print(czy_mozna_wydac(100, 25))  # Wynik: True (4 x 25 = 100)
print(czy_mozna_wydac(98, 25))   # Wynik: False (nie da się)
```

### Zadanie 2.3: Uproszczona wersja wydawania reszty
Zaimplementuj uproszczoną wersję algorytmu wydawania reszty.

```python
def wydaj_reszte_uproszczona(kwota, nominaly):
    wynik = {}
    for nominal in sorted(nominaly, reverse=True):
        if kwota >= nominal:
            ilosc = kwota // nominal
            wynik[nominal] = ilosc
            kwota = kwota % nominal
    
    if kwota == 0:
        return wynik
    else:
        return None

# Przykład:
nominaly = [1, 5, 10, 25]
print(wydaj_reszte_uproszczona(63, nominaly))  # Wynik: {25: 2, 10: 1, 1: 3}
```

## 3. Operacje na planszy

### Zadanie 3.1: Inicjalizacja planszy
Napisz funkcję, która inicjalizuje planszę o podanych wymiarach.

```python
def stworz_plansze(wysokosc, szerokosc, wartosc_domyslna=0):
    return [[wartosc_domyslna for _ in range(szerokosc)] for _ in range(wysokosc)]

# Przykład:
plansza = stworz_plansze(3, 4)
for wiersz in plansza:
    print(wiersz)
# Wynik:
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
```

### Zadanie 3.2: Sprawdzenie granic planszy
Napisz funkcję, która sprawdza, czy dane współrzędne znajdują się na planszy.

```python
def czy_na_planszy(plansza, x, y):
    return 0 <= x < len(plansza) and 0 <= y < len(plansza[0])

# Przykład:
plansza = stworz_plansze(3, 4)
print(czy_na_planszy(plansza, 1, 2))  # Wynik: True
print(czy_na_planszy(plansza, 3, 2))  # Wynik: False
```

### Zadanie 3.3: Sprawdzenie sąsiadów
Napisz funkcję, która zwraca listę dozwolonych sąsiadów danego pola.

```python
def dozwoleni_sasiedzi(plansza, x, y):
    kierunki = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # prawo, dół, lewo, góra
    sasiedzi = []
    
    for dx, dy in kierunki:
        nowy_x, nowy_y = x + dx, y + dy
        if czy_na_planszy(plansza, nowy_x, nowy_y) and plansza[nowy_x][nowy_y] == 0:
            sasiedzi.append((nowy_x, nowy_y))
    
    return sasiedzi

# Przykład:
plansza = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]
print(dozwoleni_sasiedzi(plansza, 0, 0))  # Wynik: [(0, 1), (1, 0)]
```

## 4. Systemy liczbowe i statystyki

### Zadanie 4.1: Konwersja między systemami liczbowymi
Napisz funkcje do konwersji liczb między systemami liczbowymi.

```python
def dec_to_bin(liczba):
    return bin(liczba)[2:]  # Usuwamy przedrostek '0b'

def dec_to_hex(liczba):
    return hex(liczba)[2:].upper()  # Usuwamy przedrostek '0x'

def bin_to_dec(bin_str):
    return int(bin_str, 2)

def hex_to_dec(hex_str):
    return int(hex_str, 16)

# Przykłady:
print(dec_to_bin(42))      # Wynik: "101010"
print(dec_to_hex(42))      # Wynik: "2A"
print(bin_to_dec("101010"))  # Wynik: 42
print(hex_to_dec("2A"))    # Wynik: 42
```

### Zadanie 4.2: Obliczanie podstawowych statystyk
Napisz funkcje do obliczania podstawowych statystyk.

```python
def oblicz_srednia(liczby):
    return sum(liczby) / len(liczby)

def oblicz_mediane(liczby):
    posortowane = sorted(liczby)
    n = len(posortowane)
    if n % 2 == 0:
        return (posortowane[n//2-1] + posortowane[n//2]) / 2
    else:
        return posortowane[n//2]

# Przykłady:
liczby = [5, 2, 7, 1, 8, 3]
print(f"Średnia: {oblicz_srednia(liczby)}")  # Wynik: Średnia: 4.333333333333333
print(f"Mediana: {oblicz_mediane(liczby)}")  # Wynik: Mediana: 4.0
```

### Zadanie 4.3: Zliczanie cyfr
Napisz funkcję, która zlicza wystąpienia każdej cyfry w liście liczb.

```python
def licz_cyfry(liczby):
    cyfry = {}
    for liczba in liczby:
        for cyfra in str(liczba):
            if cyfra in cyfry:
                cyfry[cyfra] += 1
            else:
                cyfry[cyfra] = 1
    return cyfry

# Przykład:
liczby = [123, 456, 789, 123]
wynik = licz_cyfry(liczby)
for cyfra, ilosc in sorted(wynik.items()):
    print(f"{cyfra}: {ilosc}")
# Wynik:
# 1: 2
# 2: 2
# 3: 2
# 4: 1
# 5: 1
# 6: 1
# 7: 1
# 8: 1
# 9: 1
```

## 5. Wskazówki do sprawdzianu

1. **Operacje na plikach**:
   - Zawsze używaj konstrukcji `with open(...) as plik:` dla bezpiecznego otwarcia i zamknięcia pliku
   - Pamiętaj o obsłudze błędów (np. FileNotFoundError)
   - Używaj odpowiednich trybów (`'r'` dla odczytu, `'w'` dla zapisu)

2. **Operacje na stringach**:
   - Używaj slicingu (`tekst[start:stop:step]`) do pobierania części stringów
   - Pamiętaj o metodach `.isupper()`, `.islower()`, `.upper()`, `.lower()`
   - Funkcja `sum()` z wyrażeniem generatorowym jest przydatna do zliczania znaków

3. **Algorytm wydawania reszty**:
   - Sortuj nominały od największego do najmniejszego (`sorted(nominaly, reverse=True)`)
   - Używaj operatora dzielenia całkowitego (`//`) i modulo (`%`)
   - Zawsze sprawdzaj, czy udało się wydać całą kwotę

4. **Operacje na planszy**:
   - Zawsze sprawdzaj granice planszy przed dostępem do elementów
   - Używaj list kierunków dla przejrzystości kodu
   - Pamiętaj, że indeksy zaczynają się od 0

5. **Systemy liczbowe**:
   - Znaj podstawowe funkcje konwersji: `bin()`, `hex()`, `int(str, base)`
   - Pamiętaj o usuwaniu prefiksów ('0b', '0x') gdy potrzebny jest tylko ciąg cyfr
   - Używaj sortowania do obliczania mediany

6. **Sortowanie i manipulacja danymi**:
   - Używaj funkcji `sorted()` do sortowania bez modyfikacji oryginalnej listy
   - Znaj różnicę między `.sort()` (modyfikuje listę) a `sorted()` (zwraca nową listę)
   - Pamiętaj o formie wykładniczej (`1e-10`) przy porównywaniu wartości zmiennoprzecinkowych