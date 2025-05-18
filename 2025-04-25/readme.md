## 1. Napisz program który będzie realizować funkcję wbudowanej funkcji `len()` bez użycia tej funkcji:

### Rozwiązanie:
```python
def my_len(collection):
    count = 0
    for _ in collection:
        count += 1
    return count

# Przykład użycia
lista = [1, 2, 3, 4, 5]
print(my_len(lista))  # Wypisze: 5

tekst = "Python"
print(my_len(tekst))  # Wypisze: 6
```

```python
# alternatywnie z uzyciem sum()
def my_len_with_sum(kolekcja):
    return sum(1 for _ in kolekcja)
```

## 2. Napisz program który będzie dzielić stringi pisane PascalCasem lub camelCasem na takie, które zwrócą listę słów tj.

```python
print(split_by_capital(""))  # []
print(split_by_capital("HelloWorld"))  # ['Hello', 'World']
print(split_by_capital("getUserData"))  # ['get', 'User', 'Data']
```
### Rozwiązanie:
```python
```

## 3. Rozwiń program w taki sposób, aby pokrywał również warianty:
```python
print(split_by_capital("PDFLoader"))  # ['PDF', 'Loader']
print(split_by_capital("HTTPRequest")) # ['HTTP', 'Request']
print(split_by_capital("iOS")) # ['i', 'OS']
```

### Rozwiązanie:
```python
```
