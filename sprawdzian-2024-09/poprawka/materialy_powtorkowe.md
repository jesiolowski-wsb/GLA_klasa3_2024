# 10 zadań przygotowawczych do sprawdzianu z Pythona

## Zadanie 1: Pętla while z warunkiem wyjścia
Napisz program, który będzie prosić użytkownika o podawanie liczb i na bieżąco sprawdzać czy ich suma nie przekracza 100. Wyświetl końcową sumę.

**Przykład:**
``` przykład użycia:
Podaj liczbę: 34
Podaj liczbę: 99
Końcowa suma: 133.0
```

**Rozwiązanie:**
```python
suma = 0
while suma <= 100:
    liczba = float(input("Podaj liczbę: "))
    suma += liczba
print(f"Końcowa suma: {suma}")
```

## Zadanie 2: Funkcja matematyczna
Stwórz funkcję `kwadrat(n)`, która zwraca kwadrat liczby n. Następnie użyj tej funkcji do wypisania kwadratów liczb od 1 do 10.

**Rozwiązanie:**
```python
def kwadrat(n):
    return n ** 2

for i in range(1, 11):
    print(f"Kwadrat liczby {i} to {kwadrat(i)}")
```

## Zadanie 3: FizzBuzz z sumą cyfr
Napisz funkcję `fizzbuzz_suma(n)`, która generuje sekwencję liczb od 1 do n, ale zastępuje niektóre liczby słowami według następujących reguł:
- Jeśli liczba jest podzielna przez 3, wypisz **"Fizz"**
- Jeśli liczba jest podzielna przez 5, wypisz **"Buzz"**
- Jeśli liczba jest podzielna zarówno przez 3, jak i przez 5, wypisz **"FizzBuzz"**
- Jeśli suma cyfr liczby jest podzielna przez 3, dodaj na końcu **"- suma podzielna przez 3"**
- W pozostałych przypadkach wypisz samą liczbę

**wycinek outputu**
```
8
Fizz - suma (9) podzielna przez 3
Buzz
11
Fizz - suma (12) podzielna przez 3
13
14
FizzBuzz - suma (15) podzielna przez 3
16
17
```

**Rozwiązanie:**
```python
def suma_cyfr(num):
    return sum(int(cyfra) for cyfra in str(num))

def fizzbuzz_suma(n):
    for i in range(1, n+1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if suma_cyfr(i) % 3 == 0:
            output += f" (suma {i} podzielna przez 3)"
        print(output if output else i)

fizzbuzz_suma(20)
```

## Zadanie 4: Rekurencyjne obliczanie sumy cyfr
Napisz funkcję rekurencyjną `suma_cyfr(n)`, która oblicza sumę cyfr danej liczby całkowitej.

**Rozwiązanie:**
```python
def suma_cyfr(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_cyfr(n // 10)

print(suma_cyfr(123))  # Wynik: 6
print(suma_cyfr(9876))  # Wynik: 30
```

## Zadanie 5: Rysowanie trójkąta
Stwórz funkcję `rysuj_trojkat(n)`, która rysuje trójkąt prostokątny o wysokości n, używając gwiazdek.

**Rozwiązanie:**
```python
def rysuj_trojkat(n):
    for i in range(1, n+1):
        print('*' * i)

rysuj_trojkat(5)
```

## Zadanie 6: Prosta symulacja konsoli
Napisz program symulujący konsolę, który przyjmuje komendy "echo" (wypisuje argument), "add" (dodaje dwie liczby) i "quit" (kończy program). Zadbaj o to aby w wypadku podania błędnego formatu wejścia np `add 22` aplikacja nie zakonczyła działania

**Rozwiązanie:**
```python
while True:
    komenda = input("> ").split()
    if komenda[0] == "echo":
        print(" ".join(komenda[1:]))
    elif komenda[0] == "add":
        if len(komenda) == 3:
            print(float(komenda[1]) + float(komenda[2]))
        else:
            print ("Podaj dwie oddzielone spacją wartości do dodania")
    elif komenda[0] == "quit":
        break
    else:
        print("Nieznana komenda")
```

## Zadanie 7: Rekurencyjne odwracanie ciągu znaków
Zaimplementuj funkcję rekurencyjną `odwroc(s)`, która odwraca podany ciąg znaków.

**Rozwiązanie:**
```python
def odwroc(s):
    if len(s) <= 1:
        return s
    else:
        return odwroc(s[1:]) + s[0]

print(odwroc("Python"))  # Wynik: nohtyP
```

## Zadanie 8: Kalkulator z historią działań
Rozszerz prosty kalkulator stworzony na zajęciach dodając funkcję zapamiętywania historii ORAZ wyświetlania ostatnich 5 działań (czyt. historia może być dłuższa niż 5 ostatnich działań)

**Rozwiązanie:**
```python
historia = []

while True:
    dzialanie = input("Podaj działanie (lub 'historia' lub 'quit'): ")
    if dzialanie == 'quit':
        break
    elif dzialanie == 'historia':
        for h in historia[-5:]:
            print(h)
    else:
        wynik = eval(dzialanie)
        print(f"Wynik: {wynik}")
        historia.append(f"{dzialanie} = {wynik}")
```

## Zadanie 9: Generowanie ciągu Fibonacciego
Napisz funkcję `fib_gen(n)`, która generuje n pierwszych wyrazów ciągu Fibonacciego.

**Rozwiązanie:**
```python
def fib_list(n):
    a, b = 0, 1
    wynik = []
    # Znak podkreślnika (_) jest często używany jako zmienna tymczasowa 
    # tzn. w przypadkach, gdy nie potrzebujemy korzystać z danej wartości. 
    # To konwencja programistyczna oznaczająca, że zmienna nie będzie używana
    for _ in range(n):
        wynik.append(a)  
        a, b = b, a + b  
    return wynik

# Wypisujemy liczby Fibonacciego
for liczba in fib_list(10):
    print(liczba)
```
