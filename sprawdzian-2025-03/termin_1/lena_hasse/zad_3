plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def sprawdz_ruch(plansza,start_x,start_y,cel_x,cel_y):
    if 0<=cel_x<len(plansza)and 0<=cel_y<len(plansza):
        if start_x == cel_x:
            return abs(start_y - cel_y) == 1
        if start_y == cel_y:
            return abs(start_x - cel_x) == 1
        else:
            return False
    else:
        return False
print(sprawdz_ruch(plansza, 0, 0, 0, 1))  # True - można się poruszyć w prawo
print(sprawdz_ruch(plansza, 0, 0, 1, 0))  # True - można się poruszyć w dół
print(sprawdz_ruch(plansza, 0, 0, 0, 2))  # False - pole (0,2) to przeszkoda
print(sprawdz_ruch(plansza, 0, 0, 1, 1))
