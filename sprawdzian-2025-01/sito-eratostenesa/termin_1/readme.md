# Sito Eratostenesa - ćwiczenie sprawdzające (20 punktów)

**Czas: 45 minut**

## Wprowadzenie
Sito Eratostenesa to algorytm służący do znajdowania liczb pierwszych w zadanym zakresie. Twoim zadaniem jest zaimplementowanie tego algorytmu i przeanalizowanie jego wydajności.

## Zadanie 1: Implementacja podstawowa (8 punkty)
Napisz funkcję `sito_eratostenesa(n)`, która:
1. Przyjmuje liczbę n jako górny zakres poszukiwań
2. Zwraca listę wszystkich liczb pierwszych z zakresu od 2 do n
3. Implementuje klasyczny algorytm Sita Eratostenesa tj.

### Przykład algorytmu w pseudokodzie
```
sito - tablica z wartościami PRAWDA
Wynik: wszystkie liczby k gdzie sito[k] == PRAWDA

    DLA i = 2 DO n:
        JEŻELI sito[i] == PRAWDA:
            // linia poniżej jest delikatnie zmieniona wzgledem implementacji z zadania maturalnego które realizowaliśmy na zajęciach
            DLA j = i * i DO n KROK i:
                sito[j] = FAŁSZ
```


### Przykład użycia:
```python
print(sito_eratostenesa(20))
# Powinno zwrócić: [2, 3, 5, 7, 11, 13, 17, 19]
```

## Zadanie 2: Analiza wydajności v1 (8 punktów)
Zmodyfikuj swoją implementację tworząc dwie wersje funkcji:
1. `sito_pelne(n)` - sprawdzającą wszystkie liczby do n
2. `sito_optymalne(n)` - sprawdzającą liczby tylko do pierwiastka z n

Każda funkcja powinna:
- Zliczać liczbę wykonanych iteracji głównej pętli
- Zliczać całkowitą liczbę operacji (sprawdzenia + oznaczenia liczb)
- Mierzyć czas wykonania
> [!TIP]
> ```python
> import time
> start_time = time.time()
> czas = time.time() - start_time
> ```
>
- Zwracać krotkę: (liczby_pierwsze, liczba_iteracji, liczba_operacji, czas)

### Rozwiązanie:

```python
import time

def sito_pelne(n):
    start_time = time.time()
    licznik_iteracji = 0
    licznik_operacji = 0

    sito = [True] * (n + 1)
    sito[0] = sito[1] = False

    for i in range(2, n + 1):  # Pełny zakres
        licznik_iteracji += 1
        if sito[i]:
            licznik_operacji += 1
            for j in range(i * i, n + 1, i):
                sito[j] = False
                licznik_operacji += 1

    liczby_pierwsze = [i for i in range(2, n + 1) if sito[i]]
    czas = time.time() - start_time

    return liczby_pierwsze, licznik_iteracji, licznik_operacji, czas

def sito_optymalne(n):
    start_time = time.time()
    licznik_iteracji = 0
    licznik_operacji = 0

    sito = [True] * (n + 1)
    sito[0] = sito[1] = False

    for i in range(2, int(n ** 0.5) + 1):  # Zakres do pierwiastka
        licznik_iteracji += 1
        if sito[i]:
            licznik_operacji += 1
            for j in range(i * i, n + 1, i):
                sito[j] = False
                licznik_operacji += 1

    liczby_pierwsze = [i for i in range(2, n + 1) if sito[i]]
    czas = time.time() - start_time

    return liczby_pierwsze, licznik_iteracji, licznik_operacji, czas
```

## Zadanie 3: Analiza wydajności v2 (2 punkty)
1. Zaimplementuj obie wersje funkcji
2. Użyj funkcji `porownaj_wydajnosc(n)` (kod poniżej), która:
   - Wywołuje obie implementacje dla zadanego n
   - Wyświetla tabelkę porównawczą z wynikami
   - Oblicza procentową różnicę w liczbie iteracji i operacji

### Funkcja porownaj_wydajnosc(n):
```python
def porownaj_wydajnosc(n):
    print(f"Porównanie wydajności dla n = {n}")
    print("-" * 50)

    wyniki_pelne = sito_pelne(n)
    wyniki_optymalne = sito_optymalne(n)

    print(f"{'Wersja':<15} {'Iteracje':<12} {'Operacje':<12} {'Czas':<8}")
    print("-" * 50)
    print(f"{'Pełna':<15} {wyniki_pelne[1]:<12} {wyniki_pelne[2]:<12} {wyniki_pelne[3]:.4f}s")
    print(f"{'Optymalna':<15} {wyniki_optymalne[1]:<12} {wyniki_optymalne[2]:<12} {wyniki_optymalne[3]:.4f}s")

    roznica_iteracji = ((wyniki_pelne[1] - wyniki_optymalne[1]) / wyniki_pelne[1]) * 100
    print(f"\nOptymalizacja zmniejszyła liczbę iteracji o {roznica_iteracji:.2f}%")

# Test
porownaj_wydajnosc(1000000)
```

## Zadanie 4: Pytanie do analizy (2 punkty) - odpowiedź napisz w komentarzu w kodzie:
- Dlaczego mimo mniejszej liczby iteracji obie wersje znajdują te same liczby pierwsze?


## Kryteria oceny:
- Poprawność implementacji podstawowej (8 punkty)
- Implementacja obu wersji z licznikami (8 punkty)
- Poprawna implementacja porównania wydajności (2 punkty)
- Wyciągnięcie poprawnego wniosku z pytania do analizy (2 punkty)


Powodzenia!