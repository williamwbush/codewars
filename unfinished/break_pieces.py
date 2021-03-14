

shape = '\n'.join(["+------------+",
                   "|            |",
                   "|            |",
                   "|            |",
                   "+------+-----+",
                   "|      |     |",
                   "|      |     |",
                   "+------+-----+"])

def break_pieces(shape):
    shape = shape.split('\n')
    coords = []
    for i, row in enumerate(shape):
        for j, char in enumerate(row):
            if char == " ":
                coords.append([i,j])

    rows = [[]]
    for i, coord in enumerate(coords[1:]):
        if coord[1] - 1 == coords[i][1]:
            rows[-1].append(coords[i])
            rows[-1].append(coord)
        else:
            rows.append([coord])
    print(rows)
    for row in rows:
        for i in range(len(row) - 1):
            if row[i] == row[i+1]:
                del row[i]
    print(rows)


break_pieces(shape)

