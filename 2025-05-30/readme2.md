## Strukturalnie vs Obiektowo + Podstawy klas

2 główne **paradygmaty** (sposoby myślenia o kodzie). Dwa najważniejsze to:
- **Programowanie strukturalne** - organizuje kod wokół funkcji
- **Programowanie obiektowe** - organizuje kod wokół obiektów

### Programowanie strukturalne

#### Czym jest?
Programowanie strukturalne to podejście, gdzie program dzielimy na mniejsze, logiczne bloki - **funkcje**. Każda funkcja ma konkretne zadanie do wykonania.

#### Główne zasady:
- Kod pisany "od góry do dołu" w logicznej kolejności
- Podział programu na funkcje
- Jasna struktura: sekwencja, wybór (if/else), pętla

#### Przykład - System ocen (strukturalnie)

```python
def dodaj_ocene(lista_ocen, nowa_ocena):
    lista_ocen.append(nowa_ocena)
    return lista_ocen

def oblicz_srednia(lista_ocen):
    if len(lista_ocen) == 0:
        return 0
    return sum(lista_ocen) / len(lista_ocen)

def sprawdz_zaliczenie(srednia):
    return srednia >= 3.0

def wyswietl_wynik(imie, srednia, zaliczyl):
    status = "ZALICZYŁ" if zaliczyl else "NIE ZALICZYŁ"
    print(f"{imie}: średnia {srednia:.2f} - {status}")

# Główny kod
imie_ucznia = "Jan Kowalski"
oceny_ucznia = []

dodaj_ocene(oceny_ucznia, 4)
dodaj_ocene(oceny_ucznia, 3)
dodaj_ocene(oceny_ucznia, 5)

srednia = oblicz_srednia(oceny_ucznia)
zaliczyl = sprawdz_zaliczenie(srednia)
wyswietl_wynik(imie_ucznia, srednia, zaliczyl)
```

### Programowanie obiektowe - podstawy

#### Czym jest?
Programowanie obiektowe to podejście, gdzie organizujemy kod wokół **obiektów** - połączenia danych (atrybutów) i funkcji (metod), które na tych danych operują.

#### Kluczowe pojęcia:

**Klasa** - szablon opisujący jak ma wyglądać obiekt (jak przepis na ciasto)
**Obiekt** - konkretna instancja klasy (jak ciasto upieczone według przepisu)
**Atrybuty** - dane przechowywane w obiekcie (np. imię ucznia)
**Metody** - funkcje należące do obiektu

#### Przykład - System ocen (obiektowo)

```python
class Uczen:    
    def __init__(self, imie):
        """Konstruktor - tworzy nowego ucznia"""
        self.imie = imie
        self.oceny = []
    
    def dodaj_ocene(self, ocena):
        if 1 <= ocena <= 6:
            self.oceny.append(ocena)
        else:
            print("Ocena musi być z zakresu 1-6!")
    
    def oblicz_srednia(self):
        if len(self.oceny) == 0:
            return 0
        return sum(self.oceny) / len(self.oceny)
    
    def czy_zaliczyl(self):
        return self.oblicz_srednia() >= 3.0
    
    def wyswietl_wynik(self):
        srednia = self.oblicz_srednia()
        status = "ZALICZYŁ" if self.czy_zaliczyl() else "NIE ZALICZYŁ"
        print(f"{self.imie}: średnia {srednia:.2f} - {status}")

# Użycie
jan = Uczen("Jan Kowalski")
anna = Uczen("Anna Nowak")

jan.dodaj_ocene(4)
jan.dodaj_ocene(3)
jan.dodaj_ocene(5)

anna.dodaj_ocene(5)
anna.dodaj_ocene(6)

jan.wyswietl_wynik()
anna.wyswietl_wynik()
```

### Schemat: Klasa vs Obiekt

