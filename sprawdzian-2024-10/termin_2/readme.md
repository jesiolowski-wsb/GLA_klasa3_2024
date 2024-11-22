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
001111
101010
```

> [!TIP]
> W tym zadaniu możesz użyć wbudowanych w język python funkcji obsługi konwersji pomiędzy systemami liczbowymi


Powodzenia!
