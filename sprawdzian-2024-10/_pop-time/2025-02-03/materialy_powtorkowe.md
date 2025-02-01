# Zadania powtórkowe przed sprawdzianem

## Operacje na stringach i listach (poziom ⭐)

### Zadanie 1: Odwracanie słów
Napisz program, który odwróci kolejność słów w zdaniu.

```python
# Dane wejściowe:
text = "Python jest super"

# Oczekiwany wynik:
# "super jest Python"

# Rozwiązanie:
words = text.split()
reversed_text = " ".join(reversed(words))
print(reversed_text)
```

### Zadanie 2: Wielkie litery
Napisz program, który zamieni pierwsze litery każdego słowa na wielkie.

```python
# Dane wejściowe:
text = "python jest super"

# Oczekiwany wynik:
# "Python Jest Super"

# Rozwiązanie:
words = text.split()
capitalized = [word.capitalize() for word in words]
result = " ".join(capitalized)
print(result)
```

### Zadanie 3: Numerowanie linii
Napisz program, który ponumeruje każdą linię tekstu.

```python
# Dane wejściowe:
lines = ["python", "java", "cpp"]

# Oczekiwany wynik:
# 1: python
# 2: java
# 3: cpp

# Rozwiązanie:
for i, line in enumerate(lines, 1):
    print(f"{i}: {line}")
```

## Operacje na plikach (poziom ⭐)

### Zadanie 4: Zapisywanie do pliku
Napisz program, który zapisze listę imion do pliku.

```python
# Dane wejściowe:
names = ["Anna", "Jan", "Piotr"]

# Oczekiwana zawartość pliku names.txt:
# Anna
# Jan
# Piotr

# Rozwiązanie:
with open('names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')
```

### Zadanie 5: Czytanie z pliku
Napisz program, który wczyta plik i policzy liczbę linii.

```python
# Zawartość pliku data.txt:
# Python
# Java
# C++

# Rozwiązanie:
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(f"Liczba linii: {len(lines)}")
```

## Słowniki (poziom ⭐)

### Zadanie 6: Liczenie znaków
Napisz program, który policzy wystąpienia każdej litery w tekście.

```python
# Dane wejściowe:
text = "python"

# Oczekiwany wynik:
# {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

# Rozwiązanie:
counter = {}
for char in text:
    counter[char] = counter.get(char, 0) + 1
print(counter)
```

### Zadanie 7: Prosty słownik
Napisz program, który stworzy słownik ocen uczniów.

```python
# Dane wejściowe:
names = ["Anna", "Jan"]
grades = [5, 4]

# Oczekiwany wynik:
# {'Anna': 5, 'Jan': 4}

# Rozwiązanie:
grades_dict = {name: grade for name, grade in zip(names, grades)}
print(grades_dict)
```

## Listy składane (poziom ⭐⭐)

### Zadanie 8: Filtrowanie liczb
Napisz program, który wybierze tylko parzyste liczby.

```python
# Dane wejściowe:
numbers = [1, 2, 3, 4, 5, 6]

# Oczekiwany wynik:
# [2, 4, 6]

# Rozwiązanie:
even = [n for n in numbers if n % 2 == 0]
print(even)
```

### Zadanie 9: Długość słów
Napisz program, który stworzy listę długości słów.

```python
# Dane wejściowe:
words = ["python", "java", "c++"]

# Oczekiwany wynik:
# [6, 4, 3]

# Rozwiązanie:
lengths = [len(word) for word in words]
print(lengths)
```

## Random i max (poziom ⭐)

### Zadanie 10: Losowy wybór
Napisz program, który wylosuje 3 imiona z listy.

```python
# Dane wejściowe:
import random
names = ["Anna", "Jan", "Piotr", "Maria", "Tomek"]

# Przykładowy wynik:
# ['Jan', 'Maria', 'Anna']

# Rozwiązanie:
selected = []
for _ in range(3):
    name = random.choice(names)
    selected.append(name)
print(selected)
```

### Zadanie 11: Największa liczba
Napisz program znajdujący największą liczbę w liście.

```python
# Dane wejściowe:
numbers = [5, 2, 8, 1, 9, 3]

# Oczekiwany wynik:
# 9

# Rozwiązanie:
max_number = max(numbers)
print(max_number)
```

## Sortowanie (poziom ⭐)

### Zadanie 12: Sortowanie imion
Napisz program, który posortuje listę imion.

```python
# Dane wejściowe:
names = ["Zofia", "Adam", "Marek"]

# Oczekiwany wynik:
# ['Adam', 'Marek', 'Zofia']

# Rozwiązanie:
sorted_names = sorted(names)
print(sorted_names)
```

### Zadanie 13: Pomijanie duplikatów
Napisz program, który usunie powtórzenia z listy.

```python
# Dane wejściowe:
numbers = [1, 2, 2, 3, 3, 4]

# Oczekiwany wynik:
# [1, 2, 3, 4]

# Rozwiązanie:
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
```

### Zadanie 14: Łączenie stringów
Napisz program łączący listę słów w jedno zdanie.

```python
# Dane wejściowe:
words = ["Python", "jest", "super"]

# Oczekiwany wynik:
# "Python jest super"

# Rozwiązanie:
sentence = " ".join(words)
print(sentence)
```

### Zadanie 15: F-stringi
Napisz program formatujący dane osobowe.

```python
# Dane wejściowe:
name = "Jan"
age = 25
city = "Warszawa"

# Oczekiwany wynik:
# "Jan (25 lat) mieszka w Warszawie"

# Rozwiązanie:
info = f"{name} ({age} lat) mieszka w {city}"
print(info)
```

## Wskazówki do zapamiętania:
- `split()` dzieli string na listę słów
- `join()` łączy listę stringów w jeden string
- `upper()` zamienia tekst na wielkie litery
- `lower()` zamienia tekst na małe litery
- `enumerate()` numeruje elementy listy
- `random.choice()` losuje element z listy
- `max()` znajduje największy element
- `sorted()` sortuje elementy
- `append()` dodaje element na koniec listy
- `readlines()` czyta wszystkie linie z pliku
- List comprehension to skrócony zapis pętli for
- F-stringi (`f"..."`) ułatwiają formatowanie tekstu