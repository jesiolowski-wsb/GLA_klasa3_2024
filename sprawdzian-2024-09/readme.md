
# Sprawdzian z programowania w Pythonie - 20.09.2024

## Zadanie 1: Symulator kalkulatora (7 punktów)
Napisz program, który będzie działał w nieskończonej pętli (podobnie jak konsola z poprzednich lekcji). Program powinien przyjmować od użytkownika operację matematyczną w formacie `liczba1 operator liczba2` (np. `3 + 5`). Obsługuj następujące operatory: `+`, `-`, `*`, `/`. 

Jeśli użytkownik wpisze `quit`, program powinien się zakończyć.

**Przykład:**
```
> 5 + 3
Wynik: 8
> 10 * 2
Wynik: 20
> quit
Kalkulator zamknięty.
```

> [!TIP] 
> Istnieje wiele sposobów, aby w poprawny sposób pobrać od użytkownika dane wejściowe. 
> Wszystkie które zadziałąją są równie dobre, lecz na wypadek tego zadania najprostszym MOŻE okazać się użycie `.split()` (feel free to google)

> [!TIP] 
> W obrębie funkcji w pythonie istnieją słówka kluczowe `continue` oraz `break` - to może tu się przydać (jak wyżej - feel free to google :)

---

## Zadanie 2: Zmodyfikowany FizzBuzz (4 punkty)
Zaimplementuj **FUNKCJĘ** `fizzbuzz_v2(n)`, która dla liczb od 1 do n będzie wyświetlać:
- "Fizz" dla liczb podzielnych przez 3,
- "Buzz" dla liczb podzielnych przez 5,
- "FizzBuzz" dla liczb podzielnych zarówno przez 3, jak i 5,
- "Boom" dla liczb podzielnych przez 7,
- dla pozostałych liczb wypisuje samą liczbę.

**Przykład:**
```python
fizzbuzz_v2(20)
```

Wynik:
```
1
2
Fizz
4
Buzz
Fizz
Boom
8
Fizz
Buzz
11
Fizz
13
Boom
FizzBuzz
16
17
Fizz
19
Buzz
```

---

## Zadanie 3: Rysowanie prostokąta (3 punkty)
Napisz funkcję `rysuj_prostokat(szerokosc, wysokosc)`, która przyjmuje dwa argumenty: szerokość i wysokość, i rysuje prostokąt za pomocą znaków `#`. Prostokąt powinien mieć podaną szerokość i wysokość.

**Przykład:**
```python
rysuj_prostokat(5, 3)
```

Wynik:
```
#####
#####
#####
```

---
## Zadanie 4: Rekurencyjne sprawdzanie palindromu (8 punktów)
Napisz funkcję rekurencyjną `is_palindrome(s)`, która sprawdza, czy dany ciąg znaków jest palindromem. Palindrom to słowo, zdanie lub ciąg znaków, który czytany od przodu i od tyłu wygląda tak samo (ignorując spacje oraz wielkość liter).

> [!TIP] 
> W zależności od typu obiektu (zmienna to tez obiekt), mamy dostępne różne metody których możemy użyć np tj. dla zmiennej typu `string`, `.upper()` zmieni litery na DUZE, 
> ale dla zmiennej typu `int` zwróci błąd (czyt. wyjątek / `Exception`). W podobny sposób, metody zamieniające w stringu jego częśći (google: `python replace`) nie będą działać na zmiennej typu `int`

### Wskazówki:

Funkcja powinna działać w następujący sposób:

1. Jeśli ciąg ma długość 0 lub 1, jest palindromem.
2. Jeśli pierwszy i ostatni znak są takie same, funkcja powinna sprawdzić, czy środkowa część ciągu (bez pierwszego i ostatniego znaku) również jest palindromem.
3. Jeśli pierwszy i ostatni znak się różnią, ciąg nie jest palindromem.
4. Ignoruj spacje oraz wielkość liter w porównaniach.

### Przykłady:

```python
print(is_palindrome("Kajak"))            # True
print(is_palindrome("A to idiota"))      # True
print(is_palindrome("Python"))           # False
```

> [!TIP] 
> Stringi są iterowalne tzn możemy poruszać się po nich w pętli / iterując +1 / -1 np:
> ```python
> slowo = "kaczKa"
> for litera in slowo:
>    print(slowo[0])     # k
>    print(slowo[0+1])   # a
>    break
> ```
> ale bardzo często nie jest to konieczne gdy potrzebujemy dostać się do konkretnego elementu np. pierwszego elementu zbioru
> ```python
> print("kaczKa"[0])      # k
> print("kaczKa"[-1])     # a
> print("kaczKa"[0:5:2])  # kcK
> ```
> ...i z góry przepraszam jeśli to Wam tylko zaciemnia obraz :D
