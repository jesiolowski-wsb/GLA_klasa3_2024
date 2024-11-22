# Sprawdzian poprawkowy z obsługi plików i systemów liczbowych (22.11.2024)
**Czas: 45 minut**  
**Maksymalna liczba punktów: 22**

> [!NOTE]
> - Dla każdego rozwiązania utwórz osobny plik w strukturze:
> ```
> \sprawdzian-2024-10\
>                    \termin_2\
>                             \nazwisko-imie\
>                                           \zad1.py
>                                           \zad2.py
>                                           \zad3.py
>                                           \zad4.py
> ```
> - Oceniane będą: poprawność działania, styl kodu oraz efektywność rozwiązania

## Zadanie 1: Konwerter DEC -> OCT (6 punktów)
Napisz program, który:
1. Wczyta z pliku `dec.txt` liczby dziesiętne (jedna na linię)
2. Przekonwertuje je na system ósemkowy BEZ UŻYCIA `oct()`
3. Zapisze wyniki do `wyniki.txt` w formacie: `[DEC] : [OCT]`

> [!TIP]
> System ósemkowy działa podobnie do binarnego, ale dzielimy przez 8 i zapisujemy reszty z dzielenia (0-7)

### Przykład:
Zawartość `dec.txt`:
```
15
64
42
```

Oczekiwana zawartość `wyniki.txt`:
```
15 : 17
64 : 100
42 : 52
```

### Rozwiązanie:
```python
def dec_to_oct(liczba):
    if liczba == 0:
        return "0"
    
    liczba = int(liczba)
    wynik = ""
    while liczba > 0:
        reszta = liczba % 8
        wynik = str(reszta) + wynik
        liczba = liczba // 8
    return wynik

with open('dec.txt', 'r') as plik:
    liczby = plik.read().splitlines()

with open('wyniki.txt', 'w') as plik:
    for liczba in liczby:
        oct_num = dec_to_oct(liczba)
        plik.write(f"{liczba} : {oct_num}\n")
```

## Zadanie 2: Filtrowanie pliku (5 punktów)
Napisz program używając list comprehension, który:
1. Wczyta `slowa.txt` 
2. Wyfiltruje słowa kończące się na 'ing'
3. Zapisze do `filtered.txt` tylko te słowa

### Przykład:
Zawartość `slowa.txt`:
```
running
cat
jumping
sleep
coding
```

Oczekiwana zawartość `filtered.txt`:
```
running
jumping
coding
```

> [!NOTE]
> Użyj dowolnego znanego sposobu aby znaleźć zakonczenie słowa (np. `.endswith()`)

### Rozwiązanie:
```python
with open('slowa.txt', 'r') as plik:
    tekst = plik.read().splitlines()
    
ing_words = [slowo for slowo in tekst if slowo.endswith('ing')]

with open('filtered.txt', 'w') as plik:
    plik.write('\n'.join(ing_words))
```

## Zadanie 3: Unikalny generator kodów (6 punkty)
Utwórz funkcję `generuj_kod()` tworzącą kody:
- 3 małe litery (a-z)
- 2 cyfry (0-9)

> [!IMPORTANT]
> Program powinien sprawdzać czy kod nie został już użyty (zapisany w pliku). Jeśli tak, wygeneruj następny / inny

### Przykład:
```python
print(generuj_kod())  # wyświetli wygenerowany kod (np.abc12)
```

### Rozwiązanie:
```python
import random


def generuj_kod():
    male_litery = ['a', 'b', 'c', 'd', 'e']
    cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def utworz_kod():
        kod_litery = ''
        for _ in range(3):
            kod_litery += random.choice(male_litery)

        kod_cyfry = ''
        for _ in range(2):
            kod_cyfry += random.choice(cyfry)

        return kod_litery + kod_cyfry

    # Wczytaj istniejące kody
    try:
        with open('kody.txt', 'r') as plik:
            uzyte_kody = plik.read().splitlines()
    except Exception:
        uzyte_kody = []

    # Generuj nowy kod dopóki nie będzie unikalny
    while True:
        nowy_kod = utworz_kod()
        if nowy_kod not in uzyte_kody:
            break

    # Zapisz nowy kod
    with open('kody.txt', 'a') as plik:
        plik.write(nowy_kod + '\n')

    return nowy_kod

print(generuj_kod())
```

## Zadanie 4: Konwerter OCT -> BIN (5 punktów)
Napisz program konwertujący liczby ósemkowe z pliku na binarne:
1. Wczytaj `oct.txt`
2. Przekonwertuj na BIN
3. Zapisz do `bin.txt` tylko liczby dłuższe niż 3 bity

### Przykład:
Zawartość `oct.txt`:
```
17
52
7
```

Oczekiwana zawartość `bin.txt`:
```
1111
101010
```

> [!TIP]
> W tym zadaniu możesz użyć wbudowanych w język python funkcji obsługi konwersji pomiędzy systemami liczbowymi

### Rozwiązanie:
```python
def oct_to_bin(oct_str):
    # Najpierw konwertujemy do dziesiętnego
    dec = int(oct_str, 8)
    
    # Teraz do binarnego
    if dec == 0:
        return "0"
        
    bin_str = ""
    while dec > 0:
        bin_str = str(dec % 2) + bin_str
        dec //= 2
    
    # Dopełniamy zerami z przodu aby mieć grupy po 3 bity
    while len(bin_str) % 3 != 0:
        bin_str = "0" + bin_str
    
    return bin_str

# Wczytanie i konwersja
with open('oct.txt', 'r') as plik:
    liczby = plik.read().splitlines()

# Konwersja i filtrowanie długich liczb
wyniki = [oct_to_bin(num) for num in liczby if len(oct_to_bin(num)) > 4]

# Zapis wyników
with open('bin.txt', 'w') as plik:
    plik.write('\n'.join(wyniki))
```

Powodzenia!
