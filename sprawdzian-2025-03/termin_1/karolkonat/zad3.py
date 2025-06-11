

def sprawdz_ruch(plansza, start_x, start_y, cel_x, cel_y):
    if plansza[cel_y][cel_x]:
        return False
    if (abs(start_x-cel_x) <= 1 or abs(start_y-cel_y) <= 1) and not (abs(start_x-cel_x) == 1 and abs(start_y-cel_y) == 1):
        return True
    return False


# Przykład planszy:
plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Przykład użycia:
print(sprawdz_ruch(plansza, 0, 0, 0, 1))  # True - można się poruszyć w prawo (EDIT: Zgodnie z przyjeta kolejnoscia (x,y) to jest ruch w dol)
print(sprawdz_ruch(plansza, 0, 0, 1, 0))  # True - można się poruszyć w dół (EDIT: Zgodnie z przyjeta kolejnoscia (x,y) to jest ruch w prawo)
print(sprawdz_ruch(plansza, 0, 0, 0, 2))  # False - pole (0,2) to przeszkoda (EDIT: Zgodnie z plansza, pole (0, 2) to nie przeszkoda, wiec True)
print(sprawdz_ruch(plansza, 1, 0, 2, 0))  # EDIT: False - pole (2, 0) to przeszkoda
print(sprawdz_ruch(plansza, 0, 0, 1, 1))  # False - ruch na ukos jest niedozwolony
