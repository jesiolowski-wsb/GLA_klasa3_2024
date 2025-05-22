# zdobyte punkty: 3/6

# ✅ Poprawne sprawdzenie czy ruch jest tylko w kierunku góra, dół, lewo, prawo (nie na ukos)
# ✅ Poprawne sprawdzenie czy ruch jest tylko o jedno pole
# ❌ Brak sprawdzenia granic planszy
# ❌ Brak sprawdzenia czy punkty startowy i docelowy to puste pola (wartość 0)
# ❌ Logika weryfikacji ruchu jest niepełna

plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
def sprawdz_ruch(plansza, start_x, start_y, cel_x, cel_y):
    #Dodaj sprawdzenie granic planszy oraz czy punkty to puste pola

    if start_x == cel_x:
        if start_y == cel_y + 1:
            return True
        elif start_y == cel_y - 1:
            return True
        else:
            return False
    elif start_y == cel_y:
        if start_x == cel_x + 1:
            return True
        elif start_x == cel_x - 1:
            return True
        else:
            return False
    else:
        return False
