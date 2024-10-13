
# Zadania z list, krotek oraz słowników

## Zadanie 1: Operacje na listach i krotkach

Napisz program, który wykona następujące operacje:
1. Utwórz listę imion: `["Jan", "Anna", "Piotr", "Kasia", "Tomasz"]`.
2. Zmień trzecie imię na "Marcin".
3. Dodaj na koniec listy nowe imię "Ewa".
4. Usuń z listy pierwsze imię.
5. Przekształć listę na krotkę i wyświetl zawartość krotki.
6. Zmień trzeci element na imię "Bob"

**Rozwiązanie:**
```python
# Tworzenie listy imion
imiona = ["Jan", "Anna", "Piotr", "Kasia", "Tomasz"]

# Zmiana trzeciego imienia na "Marcin"
imiona[2] = "Marcin"

# Dodanie imienia "Ewa" na koniec listy
imiona.append("Ewa")

# Usunięcie pierwszego imienia
imiona.pop(0)

# Przekształcenie listy na krotkę
krotka_imiona = tuple(imiona)

# Wyświetlenie krotki
print(krotka_imiona)
```

---

## Zadanie 2: Praca ze słownikami

Napisz program, który wykona następujące operacje:
1. Utwórz słownik zawierający dane o dwóch uczniach:
   ```python
   uczniowie = {
       "uczen1": {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 17},
       "uczen2": {"imie": "Anna", "nazwisko": "Nowak", "wiek": 16}
   }
   ```
2. Dodaj trzeciego ucznia do słownika o danych: `"imie": "Tomasz", "nazwisko": "Wiśniewski", "wiek": 18`.
3. Zwiększ wiek pierwszego ucznia o 1.
4. Usuń z listy drugiego ucznia.
5. Wyświetl wynikowy słownik.

**Rozwiązanie:**
```python
# Tworzenie słownika z dwoma uczniami
uczniowie = {
    "uczen1": {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 17},
    "uczen2": {"imie": "Anna", "nazwisko": "Nowak", "wiek": 16}
}

# Dodanie trzeciego ucznia
uczniowie["uczen3"] = {"imie": "Tomasz", "nazwisko": "Wiśniewski", "wiek": 18}

# Zwiększenie wieku pierwszego ucznia o 1
uczniowie["uczen1"]["wiek"] += 1

# Usunięcie drugiego ucznia
del uczniowie["uczen2"]

# Wyświetlenie wynikowego słownika
print(uczniowie)
```
