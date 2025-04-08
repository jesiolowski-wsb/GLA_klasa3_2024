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

### Rozwiązanie:
```python
with open("tajny_przekaz.txt", "r") as plik:
    slowa = [line.strip() for line in plik.readlines()]

max_wielkich = 0
slowo_z_max_wielkich = ""

for slowo in slowa:
    wielkie_litery = sum(1 for litera in slowo if litera.isupper())
    if wielkie_litery > max_wielkich:
        max_wielkich = wielkie_litery
        slowo_z_max_wielkich = slowo
    # Jeśli mamy tyle samo wielkich liter, zostawiamy pierwsze znalezione

tajna_wiadomosc = ""
for i in range(9, len(slowa), 10):  # Zaczynamy od indeksu 9 (10. słowo)
    if len(slowa[i]) >= 5:  # Sprawdź czy słowo ma co najmniej 5 liter
        tajna_wiadomosc += slowa[i][4]  # 5. litera (indeks 4)

with open("wyniki1.txt", "w") as wyniki:
    wyniki.write(f"Zadanie 1.1:\n{slowo_z_max_wielkich} ({max_wielkich} wielkie litery)\n\n")
    wyniki.write(f"Zadanie 1.2:\n{tajna_wiadomosc}\n")
```

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

### Rozwiązanie:
```python
def wydaj_reszte(kwota, nominaly):
    nominaly = sorted(nominaly, reverse=True)

    wydane_monety = {}
    pozostala_kwota = kwota

    for nominal in nominaly:
        # Ile razy możemy użyć danego nominału
        ilosc = pozostala_kwota // nominal

        if ilosc > 0:
            wydane_monety[nominal] = ilosc
            pozostala_kwota -= nominal * ilosc

    # Sprawdzamy czy udało się wydać całą resztę
    if pozostala_kwota > 0:
        print(f"Nie można wydać reszty {kwota} przy użyciu podanych nominałów.")
        return None

    return wydane_monety


nominaly1 = [1, 5, 10, 25, 100]
wynik1 = wydaj_reszte(142, nominaly1)
print("Wydanie reszty 142 przy nominałach [1, 5, 10, 25, 100]:")
if wynik1:
    for nominal, ilosc in wynik1.items():
        print(f"{ilosc} x {nominal}")

# Test gdy nie można wydać reszty
nominaly2 = [5, 10, 25]
wynik2 = wydaj_reszte(8, nominaly2)
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

### Rozwiązanie:
```python
def sprawdz_ruch(plansza, start_x, start_y, cel_x, cel_y):
    # Sprawdzenie czy współrzędne są w granicach planszy
    if (start_x < 0 or start_x >= len(plansza) or
            start_y < 0 or start_y >= len(plansza[0]) or
            cel_x < 0 or cel_x >= len(plansza) or
            cel_y < 0 or cel_y >= len(plansza[0])):
        return False

    # Sprawdzenie czy punkt startowy i docelowy to puste pola
    if plansza[start_x][start_y] == 1 or plansza[cel_x][cel_y] == 1:
        return False

    # Sprawdzenie czy ruch jest dozwolony (tylko o jedno pole w kierunku góra, dół, lewo, prawo)
    dozwolone_ruchy = [
        (start_x + 1, start_y),  # dół
        (start_x - 1, start_y),  # góra
        (start_x, start_y + 1),  # prawo
        (start_x, start_y - 1)  # lewo
    ]

    # Sprawdzenie czy punkt docelowy jest wśród dozwolonych ruchów
    return (cel_x, cel_y) in dozwolone_ruchy


# Test funkcji
plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

print(f"Ruch z (0,0) do (0,1): {sprawdz_ruch(plansza, 0, 0, 0, 1)}")  # True
print(f"Ruch z (0,0) do (1,0): {sprawdz_ruch(plansza, 0, 0, 1, 0)}")  # True
print(f"Ruch z (0,0) do (0,2): {sprawdz_ruch(plansza, 0, 0, 0, 2)}")  # False - przeszkoda
print(f"Ruch z (0,0) do (1,1): {sprawdz_ruch(plansza, 0, 0, 1, 1)}")  # False - ruch na ukos
```

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

### Rozwiązanie:
```python
def analiza_liczb():
    # Wczytanie liczb z pliku
    with open("liczby.txt", "r") as plik:
        liczby = [int(line.strip()) for line in plik.readlines()]

    # Tworzenie reprezentacji binarnych i szesnastkowych
    reprezentacje = []
    for liczba in liczby:
        bin_rep = bin(liczba)[2:]  # Usuwamy przedrostek '0b'
        hex_rep = hex(liczba)[2:].upper()  # Usuwamy przedrostek '0x' i konwertujemy na wielkie litery
        reprezentacje.append((liczba, bin_rep, hex_rep))

    # Obliczanie statystyk
    srednia = sum(liczby) / len(liczby)
    posortowane = sorted(liczby)
    if len(posortowane) % 2 == 0:
        mediana = (posortowane[len(posortowane) // 2 - 1] + posortowane[len(posortowane) // 2]) / 2
    else:
        mediana = posortowane[len(posortowane) // 2]

    # Liczenie wystąpień cyfr
    cyfry_statystyki = {}
    for liczba in liczby:
        for cyfra in str(liczba):
            if cyfra in cyfry_statystyki:
                cyfry_statystyki[cyfra] += 1
            else:
                cyfry_statystyki[cyfra] = 1

    # Zapisanie wyników do pliku
    with open("wyniki_liczby.txt", "w") as wyniki:
        wyniki.write("Zadanie 4.1:\n")
        for liczba, bin_rep, hex_rep in reprezentacje:
            wyniki.write(f"{liczba} -> binarnie: {bin_rep}, hex: {hex_rep}\n")

        wyniki.write("\nZadanie 4.2:\n")
        wyniki.write(f"Średnia: {srednia:.2f}\n")
        wyniki.write(f"Mediana: {mediana}\n")
        wyniki.write("Statystyki cyfr:\n")
        for cyfra in sorted(cyfry_statystyki.keys()):
            wyniki.write(f"{cyfra}: {cyfry_statystyki[cyfra]}\n")

    return reprezentacje, srednia, mediana, cyfry_statystyki


# Test funkcji
reprezentacje, srednia, mediana, statystyki = analiza_liczb()
print(f"Średnia: {srednia:.2f}")
print(f"Mediana: {mediana}")
print("Statystyki cyfr:")
for cyfra, ilosc in sorted(statystyki.items()):
    print(f"{cyfra}: {ilosc}")
```

## Powodzenia!