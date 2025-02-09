# [POP-time] poprawka sprawdzianu z bramek logicznych
**Czas: 45 minut**  
**Maksymalna liczba punktów: 20**

# System alarmowy - projekt zabezpieczeń (20 punktów)

## Wprowadzenie
Jesteś inżynierem pracującym nad systemem alarmowym dla małego muzeum. System wykorzystuje różne czujniki i bramki logiczne do wykrywania potencjalnych włamań i zagrożeń. Twoim zadaniem jest zaimplementowanie kluczowych elementów systemu.

## Zadanie 1: Podstawowe moduły bezpieczeństwa (6 punktów)
Zaimplementuj następujące moduły systemu alarmowego:

1. **czujnik_ruchu(czujnik1, czujnik2)** - funkcja symulująca bramkę OR, alarm włącza się gdy którykolwiek z czujników wykryje ruch
2. **drzwi_bezpieczne(zamek_glowny, zamek_awaryjny)** - funkcja symulująca bramkę AND, drzwi są bezpieczne tylko gdy oba zamki są aktywne
3. **wykryj_awarie(status_systemu)** - funkcja symulująca bramkę NOT, zwraca True gdy system nie działa prawidłowo
4. **alarm_przeciwpozarowy(czujnik_dymu, czujnik_temperatury)** - funkcja symulująca bramkę XOR, włącza alarm gdy tylko jeden z czujników wykryje zagrożenie (zabezpieczenie przed fałszywymi alarmami)

```python
# Przykład użycia:
print("Test systemu przeciwpożarowego:")
print(f"Tylko dym: {alarm_przeciwpozarowy(True, False)}")      # True
print(f"Dym i temperatura: {alarm_przeciwpozarowy(True, True)}") # False (możliwa awaria czujników)
```

### Rozwiązanie

```python
def czujnik_ruchu(czujnik1, czujnik2):
    """
    Implementacja bramki OR - alarm gdy którykolwiek czujnik wykryje ruch
    """
    return czujnik1 or czujnik2

def drzwi_bezpieczne(zamek_glowny, zamek_awaryjny):
    """
    Implementacja bramki AND - bezpieczne tylko gdy oba zamki działają
    """
    return zamek_glowny and zamek_awaryjny

def wykryj_awarie(status_systemu):
    """
    Implementacja bramki NOT - True gdy system nie działa
    """
    return not status_systemu

def alarm_przeciwpozarowy(czujnik_dymu, czujnik_temperatury):
    """
    Implementacja bramki XOR - alarm gdy tylko jeden czujnik wykryje zagrożenie
    """
    return (czujnik_dymu or czujnik_temperatury) and not (czujnik_dymu and czujnik_temperatury)

# Testy podstawowych modułów:
print("=== Testy podstawowych modułów ===")
print("\nTest czujnika ruchu:")
print(f"Oba nieaktywne: {czujnik_ruchu(False, False)}")        # False
print(f"Jeden aktywny: {czujnik_ruchu(True, False)}")          # True
print(f"Oba aktywne: {czujnik_ruchu(True, True)}")            # True

print("\nTest zabezpieczenia drzwi:")
print(f"Oba zamki aktywne: {drzwi_bezpieczne(True, True)}")    # True
print(f"Jeden zamek aktywny: {drzwi_bezpieczne(True, False)}") # False

print("\nTest systemu przeciwpożarowego:")
print(f"Tylko dym: {alarm_przeciwpozarowy(True, False)}")       # True
print(f"Oba czujniki: {alarm_przeciwpozarowy(True, True)}")     # False
```

## Zadanie 2: Panel kontrolny (6 punktów)
Napisz funkcję `wyswietl_stan_systemu()`, która pokaże działanie wszystkich modułów bezpieczeństwa w formie tabeli:

### Rozwiązanie

