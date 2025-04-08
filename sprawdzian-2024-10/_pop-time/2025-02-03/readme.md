# [POP-time] FINALNA poprawka sprawdzianu z obsługi plików i konwersji między systemami liczbowymi (03.02.2025)
**Czas: 45 minut**  
**Maksymalna liczba punktów: 22**


> [!NOTE]
> - Dla każdego rozwiązania poproszę osobny plik, tj struktura odpowiedzi powinna wyglądać tak:
> ```
> \sprawdzian-2024-10\_pop-time\2025-02-03\
>                                         \jak-kowalski\
>                                                      \zad1.py
>                                                      \zad2.py
>                                                      \zad3.py
>                                                      \zad4.py
> ```
> - Oceniane będą: poprawność działania, styl kodu oraz efektywność rozwiązania

---

## Zadanie 1: Konwerter HEX -> DEC (6 punktów)
Napisz program, który:
1. Wczyta z pliku `hex_input.txt` liczby szesnastkowe (jedna na linię)
2. Przekonwertuje je na system dziesiętny **BEZ UŻYCIA** `int(x, 16)`
3. Zapisze wyniki do `dec_output.txt` w formacie: `[HEX] : [DEC]`

Zawartość pliku `hex_input.txt`:
```
1A
2F
FF
```

Oczekiwana zawartość pliku `dec_output.txt`:
```
1A : 26
2F : 47
FF : 255
```

> [!TIP]
> Dla systemu szesnastkowego cyfry to: 0-9 oraz A=10, B=11, C=12, D=13, E=14, F=15.
> Każda pozycja to potęga liczby 16, np. "1A" = 1×16¹ + 10×16⁰ = 16 + 10 = 26

### Rozwiązanie:

```python
def hex_to_dec(hex_str):
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
                 '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    dec = 0
    for i, digit in enumerate(reversed(hex_str.upper())):
        dec += hex_digits[digit] * (16 ** i)
    return dec

with open('hex_input.txt', 'r') as plik:
    hex_numbers = plik.read().splitlines()

with open('dec_output.txt', 'w') as plik:
    for hex_num in hex_numbers:
        dec_num = hex_to_dec(hex_num)
        plik.write(f"{hex_num} : {dec_num}\n")
```

---

## Zadanie 2: Filtr palindromów (5 punktów)
Napisz program używając list comprehension, który:
1. Wczyta `words.txt` zawierający słowa (jedno w linii)
2. Wyfiltruje tylko palindromy (słowa czytane tak samo od przodu i od tyłu)
3. Zapisze do `palindromes.txt` tylko te słowa, które mają więcej niż 3 znaki

Zawartość pliku `words.txt`:
```
kayak
level
dog
noon
dad
radar
```

Oczekiwana zawartość pliku `palindromes.txt`:
```
kayak
level
radar
```

> [!TIP]
> Pamiętaj że string[::-1] odwraca string, a string.lower() zamienia wszystkie litery na małe

### Rozwiązanie:

```python
with open('words.txt', 'r') as plik:
    words = plik.read().splitlines()

palindromes = [word for word in words 
              if len(word) > 3 and word.lower() == word.lower()[::-1]]

with open('palindromes.txt', 'w') as plik:
    plik.write('\n'.join(palindromes))
```

---

## Zadanie 3: Generator kodów weryfikacyjnych (4 punkty)
Utwórz funkcję `generate_code()`, która:
1. Wygeneruje kod składający się z:
   - 2 wielkich liter (tylko spośród: A, B, C, D)
   - 3 cyfr (tylko parzyste: 0, 2, 4, 6, 8)
2. Dopisze wygenerowany kod do pliku `codes.txt`
3. Zwróci wygenerowany kod

Przykład wywołania:
```python
print(generate_code())  # Wyświetli np. "AB240"
print(generate_code())  # Wyświetli np. "DC682"
```

### Rozwiązanie:

```python
import random

def generate_code():
    letters = 'ABCD'
    digits = '02468'
    
    code = (
        ''.join(random.choice(letters) for _ in range(2)) +
        ''.join(random.choice(digits) for _ in range(3))
    )
    
    with open('codes.txt', 'a') as plik:
        plik.write(code + '\n')
    
    return code
```

---

## Zadanie 4: Licznik słów (7 punktów)
Napisz program, który:
1. Wczyta dwa pliki tekstowe: `file1.txt` i `file2.txt`
2. Używając list comprehension:
   - policzy ile razy każde słowo występuje w każdym pliku
   - znajdzie najczęściej występujące słowo w każdym pliku
3. Zapisze wyniki do `analysis.txt`

Zawartość pliku `file1.txt`:
```
python java python
ruby java sql
```

Zawartość pliku `file2.txt`:
```
python code java
code code python
```

Oczekiwana zawartość pliku `analysis.txt`:
```
Plik 1:
python: 2 razy
java: 2 razy
ruby: 1 raz
sql: 1 raz
Najczęstsze słowa: python, java

Plik 2:
python: 2 razy
code: 3 razy
java: 1 raz
Najczęstsze słowo: code
```

### Rozwiązanie:

```python
def count_words(filename):
    with open(filename, 'r') as plik:
        # Najpierw wczytaj wszystkie linie
        lines = plik.readlines()
        
        # Przygotuj listę na wszystkie słowa
        words = []
        
        # Przetwórz każdą linię
        for line in lines:
            # Podziel linię na słowa i dodaj do listy
            line_words = line.split()
            for word in line_words:
                words.append(word.lower())
        
    # Przygotuj listę na licznik słów
    word_counts = []
    
    # Dla każdego unikalnego słowa policz wystąpienia
    for word in sorted(set(words)):
        count = words.count(word)
        word_counts.append((word, count))
    
    # Znajdź najczęściej występujące słowa
    max_count = 0
    most_common = []
    
    for word, count in word_counts:
        if count > max_count:
            max_count = count
            most_common = [word]
        elif count == max_count:
            most_common.append(word)
    
    return word_counts, most_common

# Analiza obu plików
counts1, most_common1 = count_words('file1.txt')
counts2, most_common2 = count_words('file2.txt')

# Zapisanie wyników
with open('analysis.txt', 'w') as plik:
    # Wyniki dla pierwszego pliku
    plik.write('Plik 1:\n')
    for word, count in counts1:
        times = 'raz' if count == 1 else 'razy'
        plik.write(f'{word}: {count} {times}\n')
    plik.write(f'Najczęstsze słowa: {", ".join(most_common1)}\n\n')
    
    # Wyniki dla drugiego pliku
    plik.write('Plik 2:\n')
    for word, count in counts2:
        times = 'raz' if count == 1 else 'razy'
        plik.write(f'{word}: {count} {times}\n')
    plik.write(f'Najczęstsze słowo: {", ".join(most_common2)}\n')
```

---

Powodzenia!