```
    KLASA Uczen               OBIEKTY
    ┌─────────────────┐      ┌─────────────────┐
    │ Atrybuty:       │      │ jan:            │
    │ - imie          │ ──→  │ imie = "Jan"    │
    │ - oceny         │      │ oceny = [4,3,5] │
    │                 │      └─────────────────┘
    │ Metody:         │      
    │ - dodaj_ocene() │      ┌─────────────────┐
    │ - oblicz_srednia│ ──→  │ anna:           │
    │ - wyswietl_wynik│      │ imie = "Anna"   │
    └─────────────────┘      │ oceny = [5,6]   │
                             └─────────────────┘
```

### 🎯 ZADANIA DO WYKONANIA

**Zadanie 1**: Stwórz klasę `Samochod` z atrybutami: marka, model, przebieg. Dodaj metody: `jedz(kilometry)`, `sprawdz_przebieg()`.

**Zadanie 2**: Stwórz klasę `Kalkulator` z metodami: `dodaj()`, `odejmij()`, `pomnoz()`, `podziel()`.

---

## Enkapsulacja - ukrywanie danych

### Czym jest enkapsulacja?
Enkapsulacja to **ukrywanie wewnętrznych szczegółów** obiektu przed światem zewnętrznym. Użytkownik może korzystać tylko z publicznych metod, ale nie ma bezpośredniego dostępu do danych.

### Po co ukrywać dane?
- **Bezpieczeństwo** - zapobiegamy przypadkowemu zepsuciu danych
- **Kontrola** - wymuszamy prawidłowy sposób używania obiektu
- **Łatwiejsze zmiany** - możemy zmienić implementację bez wpływu na resztę kodu

### Poziomy dostępu w Pythonie:

#### 1. Publiczne (brak oznaczeń) - każdy ma dostęp
```python
self.imie = "Jan"  # Każdy może czytać i zmieniać
```

#### 2. Chronione (jedno podkreślenie `_`) - sygnał ostrzegawczy
```python
self._oceny = []  # Sygnał: "nie ruszaj tego bezpośrednio!"
```

#### 3. Prywatne (dwa podkreślenia `__`) - naprawdę ukryte
```python
self.__pin = "1234"  # Bardzo trudno dostępne z zewnątrz
```

### Przykład - Konto bankowe

```python
class KontoBankowe:
    def __init__(self, wlasciciel, saldo_poczatkowe):
        # PUBLICZNE - każdy może to zobaczyć
        self.wlasciciel = wlasciciel
        
        # CHRONIONE - nie ruszaj bezpośrednio!
        self._numer_konta = "123456789"
        self._historia = []
        
        # PRYWATNE - naprawdę ukryte!
        self.__saldo = saldo_poczatkowe
        self.__pin = "1234"
    
    # Jedyny sposób dostępu do prywatnych danych
    def wplac(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
            self._historia.append(f"Wpłata: {kwota}")
            print(f"Wpłacono {kwota} zł")
        else:
            print("Kwota musi być dodatnia!")
    
    def wyplac(self, kwota, pin):
        if pin != self.__pin:
            print("Błędny PIN!")
            return
        
        if 0 < kwota <= self.__saldo:
            self.__saldo -= kwota
            self._historia.append(f"Wypłata: {kwota}")
            print(f"Wypłacono {kwota} zł")
        else:
            print("Niewystarczające środki!")
    
    def sprawdz_saldo(self, pin):
        if pin != self.__pin:
            print("Błędny PIN!")
            return None
        return self.__saldo

# PRAWIDŁOWE UŻYCIE
konto = KontoBankowe("Jan Kowalski", 1000)
konto.wplac(500)
print(f"Saldo: {konto.sprawdz_saldo('1234')}")

# NIEPRAWIDŁOWE - łamanie enkapsulacji
# konto._saldo = 999999  # ŹLE! Można to zrobić, ale nie powinno się!
```

### Porównanie: Co można robić z różnymi poziomami

