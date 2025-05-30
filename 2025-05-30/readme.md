
# Programowanie strukturalne i obiektowe w Pythonie

## 🔹 Programowanie strukturalne
- Opiera się na funkcjach i kolejności wykonywania instrukcji.
- Dobre dla prostych problemów.

Przykład:
```python
def utworz_konto(imie, saldo_poczatkowe):
    return {"imie": imie, "saldo": saldo_poczatkowe}

def wplac(konto, kwota):
    konto["saldo"] += kwota
    return konto

moje_konto = utworz_konto("Anna", 1000)
wplac(moje_konto, 500)
print(f"{moje_konto['imie']} ma {moje_konto['saldo']} zł")

```

---

## 🔸 Programowanie obiektowe
- Wykorzystuje klasy i obiekty.
- Pozwala lepiej organizować kod w większych projektach.

Przykład:
```python
class KontoBankowe:
    def __init__(self, imie, saldo):
        self.imie = imie
        self.saldo = saldo
        
    def wplac(self, kwota):
        self.saldo += kwota

moje_konto = KontoBankowe("Anna", 1000)
moje_konto.wplac(500)
print(f"{moje_konto.imie} ma {moje_konto.saldo} zł")
```

---

## 🧪 Zadanie:
1. Napisz program do zarządzania magazynem produktów:
    - Dodawanie produktu (nazwa, ilość)
    - Zwiększanie/zmniejszanie ilości
    - Wyświetlenie magazynu
2. Najpierw wersja strukturalna, potem obiektowa.

```python
# przyklad uzycia wersji strukturalnej
dodaj_produkt("jabłka", 50)
dodaj_produkt("banany", 30)
zmien_ilosc("jabłka", -10)  # sprzedaż
pokaz_magazyn()
```

---

## 🧠 Podsumowanie:
| Cecha | Strukturalne | Obiektowe |
|-------|--------------|-----------|
| Styl | Funkcyjny | Klasy, obiekty |
| Skala | Proste programy | Większe projekty |
