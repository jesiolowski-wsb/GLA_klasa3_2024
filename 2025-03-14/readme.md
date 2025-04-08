# UWAGA: nie wolno sortować danych wejściowych!

## 1.
Napisz program (lub programy), który dla tablicy wyrazów znajdzie najdłuższy i najkrótszy wyraz. 

Jeśli w tablicy występuje więcej niż jeden wyraz o jednakowej długości, to odpowiedź
stanowić powinien mający pierwszeństwo w kolejności alfabetycznej (dla tablicy o wyrazach różnej długości).

Jeśli wszystkie wyrazy w tablicy mają jednakową długość, to minimum stanowić powinien wyraz pierwszy
w kolejności alfabetycznej, zaś maksimum ostatni.

Zastanów się:
- jak potraktować tablicę o długości 0?
- jak potraktować tablicę o długości 1?
- jak uniknąć niepotrzebnych operacji?

Algorytm odpowiedzialny za znajdowanie wyrazu najkrótszego i najdłuższego powinien działać z liniową złożonością czasową.

Przygotuj tablice wyrazów do testów.

### Rozwiązanie:
```python
def find_min_max_words(words):
    """
    Funkcja znajdująca najkrótszy i najdłuższy wyraz w tablicy zgodnie z kryteriami:
    - Jeśli w tablicy jest więcej wyrazów o tej samej długości, wybierany jest
      pierwszy/ostatni w kolejności alfabetycznej
    - Jeśli wszystkie wyrazy mają tę samą długość, najkrótszy to pierwszy alfabetycznie,
      najdłuższy to ostatni alfabetycznie

    Złożoność czasowa: O(n), gdzie n to liczba wyrazów

    Argumenty:
        words (list): Lista wyrazów do analizy

    Zwraca:
        tuple: (najkrótszy_wyraz, najdłuższy_wyraz) lub (None, None) dla pustej tablicy
    """
    # Przypadek brzegowy: pusta tablica
    if not words:
        return None, None

    # Przypadek brzegowy: tablica z jednym wyrazem
    if len(words) == 1:
        return words[0], words[0]

    # Inicjalizacja zmiennych pierwszym wyrazem
    shortest = words[0]
    longest = words[0]

    # Sprawdzenie, czy wszystkie wyrazy mają tę samą długość
    same_length = all(len(word) == len(words[0]) for word in words)

    if same_length:
        # Jeśli wszystkie wyrazy mają tę samą długość, znajdź pierwszy i ostatni alfabetycznie
        return min(words), max(words)

    # Analiza pozostałych wyrazów w tablicy
    for word in words[1:]:
        # Sprawdzenie najkrótszego wyrazu
        if len(word) < len(shortest) or (len(word) == len(shortest) and word < shortest):
            shortest = word

        # Sprawdzenie najdłuższego wyrazu
        if len(word) > len(longest) or (len(word) == len(longest) and word > longest):
            longest = word

    return shortest, longest


def test_word_analysis():
    """
    Funkcja testująca dla różnych przypadków
    """
    # Przypadek 1: Pusta tablica
    empty_array = []

    # Przypadek 2: Tablica z jednym wyrazem
    single_word_array = ["test"]

    # Przypadek 3: Tablica z wyrazami różnej długości
    mixed_length_array = ["apple", "banana", "kiwi", "strawberry", "fig", "orange"]

    # Przypadek 4: Tablica z wyrazami o tej samej długości
    same_length_array = ["apple", "juice", "grape", "melon", "lemon"]

    # Przypadek 5: Tablica z kilkoma wyrazami o maksymalnej/minimalnej długości
    multiple_min_max_array = ["cat", "dog", "elephant", "ant", "bee", "dinosaur", "anaconda"]

    # Przypadek 6: Sytuacja, gdy najkrótszych wyrazów jest kilka
    multiple_min_array = ["cat", "dog", "ant", "bee", "fox"]

    # Przypadek 7: Sytuacja, gdy najdłuższych wyrazów jest kilka
    multiple_max_array = ["elephant", "dinosaur", "crocodile", "alligator"]

    # Wyświetlenie wyników dla każdego przypadku
    print("Przypadek 1 (pusta tablica):")
    shortest, longest = find_min_max_words(empty_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

    print("\nPrzypadek 2 (jeden wyraz):")
    shortest, longest = find_min_max_words(single_word_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

    print("\nPrzypadek 3 (wyrazy różnej długości):")
    shortest, longest = find_min_max_words(mixed_length_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

    print("\nPrzypadek 4 (wyrazy o tej samej długości):")
    shortest, longest = find_min_max_words(same_length_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

    print("\nPrzypadek 5 (kilka wyrazów o minimalnej/maksymalnej długości):")
    shortest, longest = find_min_max_words(multiple_min_max_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

    print("\nPrzypadek 6 (kilka najkrótszych wyrazów):")
    shortest, longest = find_min_max_words(multiple_min_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

    print("\nPrzypadek 7 (kilka najdłuższych wyrazów):")
    shortest, longest = find_min_max_words(multiple_max_array)
    print(f"  Najkrótszy: {shortest}")
    print(f"  Najdłuższy: {longest}")

test_word_analysis()
```