```python
konto = KontoBankowe("Jan Kowalski", 1000)

# PUBLICZNE - bez problemu
print(konto.wlasciciel)        # ✓ Działa
konto.wlasciciel = "Anna"      # ✓ Można zmienić

# CHRONIONE - można, ale nie powinno się
print(konto._numer_konta)      # ⚠️ Działa, ale to sygnał "nie rób tego"
konto._historia.append("test") # ⚠️ Można, ale łamie zasady

# PRYWATNE - Python blokuje dostęp
# print(konto.__saldo)         # ❌ BŁĄD! AttributeError
# konto.__pin = "9999"         # ❌ BŁĄD! Nie można zmienić

# PRAWIDŁOWY dostęp do prywatnych danych - przez metody
konto.wplac(500)                           # ✓ Kontrolowane
print(f"Saldo: {konto.sprawdz_saldo('1234')}")  # ✓ Bezpieczne
```

### 🎯 ZADANIA DO WYKONANIA 

**Zadanie 3**: Popraw klasę `Samochod` z poprzedniej lekcji - ukryj przebieg i dodaj metodę `dodaj_kilometry()` z walidacją (tylko dodatnie wartości).

**Zadanie 4**: Stwórz klasę `Telefon` z ukrytym numerem PIN i metodami: `odblokuj(pin)`, `zablokuj()`, `dzwon(numer)` (tylko gdy odblokowany).

---

## Dziedziczenie - klasy potomne

### Czym jest dziedziczenie?
Dziedziczenie pozwala tworzyć nowe klasy **na podstawie już istniejących**. Klasa potomna dziedziczy wszystkie atrybuty i metody z klasy rodzica, ale może je rozszerzyć lub zmienić.

### Terminologia:
- **Klasa rodzic** (bazowa) - klasa, z której dziedziczymy
- **Klasa potomek** (pochodna) - klasa dziedzicząca

### Co dziedziczy klasa potomek?
1. Wszystkie atrybuty klasy rodzica
2. Wszystkie metody klasy rodzica
3. Może dodać nowe atrybuty i metody
4. Może zmienić (nadpisać) metody rodzica

### Przykład - System szkolny

```python
# KLASA RODZIC - wspólne cechy wszystkich osób w szkole
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}, mam {self.wiek} lat")
    
    def wejdz_do_szkoly(self):
        print(f"{self.imie} wszedł do szkoły")

# KLASA POTOMEK - Uczeń dziedziczy wszystko z Osoba + dodaje swoje
class Uczen(Osoba):  # ← Dziedziczenie!
    def __init__(self, imie, nazwisko, wiek, klasa):
        # Wywołujemy konstruktor rodzica
        super().__init__(imie, nazwisko, wiek)
        # Dodajemy nowe atrybuty
        self.klasa = klasa
        self.oceny = []
    
    # NADPISUJEMY metodę z rodzica
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}, uczeń klasy {self.klasa}")
    
    # DODAJEMY nowe metody
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

# KLASA POTOMEK - Nauczyciel też dziedziczy z Osoba
class Nauczyciel(Osoba):
    def __init__(self, imie, nazwisko, wiek, przedmiot):
        super().__init__(imie, nazwisko, wiek)
        self.przedmiot = przedmiot
        self._pensja = 5000  # Prywatne!
    
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}, nauczyciel {self.przedmiot}")
    
    def sprawdz_pensje(self):
        return self._pensja

# Użycie
uczen = Uczen("Jan", "Kowalski", 16, "3A")
nauczyciel = Nauczyciel("Anna", "Nowak", 35, "matematyka")

# Wszyscy mogą używać metod z klasy Osoba
uczen.wejdz_do_szkoly()        # Odziedziczona metoda
nauczyciel.wejdz_do_szkoly()   # Odziedziczona metoda

# Każdy ma swoją wersję przedstaw_sie()
uczen.przedstaw_sie()      # "Jestem Jan Kowalski, uczeń klasy 3A"
nauczyciel.przedstaw_sie() # "Jestem Anna Nowak, nauczyciel matematyka"

# Tylko uczeń może dodawać oceny
uczen.dodaj_ocene(5)
```

