gameMatrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]
gameMatrix[3][2]=2
szukane=2
def find_element_index(gameMatrix, szukane):
    for i, row in enumerate(gameMatrix):
        if szukane in row:
            x=row.index(szukane)
            return (i, x)

l=find_element_index(gameMatrix,szukane)
kupa=int(l[0])
dupa=int(l[1])
print(kupa,dupa)
def can_travel_to(kupa,dupa):
    ruchy=[]
    if gameMatrix[kupa-1][dupa-1]== True:
        ruchy.append([kupa-1,dupa-1])
    if gameMatrix[kupa][dupa-1]== True:
        ruchy.append([kupa,dupa-1])
    if gameMatrix[kupa+1][dupa-1]== True:
        ruchy.append([kupa+1,dupa-1])
    if gameMatrix[kupa -1 ][ dupa ] == True:
        ruchy.append([kupa + 1, dupa - 1])
    if gameMatrix[kupa + 1][ dupa] == True:
        ruchy.append([kupa + 1, dupa - 1])
    if gameMatrix[kupa -1 ][ dupa+1 ] == True:
        ruchy.append([kupa - 1, dupa + 1])
    if gameMatrix[kupa  ][ dupa +1 ] == True:
        ruchy.append([kupa , dupa + 1])
    if gameMatrix[kupa +1 ][ dupa + 1] == True:
        ruchy.append([kupa + 1, dupa - 1])
    return (ruchy)
print("pozycje na które mozna sie ruszyc to",can_travel_to(kupa,dupa))
