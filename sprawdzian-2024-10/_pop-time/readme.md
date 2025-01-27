# [POP-time] poprawka sprawdzianu z obsługi plików i konwersji między systemami liczbowymi (27.01.2025)
**Czas: 45 minut**  
**Maksymalna liczba punktów: 22**


> [!NOTE]
> - Dla każdego rozwiązania poproszę osobny plik, tj struktura odpowiedzi powinna wyglądać tak:
> ```
> \sprawdzian-2024-10\
>                    \_pop-time\
>                             \jak-kowalski\
>                                          \zad1.py
>                                          \zad2.py
>                                          \zad3.py
> ```
> - Oceniane będą: poprawność działania, styl kodu, efektywność rozwiązania oraz spełnianie kryteriów polecenia

---

## Zadanie 1: System trójkowy (6 punktów)
Napisz program, który:
1. Wczyta z pliku `decimal.txt` listę liczb dziesiętnych (jedna w linii)
2. Przekonwertuje każdą liczbę na system trójkowy
3. Zapisze wyniki do pliku `ternary.txt` w formacie:
   ```
   [liczba dziesiętna] : [liczba w systemie trójkowym]
   ```

Zawartość pliku `decimal.txt`:
```
8
9
10
```

Oczekiwana zawartość pliku `ternary.txt`:
```
8 : 22
9 : 100
10 : 101
```

---

## Zadanie 2: Analiza numerów telefonów (5 punktów)
Napisz program, który:
1. Wczyta plik `phones.txt` zawierający numery telefonów (jeden w linii)
2. Używając list comprehension (list składanych), wyfiltruje numery które:
   - Mają dokładnie 9 cyfr
   - Zaczynają się od 5 lub 6
3. Zapisze poprawne numery do pliku `valid_phones.txt`

Zawartość pliku `phones.txt`:
```
123456789
512345678
612345678
51234567
789456123
```

Oczekiwana zawartość pliku `valid_phones.txt`:
```
512345678
612345678
```

---

## Zadanie 3: Sumator plików binarnych (4 punkty)
Napisz program, który:
1. Wczyta dwa pliki `bin1.txt` i `bin2.txt` zawierające liczby binarne
2. Zsumuje odpowiadające sobie liczby (w systemie dziesiętnym)
3. Zapisze wyniki do pliku `sum.txt`

Zawartość pliku `bin1.txt`:
```
1010
1100
```

Zawartość pliku `bin2.txt`:
```
0101
0011
```

Oczekiwana zawartość pliku `sum.txt`:
```
15
15
```

---

## Zadanie 4: Statystyki tekstu (7 punktów)
Napisz program analizujący plik tekstowy, który:
1. Wczyta plik `text.txt`
2. Używając list comprehension obliczy:
   - liczbę słów
   - średnią długość słowa
   - liczbę zdań (zakładamy, że zdanie kończy się `.`, `!` lub `?`)
3. Zapisze statystyki do pliku `stats.txt`

Zawartość pliku `text.txt`:
```
Python to jezyk programowania. Jest prosty w uzyciu! Czy nie sadzisz?
```

Oczekiwana zawartość pliku `stats.txt`:
```
Liczba słów: 11
Średnia długość słowa: 5.1
Liczba zdań: 3
```

---

Powodzenia!
