# Algorytm wydawania reszty
Algorytm rozwiązuje problem obliczeniowy: mając daną kwotę (resztę) oraz zestaw dostępnych nominałów monet/banknotów, jak wydać tę kwotę używając minimalnej liczby monet?

## Zasada działania algorytmu zachłannego:

- Posortuj dostępne nominały od największego do najmniejszego
- Wybieraj największy nominał, który nie przekracza pozostałej do wydania kwoty*
- Powtarzaj krok 2, aż cała kwota zostanie wydana

### Czym jest 'algorytm zachłanny'
Algorytm zachłanny (ang. greedy algorithm) – algorytm, który w celu wyznaczenia rozwiązania w każdym kroku dokonuje zachłannego, tj. najlepiej rokującego w danym momencie wyboru rozwiązania częściowego. 

Innymi słowy algorytm zachłanny nie dokonuje oceny czy w kolejnych krokach jest sens wykonywać dane działanie, dokonuje decyzji lokalnie optymalnej, dokonuje on wyboru wydającego się w danej chwili najlepszym, kontynuując rozwiązanie podproblemu wynikającego z podjętej decyzji

(źródło: https://pl.wikipedia.org/wiki/Algorytm_zach%C5%82anny)


### Implementacja w Pythonie
```python
def wydaj_reszte(kwota, nominaly):
    # Sortujemy nominały malejąco
    nominaly.sort(reverse=True)
    wydane_monety = {}

    # Dla każdego nominału
    for nominal in nominaly:
        # Ile razy możemy użyć danego nominału
        ilosc = kwota // nominal

        if ilosc > 0:
            wydane_monety[nominal] = ilosc
            kwota -= nominal * ilosc

    return wydane_monety


# Przykład użycia
nominaly = [1, 2, 5, 10, 20, 50, 100, 200, 500]
kwota = 237
wynik = wydaj_reszte(kwota, nominaly)

print(f"Reszta {kwota} zł:")
for nominal, ilosc in wynik.items():
    print(f"{ilosc} x {nominal} zł")
...
```

*. czy 'reszta z dzielenia' ma tu jakies znaczenie? Dlaczego algorytm nie działa dla przykladu [1,4,5] i potrzeby wydania 8? A z jakiego powodu nie działa dobrze dla przykladu [20, 50, 100, 200] i potrzeby wydania 60?

### Rozszerzenie zadania:
* Sprawdzaj czy wydanie reszty jest możliwe
* Obsłuż przypadek, gdy niektórych nominałów brakuje
* Wyświetlaj sumaryczną liczbę wydanych monet

## Programowanie dynamiczne
Podejście 'zachłane' nie zawsze jest optymalne tj. ma swoje ograniczenia, warto więc zrobić krok wstecz i wrócić do idei dzielenia dużego problemu na małe tj. przypomnij sobie różnicę w podejściu top-down (zstępujące) i bottom-up (wstępujące)

Spróbuj zrozumieć algorytm poniżej wyciągając wnioski

### Implementacja w Pythonie
```python
def min_liczba_monet_dp(kwota, nominaly):
    dp = [kwota + 1] * (kwota + 1)
    dp[0] = 0

    wybrane_monety = [[] for _ in range(kwota + 1)]

    for i in range(1, kwota + 1):
        for nominal in nominaly:
            if nominal <= i and dp[i - nominal] + 1 < dp[i]:
                dp[i] = dp[i - nominal] + 1
                wybrane_monety[i] = wybrane_monety[i - nominal].copy()
                wybrane_monety[i].append(nominal)

    return dp[kwota], wybrane_monety[kwota]


# Przykład użycia
nominaly = [1, 3, 4]
kwota = 6
min_monet, wybrane = min_liczba_monet_dp(kwota, nominaly)

print(f"Minimalna liczba monet dla kwoty {kwota}: {min_monet}")
print(f"Wybrane monety: {wybrane}")
```
