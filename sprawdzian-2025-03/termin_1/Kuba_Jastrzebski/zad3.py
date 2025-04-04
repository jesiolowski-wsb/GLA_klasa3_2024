def sprawdz_ruch(plansza, x1, y1, x2, y2):
    if plansza[x1][y1]: return False
    if plansza[x2][y2]: return False
    if x2 in (x1-1, x1, x1+1) and y2 in (y1-1, y1, y1+1) and x2 >= 0 and y2 >= 0 and (x2, y2) != (x1, y1) and (x2+y2)-(x1+y1) in [1, -1]: return True
    return False


plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]


print(sprawdz_ruch(plansza, 0, 0, 0, 1))
print(sprawdz_ruch(plansza, 0, 0, 1, 0))
print(sprawdz_ruch(plansza, 0, 0, 0, 2))
print(sprawdz_ruch(plansza, 0, 0, 1, 1))