gameMatrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]


def czy_ruch_wykonalny(current_x, current_y, chosen_x, chosen_y):
    if current_y == chosen_y:
        return (chosen_x-current_x==2) or (chosen_x-current_x==-1) or (chosen_x-current_x==1)
    elif current_x==current_x:
        return abs(current_y-chosen_y)==1
    else: return False



def can_travel_to(gameMatrix,current_x,current_y,chosen_x,chosen_y):
    if czy_ruch_wykonalny(current_x,current_y,chosen_x,chosen_y)==True or None:
        return gameMatrix[chosen_y][chosen_x]
    if gameMatrix[current_y][current_x]==False:
        return False
    else:
        return False

print(can_travel_to(gameMatrix, 3, 2, 2, 2)) # True, ruch jest dopuszczalny
print(can_travel_to(gameMatrix, 3, 2, 3, 4)) # False, nie można przepłynąć przez ląd
print(can_travel_to(gameMatrix, 3, 2, 3, 3)) # False, nie można przepłynąć przez ląd
print(can_travel_to(gameMatrix, 3, 2, 3, 5)) # False, nie można przepłynąć przez ląd + zbyt daleko
print(can_travel_to(gameMatrix, 3, 2, 6, 2)) # False, poza dopuszczalnym zakresem
print()
print(can_travel_to(gameMatrix, 3, 2, 20, 16)) #sprawdzalam co sie dzieje poza plansza
