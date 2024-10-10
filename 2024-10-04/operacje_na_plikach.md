
# Operacje na plikach w Pythonie

## 1. Otwieranie pliku z użyciem `with`

```python
with open('plik.txt', 'r') as plik:
    zawartosc = plik.read()
```
- Konstrukcja `with` automatycznie zamyka plik po zakończeniu operacji, nawet jeśli wystąpi błąd.
- Idealna do pracy z plikami, by unikać ręcznego zamykania.

## 2. Otwieranie pliku bez `with`

```python
plik = open('plik.txt', 'r')
zawartosc = plik.read()
plik.close()
```
- Należy pamiętać o zamknięciu pliku po zakończeniu pracy, aby zwolnić zasoby.

---

## Zapisywanie do pliku

```python
imie = "a"
nazwisko = "b"
with open('uczniowie.txt', 'w') as plik:
    plik.write(imie + ' ' + nazwisko + '\n')
```
- Tryb `'w'` otwiera plik do zapisu, nadpisując jego zawartość.
- Aby dodać dane do istniejącego pliku, użyj trybu `'a'` (append).

---

## Różne sposoby odczytu plików

### Odczyt całego pliku do zmiennej

```python
with open('plik.txt', 'r') as plik:
    zawartosc = plik.read()
```
- Odczytuje całą zawartość pliku jako jeden ciąg znaków.

### Odczyt linia po linii

```python
with open('plik.txt', 'r') as plik:
    for linia in plik:
        print(linia)
```
- Odczyt każdej linii z pliku osobno, przydatne dla dużych plików.

### Odczyt określonej liczby znaków

```python
with open('plik.txt', 'r') as plik:
    fragment = plik.read(100)
```
- Odczytuje tylko pierwsze 100 znaków z pliku.

### Odczyt pliku JSON

```python
import json

with open('plik.json', 'r') as plik:
    dane_json = json.load(plik)
```
- Odczyt i automatyczne przekształcenie danych z pliku JSON do słownika lub innej struktury danych.
