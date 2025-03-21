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


# Przykład użycia
nominaly = [1, 2, 5, 10, 20, 50, 100, 200, 500]
kwota = 237
wynik = wydaj_reszte(kwota, nominaly)
...
```

*. czy 'reszta z dzielenia' ma tu jakies znaczenie? Dlaczego algorytm nie działa dla przykladu [1,4,5] i potrzeby wydania 8? A z jakiego powodu nie działa dobrze dla przykladu [20, 50, 100, 200] i potrzeby wydania 60?

### Rozszerzenie zadania:
* Sprawdzaj czy wydanie reszty jest możliwe
* Obsłuż przypadek, gdy niektórych nominałów brakuje
* Wyświetlaj sumaryczną liczbę wydanych monet

## Programowanie dymaniczne
Podejście 'zachłane' nie zawsze jest optymalne tj. ma swoje ograniczenia, warto więc zrobić krok wstecz i wrócić do idei dzielenia dużego problemu na małe tj. przypomnij sobie różnicę w podejściu top-down (zstępujące) i bottom-up (wstępujące)

### Implementacja w Pythonie
```python
...
```
