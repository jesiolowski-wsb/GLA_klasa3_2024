# zdobyte punkty: 4/6

# ✅ Sprawdza czy punkty startowy i docelowy to puste pola
# ✅ Funkcja zwraca wartość logiczną
# ✅ strasznie zwarte rozwiązanie
# ❌ zwartośc rozwiąznia zmniejsza jego czytelność
# ❌ Pozwala na ruch po przekątnej (ukos), co jest niezgodne z wymaganiami
# ❌ Brak sprawdzenia górnej granicy planszy
# ❌ Warunek (x2+y2)-(x1+y1) in [1, -1] nie gwarantuje ruchu tylko w pionie lub poziomie

def sprawdz_ruch(plansza, x1, y1, x2, y2):
    if plansza[x1][y1]: return False
    if plansza[x2][y2]: return False
    if x2 in (x1-1, x1, x1+1) and y2 in (y1-1, y1, y1+1) and x2 >= 0 and y2 >= 0 and (x2, y2) != (x1, y1) and (x2+y2)-(x1+y1) in [1, -1]: return True
    return False

# czasem czytelność rozwiązania może ułatwiać debug np
# def sprawdz_ruch(plansza, x1, y1, x2, y2):
    # # Sprawdzenie granic planszy
    # if (x1 < 0 or x1 >= len(plansza) or
    #         y1 < 0 or y1 >= len(plansza[0]) or
    #         x2 < 0 or x2 >= len(plansza) or
    #         y2 < 0 or y2 >= len(plansza[0])):
    #     return False
    #
    # # Sprawdzenie czy pola są puste
    # if plansza[x1][y1] == 1 or plansza[x2][y2] == 1:
    #     return False
    #
    # # Sprawdzenie czy ruch jest dozwolony (tylko pion lub poziom, o jedno pole)
    # dozwolone_ruchy = [
    #     (x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)
    # ]
    # return (x2, y2) in dozwolone_ruchy


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