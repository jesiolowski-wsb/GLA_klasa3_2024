# Sprawdzian z Podstaw Programowania w Pythonie
**Punkty:** 22 pkt (> 11 pkt = ocena pozytywna)

Test sprawdzający wiedzę z dziedziny podstawy programowej w wersji podstawowej.

Rozwiązania wklej na githuba w formie `nazwisko_imie.py` w bieżącym folderze (tj. w tym o nazwie `sprawdzian-uzupelniajacy`)


---

## Zadanie 1 (6 punktów)
**Algorytmy na liczbach**

**a)** Napisz funkcję `sprawdz_pierwszosc(n)`, która sprawdzi czy liczba jest pierwsza używając metody naiwnej (3 pkt)

```python
def sprawdz_pierwszosc(n):
    # Twój kod tutaj
    pass
```

**b)** Napisz funkcję `dec_na_bin(liczba)`, która zamieni liczbę dziesiętną na binarną (bez użycia funkcji bin()) (3 pkt)

```python
def dec_na_bin(liczba):
    # Twój kod tutaj
    pass
```

---

## Zadanie 2 (5 punktów)
**Algorytmy na tekstach**

**a)** Napisz funkcję `szyfr_cezara(tekst, przesuniecie)`, która zaszyfruje tekst szyfrem Cezara (3 pkt)

```python
def szyfr_cezara(tekst, przesuniecie):
    # Twój kod tutaj
    pass

# Przykład użycia: szyfr_cezara("HELLO", 3) powinno zwrócić "KHOOR"
```

**b)** Napisz funkcję `znajdz_wzorzec(tekst, wzorzec)`, która znajdzie pierwsze wystąpienie wzorca w tekście metodą naiwną i zwróci jego pozycję (lub -1 jeśli nie znajdzie) (2 pkt)

```python
def znajdz_wzorzec(tekst, wzorzec):
    # Twój kod tutaj
    pass
```

---

## Zadanie 3 (3 punkty)
**Ciąg Fibonacciego**

Napisz funkcję rekurencyjną `fibonacci(n)`, która obliczy n-ty element ciągu Fibonacciego:

```python
def fibonacci(n):
    # Twój kod tutaj
    pass

# fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, fibonacci(3) = 2, itd.
```

---

## Zadanie 4 (4 punkty)
**Algorytm wydawania reszty**

Napisz funkcję `wydaj_reszte(kwota_reszty)`, która wyda resztę używając minimalnej liczby monet/banknotów. Dostępne nominały: [200, 100, 50, 20, 10, 5, 2, 1] (w groszach).

```python
def wydaj_reszte(kwota_reszty):
    # Twój kod tutaj
    pass

# Przykład: wydaj_reszte(287) powinno zwrócić słownik lub listę pokazującą ile banknotów/monet każdego nominału
```

---

## Zadanie 5 (4 punkty)
**Program kompleksowy**

Napisz kompletny program, który:
1. Wczyta od użytkownika listę liczb (oddzielonych spacjami)
2. Posortuje je rosnąco
3. Sprawdzi, które z nich są liczbami pierwszymi
4. Wyświetli wyniki w czytelnej formie

```python
# Twój kompletny program tutaj
```

---

**Uwagi:**
- Kod powinien być czytelny i zawierać komentarze tam, gdzie to konieczne
- Można używać wbudowanych funkcji Pythona, chyba że zadanie wymaga inaczej
- W przypadku problemów z implementacją, napisz pseudokod - otrzymasz punkty częściowe
- Pamiętaj o obsłudze przypadków brzegowych (np. puste listy, liczby ujemne)