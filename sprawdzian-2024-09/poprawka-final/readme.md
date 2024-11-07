# Drugie (ostatnie) podejście poprawkowe do sprawdzianu z rekurencji i podstaw algorytmów (25.10.2024)
**Czas: 60 minut**  
**Maksymalna liczba punktów: 22**

## Zadanie 1: Tablica mnożenia (6 punktów)
Napisz funkcję `tablica_mnozenia(n)`, która generuje i wyświetla tablicę mnożenia o wymiarach n x n. Użyj pętli w pętli do stworzenia tej tablicy.

Przykład dla n = 5:
```
  1  2  3  4  5
  2  4  6  8 10
  3  6  9 12 15
  4  8 12 16 20
  5 10 15 20 25
```

> [!TIP] 
> Jeśli chcesz uzyskać efekt konkretnej ilości znaków w zmiennej wynikowej per wartość
> ```
> i=8
> print(f"{i:25}")
> ```
> wyświetli:
> ```
>                          8
> ```

### Rozwiązanie:

```python
def tablica_mnozenia(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i*j:3}", end=" ")  # :3 zapewnia, że każda liczba zajmuje 3 miejsca
        print()

print("Tablica mnożenia 5x5:")
tablica_mnozenia(5)
```


---

## Zadanie 2: Rekurencyjne odwracanie listy (7 punktów)
Napisz funkcję rekurencyjną `odwroc_liste(lista)`, która odwraca kolejność elementów w liście (bez użycia wbudowanych funkcji odwracania).

Przykład:
```python
print(odwroc_liste([1, 2, 3, 4, 5]))  # Powinno zwrócić [5, 4, 3, 2, 1]
print(odwroc_liste(['a', 'b', 'c']))  # Powinno zwrócić ['c', 'b', 'a']
```

### Rozwiązanie:

```python
def odwroc_liste(lista):
    if len(lista) <= 1:
        return lista
    else:
        return odwroc_liste(lista[1:]) + [lista[0]]

print("\nOdwrócona lista [1, 2, 3, 4, 5]:")
print(odwroc_liste([1, 2, 3, 4, 5]))


```

---

## Zadanie 3: Zgadywanka liczb (5 punktów)
Napisz program, który losuje liczbę od 1 do 100, a następnie prosi użytkownika o zgadnięcie tej liczby. Program powinien działać w nieskończonej pętli, dopóki użytkownik nie zgadnie liczby lub nie wpisze "koniec" aby zakończyć grę. Po każdej próbie program powinien informować, czy podana liczba jest za duża, za mała, czy prawidłowa.

Przykład działania:
```
Zgadnij liczbę od 1 do 100 (lub wpisz 'koniec' aby zakończyć):
> 50
Za mało!
> 75
Za dużo!
> 60
Brawo! Zgadłeś! Wylosowana liczba to 60.
Czy chcesz zagrać ponownie? (tak/nie): nie
Dziękuję za grę!
```

> [!TIP] 
> na zajęciach używaliśmy już `random.choice()`, tutaj lepsze zastosowanie będzie mieć `random.randint(1, 100)`

### Rozwiązanie:

```python
import random

def zgadywanka():
    while True:
        liczba = random.randint(1, 100)
        print("\nZgadnij liczbę od 1 do 100 (lub wpisz 'koniec' aby zakończyć):")

        while True:
            proba = input("> ")
            if proba.lower() == 'koniec':
                print("Dziękuję za grę!")
                return

            try:
                proba = int(proba)
                if proba < liczba:
                    print("Za mało!")
                elif proba > liczba:
                    print("Za dużo!")
                else:
                    print(f"Brawo! Zgadłeś! Wylosowana liczba to {liczba}.")
                    break
            except ValueError:
                print("Proszę podać liczbę lub 'koniec'.")

        if input("Czy chcesz zagrać ponownie? (tak/nie): ").lower() != 'tak':
            print("Dziękuję za grę!")
            break


zgadywanka()
```

---

## Zadanie 4: LuckyNumber (4 punktów)
Napisz funkcję `lucky_number(n)`, która dla liczb od 1 do n wyświetla:
- "Lucky" dla liczb podzielnych przez 2
- "Number" dla liczb większych niż 7
- "LuckyNumber" dla liczb spełniających oba warunki
- samą liczbę dla pozostałych przypadków

Przykład dla n = 10:
```python
lucky_number(10)
```

Wynik:
```
1
Lucky        # 2 jest podzielne przez 2
3
Lucky        # 4 jest podzielne przez 2
5
Lucky        # 6 jest podzielne przez 2
7
LuckyNumber  # 8 jest podzielne przez 2 i większe niż 7
9
LuckyNumber  # 10 jest podzielne przez 2 i większe niż 7
```

### Rozwiązanie:

```python
def lucky_number(n):
    for i in range(1, n + 1):
        if i % 2 == 0 and i > 7:
            print("LuckyNumber")
        elif i % 2 == 0:
            print("Lucky")
        elif i > 7:
            print("Number")
        else:
            print(i)

lucky_number(10)
```
