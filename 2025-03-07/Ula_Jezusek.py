gameMatrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]
def can_travel_to(gameMatrix ,a, b,c, d):
    if c == a:
        if d == b + 1 or d == b - 1 :
            return(gameMatrix[c][d])
        elif d == b + 2:
            if gameMatrix[c][ b + 1] == False:
                return(False)
            else:
                return(gameMatrix[c][d])
        else:
            return(False)
    elif d == b:
        if c == a + 1 or c == a - 1:
            return(gameMatrix[c][d])
        else:
            return(False)
    else:
        return(False)

print(can_travel_to(gameMatrix,3, 2, 6, 2))