### Schemat dziedziczenia:

```
           Osoba
      ┌─────┴─────┐
      │           │
    Uczen    Nauczyciel
              │
          Dyrektor
```

### Wielopoziomowe dziedziczenie

```python
# Dyrektor dziedziczy po Nauczycielu (który dziedziczy po Osoba)
class Dyrektor(Nauczyciel):
    def __init__(self, imie, nazwisko, wiek, lata_stazu):
        super().__init__(imie, nazwisko, wiek, "zarządzanie")
        self.lata_stazu = lata_stazu
        self._pensja = 8000  # Wyższa pensja
    
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}, dyrektor ({self.lata_stazu} lat stażu)")
    
    def zwolaj_rade(self):
        print("Zwołuję radę pedagogiczną!")

dyrektor = Dyrektor("Piotr", "Wiśniewski", 50, 20)

# Dyrektor może wszystko co Nauczyciel i Osoba:
dyrektor.wejdz_do_szkoly()    # Z Osoba
dyrektor.sprawdz_pensje()     # Z Nauczyciel  
dyrektor.zwolaj_rade()        # Własna metoda
```

### 🎯 ZADANIA DO WYKONANIA 

**Zadanie 5**: Stwórz klasę `Pojazd` z atrybutami: marka, rok_produkcji, metoda `jedz()`. Następnie stwórz klasy potomne: `Samochod` (dodaj: liczba_drzwi) i `Motocykl` (dodaj: typ_silnika).

**Zadanie 6**: Rozszerz system szkolny - dodaj klasę `Wychowawca` dziedziczącą po `Nauczyciel` z metodą `sprawdz_frekwencje()`.

---

## Porównanie podejść - Podsumowanie

| Aspekt | Programowanie strukturalne | Programowanie obiektowe |
|--------|---------------------------|------------------------|
| **Organizacja** | Funkcje + dane oddzielnie | Dane i metody razem |
| **Trudność** | Łatwiejsze na początku | Trudniejsze na początku |
| **Małe programy** | Wystarczające ✓ | Może być przesadą |
| **Duże projekty** | Trudne do zarządzania | Łatwiejsze ✓ |
| **Ponowne użycie** | Ograniczone | Lepsze ✓ |
| **Zespołowa praca** | Trudniejsza | Łatwiejsza ✓ |

## Kiedy używać którego podejścia?

### Użyj programowania strukturalnego gdy:
- Piszesz małe, proste programy (do 200 linii)
- Rozwiązujesz jednorazowy problem
- Program ma prostą, liniową logikę

### Użyj programowania obiektowego gdy:
- Piszesz większy program (>200 linii)
- Program będzie rozwijany przez dłuższy czas
- Pracujesz w zespole
- Modelujesz rzeczywiste obiekty (osoby, pojazdy, produkty)

## Częste błędy

❌ **Tworzenie klasy (gdy wystarczy funkcja)**
```python
# ŹLE - niepotrzebna klasa
class Dodawanie:
    def dodaj(self, a, b):
        return a + b

# DOBRZE - wystarczy funkcja
def dodaj(a, b):
    return a + b
```

❌ **Mylenie klasy z obiektem**
```python
# ŹLE - próba wywołania metody na klasie
Uczen.dodaj_ocene(5)

# DOBRZE - wywołanie na obiekcie
jan = Uczen("Jan", "Kowalski", 16, "3A")
jan.dodaj_ocene(5)
```

❌ **Robienie wszystkiego publicznym**
```python
# ŹLE - brak enkapsulacji
class Konto:
    def __init__(self):
        self.saldo = 1000  # Każdy może to zmienić!

# LEPIEJ - kontrola dostępu
class Konto:
    def __init__(self):
        self._saldo = 1000  # Sygnał: nie zmieniaj bezpośrednio
```

---

**Dobry programista powinien znać oba podejścia i umieć wybrać odpowiednie do sytuacji!**
