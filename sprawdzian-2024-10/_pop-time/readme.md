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

### Rozwiązanie:

```python
def dec_to_ternary(liczba):
    if liczba == 0:
        return "0"
    
    liczba = int(liczba)
    wynik = ""
    while liczba > 0:
        reszta = liczba % 3
        wynik = str(reszta) + wynik
        liczba = liczba // 3
    return wynik

with open('decimal.txt', 'r') as plik:
    liczby = plik.readlines()
    liczby = [x.strip() for x in liczby]

with open('ternary.txt', 'w') as plik:
    for liczba in liczby:
        tern = dec_to_ternary(liczba)
        plik.write(f"{liczba} : {tern}\n")
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

### Rozwiązanie:

```python
def is_valid_phone(number):
    return (len(number) == 9 and 
            number.isdigit() and 
            number[0] in ['5', '6'])

with open('phones.txt', 'r') as plik:
    numery = plik.read().splitlines()
    
valid_numbers = [num for num in numery if is_valid_phone(num)]

with open('valid_phones.txt', 'w') as plik:
    for num in valid_numbers:
        plik.write(num + '\n')
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

### Rozwiązanie:

```python
def bin_to_dec(binary):
    return int(binary, 2)

with open('bin1.txt', 'r') as f1, open('bin2.txt', 'r') as f2:
    bin1 = f1.read().splitlines()
    bin2 = f2.read().splitlines()

sums = [bin_to_dec(b1) + bin_to_dec(b2) 
        for b1, b2 in zip(bin1, bin2)]

with open('sum.txt', 'w') as plik:
    for suma in sums:
        plik.write(f"{suma}\n")
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

### Rozwiązanie:

```python
def analyze_text(text):
    words = [word.strip('.,!?') for word in text.split()]
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    word_count = len(words)
    avg_length = round(sum(len(word) for word in words) / word_count, 1)

    return word_count, avg_length, sentence_count


with open('text.txt', 'r', encoding='utf-8') as plik:
    text = plik.read()

word_count, avg_length, sentence_count = analyze_text(text)

with open('stats.txt', 'w', encoding='utf-8') as plik:
    plik.write(f"Liczba słów: {word_count}\n")
    plik.write(f"Średnia długość słowa: {avg_length}\n")
    plik.write(f"Liczba zdań: {sentence_count}\n")

```

---

Powodzenia!