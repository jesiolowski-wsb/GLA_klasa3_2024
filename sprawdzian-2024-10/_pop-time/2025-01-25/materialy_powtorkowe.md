# 10 zadań przygotowawczych do sprawdzianu z Pythona

## Zadanie 1: Analiza tekstu
Napisz program, który zliczy liczbę wystąpień każdej samogłoski w tekście z pliku.

**Przykład:**
```python
tekst = "Python jest super!"
samogloski = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# Wynik powinien pokazać:
# a: 0
# e: 1
# i: 0
# o: 0
# u: 2
```

**Rozwiązanie:**
```python
with open('tekst.txt', 'r') as plik:
    tekst = plik.read().lower()
    samogloski = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for samogloska in samogloski:
        samogloski[samogloska] = tekst.count(samogloska)
        
    for samogloska, liczba in samogloski.items():
        print(f"{samogloska}: {liczba}")
```

## Zadanie 2: Łączenie list
Napisz program łączący dwie listy liczb parami i obliczający średnią każdej pary.

**Przykład:**
```python
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
# Wynik: [3.0, 4.0, 5.0, 6.0]
```

**Rozwiązanie:**
```python
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

srednie = [round((a + b) / 2, 1) for a, b in zip(lista1, lista2)]
print(srednie)
```

## Zadanie 3: Czyszczenie danych
Napisz program, który oczyści listę stringów z białych znaków na początku i końcu.

**Przykład:**
```python
dane = ["  Python  ", " Java ", "   C++"]
# Wynik: ["Python", "Java", "C++"]
```

**Rozwiązanie:**
```python
dane = ["  Python  ", " Java ", "   C++"]
oczyszczone = [tekst.strip() for tekst in dane]
print(oczyszczone)
```

## Zadanie 4: Parsowanie CSV
Napisz program, który przetworzy prosty format CSV.

**Przykład:**
```python
wiersz = "Jan,Kowalski,25,Warszawa"
# Wynik: ['Jan', 'Kowalski', '25', 'Warszawa']
```

**Rozwiązanie:**
```python
with open('dane.csv', 'r') as plik:
    for wiersz in plik:
        dane = wiersz.strip().split(',')
        print(dane)
```

## Zadanie 5: Sumowanie kolumn
Napisz program sumujący wartości w kolumnach pliku z liczbami.

**Przykład:**
```
1 2 3
4 5 6
7 8 9
# Suma kolumn: [12, 15, 18]
```

**Rozwiązanie:**
```python
with open('liczby.txt', 'r') as plik:
    # Wczytaj wszystkie linie i przekonwertuj na liczby
    macierz = [[int(num) for num in line.split()] for line in plik]
    
    # Użyj zip do transponowania i sum do sumowania kolumn
    sumy_kolumn = [sum(kolumna) for kolumna in zip(*macierz)]
    print(sumy_kolumn)
```

## Zadanie 6: Statystyki tekstu
Napisz program liczący podstawowe statystyki tekstu.

**Przykład:**
```python
tekst = "Python jest super. To świetny język!"
# Wynik:
# Liczba słów: 6
# Średnia długość słowa: 5
# Liczba zdań: 2
```

**Rozwiązanie:**
```python
tekst = "Python jest super. To świetny język!"
slowa = tekst.split()
zdania = tekst.split('.')

liczba_slow = len(slowa)
srednia_dlugosc = round(sum(len(slowo) for slowo in slowa) / liczba_slow)
liczba_zdan = len([zdanie for zdanie in zdania if zdanie.strip()])

print(f"Liczba słów: {liczba_slow}")
print(f"Średnia długość słowa: {srednia_dlugosc}")
print(f"Liczba zdań: {liczba_zdan}")
```

## Zadanie 7: Formatowanie numerów
Napisz program formatujący numery telefonów z pliku.

**Przykład:**
```python
numery = ["123456789", "987654321"]
# Wynik: ["123-456-789", "987-654-321"]
```

**Rozwiązanie:**
```python
def formatuj_numer(numer):
    numer = numer.strip()
    return f"{numer[:3]}-{numer[3:6]}-{numer[6:]}"

with open('numery.txt', 'r') as plik:
    numery = plik.readlines()
    sformatowane = [formatuj_numer(numer) for numer in numery if len(numer.strip()) == 9]
    print(sformatowane)
```

## Zadanie 8: Łączenie list z wagami
Napisz program łączący dwie listy z wagami.

**Przykład:**
```python
wartosci = [10, 20, 30]
wagi = [0.2, 0.3, 0.5]
# Wynik: 22.0 (10*0.2 + 20*0.3 + 30*0.5)
```

**Rozwiązanie:**
```python
wartosci = [10, 20, 30]
wagi = [0.2, 0.3, 0.5]

wynik = sum(wartosc * waga for wartosc, waga in zip(wartosci, wagi))
print(round(wynik, 1))
```

## Zadanie 9: Analiza ocen
Napisz program analizujący oceny uczniów z pliku.

**Przykład:**
```
Jan: 3,4,5
Anna: 5,5,4
Piotr: 4,3,4
```

**Rozwiązanie:**
```python
with open('oceny.txt', 'r') as plik:
    for linia in plik:
        uczen, oceny = linia.strip().split(':')
        oceny = [int(ocena) for ocena in oceny.split(',')]
        srednia = round(sum(oceny) / len(oceny), 2)
        print(f"{uczen}: {srednia}")
```

## Zadanie 10: Przetwarzanie adresów email
Napisz program, który przetworzy listę adresów email.

**Przykład:**
```python
emails = ["jan@gmail.com ", " anna@wp.pl ", "piotr@gmail.com"]
# Wynik: {'gmail.com': 2, 'wp.pl': 1}
```

**Rozwiązanie:**
```python
emails = ["jan@gmail.com ", " anna@wp.pl ", "piotr@gmail.com"]
domeny = {}

for email in emails:
    email = email.strip()
    domena = email.split('@')[1]
    domeny[domena] = domeny.get(domena, 0) + 1

print(domeny)
```
