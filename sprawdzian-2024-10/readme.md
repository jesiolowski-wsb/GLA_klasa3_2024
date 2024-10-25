# Sprawdzian z obsługi plików i konwersji między systemami liczbowymi - 25.10.2024
**Czas: 45 minut**  
**Maksymalna liczba punktów: 22**


> [!NOTE]
> - Dla każdego rozwiązania poproszę osobny plik, tj struktura odpowiedzi powinna wyglądać tak:
> ```
> \sprawdzian-2024-10\
>                    \jak-kowalski\
>                                 \zad1.py
>                                 \zad2.py
>                                 \zad3.py
> ```
> - Oceniane będą: poprawność działania, styl kodu oraz efektywność rozwiązania

---

## Zadanie 1: Konwerter z systemu dziesiętnego na binarny (6 punktów)
Napisz program, który:
1. Wczyta z pliku `liczby.txt` listę liczb w systemie dziesiętnym (założenie: jedna linia zawiera jedną liczbę)
2. Przekonwertuje każdą liczbę na system binarny **BEZ UŻYCIA WBUDOWANEJ FUNKCJI `bin()`**
3. Zapisze wyniki do pliku `wyniki.txt` w formacie:
   ```
   [liczba dziesiętna] : [liczba binarna]
   ```

Zawartość pliku `liczby.txt`:
```
8
4
6
```

Oczekiwana zawartość pliku `wyniki.txt`:
```
8 : 1000
4 : 100
6 : 110
```

> [!TIP]
> Aby przekonwertować liczbę z systemu dziesiętnego na binarny:
> 1. Dziel liczbę przez 2 i zapisuj resztę z dzielenia (0 lub 1)
> 2. Kontynuuj dzielenie wyniku przez 2, aż wynik będzie równy 0
> 3. Odczytaj cyfry od końca

[//]: # (### Rozwiązanie zadania 1:)
[//]: # (```python)
[//]: # ()
[//]: # (```)

---

## Zadanie 2: Analiza tekstu z listą składaną (5 punktów)
Napisz program, który:
1. Wczyta zawartość pliku `tekst.txt`
2. Używając list comprehension / listy składanej, stworzy listę wszystkich słów, które:
   - mają długość większą niż 3 znaki
   - zaczynają się wielką literą 
3. Zapisze wyniki do pliku `analiza.txt`, każde słowo w nowej linii

Tekst do sprawdzenia:
```
Ania i Tomek poszli do kina.
Potem kupili lody.
```

Oczekiwana zawartość pliku `analiza.txt`:
```
Ania
Tomek
Potem
```

> [!TIP]
> jeśli `.upper()` wywołane na elemencie łańcuchowym zmienia string na duże litery, `.isupper()` pomoże obsłużyć warunek sprawdzenia czy element jest napisany dużymi czy małymi literami

[//]: # (### Rozwiązanie zadania 2:)
[//]: # (```python)
[//]: # ()
[//]: # (```)

---

## Zadanie 3: Generator numerów ID (4 punkty)
Utwórz funkcję `generuj_id()`, która:
1. Wygeneruje nowe ID składające się z:
   - 2 wielkich liter (tylko A, B, C, D, E)
   - 3 cyfr (0-9)
2. Zapisze wygenerowane ID do pliku `id.txt`
3. Zwróci wygenerowane ID

Przykład wywołania:
```python
nowe_id = generuj_id()
print(nowe_id)  # np. "AB123"
```

[//]: # (### Rozwiązanie zadania 3:)
[//]: # (```python)
[//]: # ()
[//]: # (```)

---

## Zadanie 4: konwerter BIN -> DEC (7 punktów)
Napisz program, który:
1. Wczyta plik `dane.txt` zawierający liczby binarne (jedna w wierszu)
2. Używając list comprehension:
   - przekonwertuje liczby binarne na dziesiętne (zastosuj dowolny sposób konwersji)
   - zostawi tylko liczby parzyste
3. Zapisze wyniki do pliku `wyniki.txt`

Zawartość pliku `dane.txt`:
```
1010
1111
1000
```

Oczekiwana zawartość pliku `wyniki.txt`:
```
10
8
```

[//]: # (### Rozwiązanie zadania 4:)
[//]: # (```python)
[//]: # ()
[//]: # (```)

Powodzenia!