```python
def wyswietl_stan_systemu():
    print("Czujnik1  Czujnik2  Ruch   Bezp.  AwariaSys  Ppoż")
    print("-" * 55)
    
    for a in [False, True]:
        for b in [False, True]:
            print(f"{int(a):<9} {int(b):<9}", end=" ")
            print(f"{int(czujnik_ruchu(a,b)):<7}", end=" ")
            print(f"{int(drzwi_bezpieczne(a,b)):<7}", end=" ")
            print(f"{int(wykryj_awarie(a)):<9}", end=" ")
            print(f"{int(alarm_przeciwpozarowy(a,b))}")

# Wywołanie:
wyswietl_stan_systemu()
```

## Zadanie 3: Inteligentny system antywłamaniowy (8 punktów)

Muzeum potrzebuje zaawansowanego systemu wykrywania włamań. Zaprojektuj funkcję `wykryj_wlamanie(ruch, wibracje, godziny_otwarcia)`, która:

1. Przyjmuje trzy parametry:
   - `ruch` - czy wykryto ruch (True/False)
   - `wibracje` - czy wykryto wibracje szyb (True/False)
   - `godziny_otwarcia` - czy muzeum jest otwarte (True/False)

2. System powinien działać według zasady:
   `ALARM = (wykryto_ruch AND wykryto_wibracje) XOR (NOT godziny_otwarcia)`
   
   Czyli alarm włącza się gdy:
   - Wykryto jednocześnie ruch i wibracje podczas godzin otwarcia
   - LUB gdy muzeum jest zamknięte (ale nie oba przypadki na raz - mogłoby to oznaczać awarię systemu)

Przetestuj system wyświetlając wszystkie możliwe scenariusze:

### Oczekiwany format wyniku:
```
Ruch  Wibracje  Otwarte  ALARM
--------------------------------
0     0         0        1
0     0         1        0
0     1         0        1
0     1         1        0
1     0         0        1
1     0         1        0
1     1         0        0
1     1         1        1
```

### Rozwiązanie

```python
def wykryj_wlamanie(ruch, wibracje, godziny_otwarcia):
    """
    Implementacja złożonego systemu antywłamaniowego
    """
    wykryto_zagrozenie = ruch and wibracje  # AND - oba czujniki muszą być aktywne
    status_muzeum = not godziny_otwarcia    # NOT - muzeum zamknięte
    return wykryto_zagrozenie ^ status_muzeum  # XOR - ale nie oba na raz (możliwa awaria)

def test_systemu_antywlamanowego():
    """
    Testuje wszystkie możliwe kombinacje wejść systemu antywłamaniowego
    """
    print("\n=== Test systemu antywłamaniowego ===")
    print("Ruch  Wibracje  Otwarte  ALARM")
    print("-" * 32)
    
    for ruch in [False, True]:
        for wibracje in [False, True]:
            for otwarte in [False, True]:
                alarm = wykryj_wlamanie(ruch, wibracje, otwarte)
                print(f"{int(ruch):<5} {int(wibracje):<9} {int(otwarte):<8} {int(alarm)}")

# Test systemu antywłamaniowego
test_systemu_antywlamanowego()
```

## Kryteria oceny:
- Poprawna implementacja modułów bezpieczeństwa (6 punktów)
- Poprawne wyświetlanie panelu kontrolnego (6 punktów)
- Poprawna implementacja i testowanie systemu antywłamaniowego (8 punktów)

## Podpowiedzi:
1. Moduły bezpieczeństwa to w rzeczywistości bramki logiczne w kontekście systemu alarmowego
2. Zwróć uwagę na przypadki fałszywych alarmów - XOR pomoże je wyeliminować
3. Przy implementacji złożonego systemu antywłamaniowego, rozbij problem na mniejsze części
4. Pamiętaj o właściwym formatowaniu tabeli wyników:
```python
print(f"{'Status':^10} {'Alarm':^10}")  # wyśrodkowany tekst
print(f"{'WYŁ':<10} {'ON':>10}")       # wyrównanie do lewej/prawej
```

Powodzenia!