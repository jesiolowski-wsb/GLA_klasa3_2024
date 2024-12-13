# Sito Eratostenesa - ćwiczenie sprawdzające (20 punktów)

**Czas: 45 minut**

## Wprowadzenie
Sito Eratostenesa to algorytm służący do znajdowania liczb pierwszych w zadanym zakresie. Twoim zadaniem będzie zaimplementowanie tego algorytmu i przeanalizowanie jego wydajności.

## Zadanie 1: Implementacja podstawowa (8 punkty)
Napisz funkcję `sito_eratostenesa(n)`, która:
1. Przyjmuje liczbę n jako górny zakres poszukiwań
2. Zwraca listę wszystkich liczb pierwszych z zakresu od 2 do n
3. Implementuje klasyczny algorytm Sita Eratostenesa tj.

### Przykład algorytmu w pseudokodzie
```
    sito = [1..n]
    DLA i = 2 DO n:
        JEŻELI sito[i] == PRAWDA:
            // Tak, linia poniżej to delikatna zmiana wzgledem implementacji z zadania maturalnego
            DLA j = i * i DO n KROK i:
                sito[j] = FAŁSZ
```


### Przykład użycia:
```python
print(sito_eratostenesa(20))  
# Powinno zwrócić: [2, 3, 5, 7, 11, 13, 17, 19]
```

## Zadanie 2: Analiza wydajności (8 punktów)
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

## Zadanie 3: Analiza wydajności (2 punkty)
1. Zaimplementuj obie wersje funkcji
2. Użyj funkcji `porownaj_wydajnosc(n)`, która:
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
