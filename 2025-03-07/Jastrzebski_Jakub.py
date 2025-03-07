def can_travel_to(matrix, boat_x, boat_y, target_x, target_y):

    possible_movements = [(boat_x - 1, boat_y), (boat_x, boat_y - 1), (boat_x, boat_y + 1), (boat_x + 1, boat_y), (boat_x + 2, boat_y)]

    if target_x > len(matrix) or target_x < 0 or target_y > len(matrix) or target_y < 0: return False
    if boat_x > len(matrix) or boat_x < 0 or boat_y > len(matrix) or boat_y < 0: return False
    if not matrix[target_y][target_x]: return False
    if not matrix[boat_y][boat_x]: return False

    if target_x == boat_x + 2:
        if not matrix[boat_y][boat_x + 1]: return False

    return (target_x, target_y) in possible_movements

gameMatrix = [
    [False, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, True],
    [False, True, True, False, True, True],
    [False, True, True, True, False, True],
    [False, False, False, False, False, False],
]


matrix4x4 = [
    [True, False, False, True],
    [False, True, True, True],
    [True, True, False, True],
    [True, True, True, True]
]


print(can_travel_to(matrix4x4, -1, 0, 0, 0))
