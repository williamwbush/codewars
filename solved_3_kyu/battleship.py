# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

def validate_battlefield(field):
    import numpy as np
    from functools import reduce

    def validate_ship(ship_size, field):
        ship_count = 0
        k = 0

        while k < 2:
            for i in range(len(field)):
                is_ship = True
                if ship_count == (5 - ship_size):
                    break
                for j in range(len(field[i]) - ship_size + 1):
                    if ship_count == (5 - ship_size):
                        break
                    if reduce(lambda x,y: x * y, [field[i][j+x] for x in range(ship_size)]) == 1:
                        if j < len(field) - ship_size:
                            if field[i][j+ship_size] == 1:
                                is_ship = False
                        if j != 0:
                            if field[i][j-1] == 1:
                                is_ship = False
                        if i != 0:
                            if sum(field[i-1][j:j+ship_size]) != 0:
                                is_ship = False
                        if i != len(field) - 1:
                            if sum(field[i+1][j:j+ship_size]) != 0:
                                is_ship = False
                        if i != 0 and j != 0:
                            if field[i-1][j-1] == 1:
                                is_ship = False 
                        if i != 0 and j < len(field) - 1:
                            if field[i-1][j+1] == 1:
                                is_ship = False
                        if i < len(field) - 1 and j != 0:
                            if field[i+1][j-1] == 1:
                                is_ship = False
                        if i < len(field) - 1 and j < len(field) - 1:
                            if field[i+1][j+1] == 1:
                                is_ship = False
                    else:
                        is_ship = False
                    if is_ship == True:
                        ship_count += 1
                        field[i][j:j+ship_size] = [0 for n in range(ship_size)]
                    is_ship = True
            k += 1
            field = np.rot90(field)
        if ship_count < (5 - ship_size):
            field = []
        return field

    for n in range(1,5):
        field = validate_ship(n, field)
        if field == []:
            return False

    for row in field:
        if 1 in row:
            return False
        
    return True

battleField = [[0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

print(validate_battlefield(battleField))