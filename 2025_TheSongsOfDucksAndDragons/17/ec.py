def solution_1(tiles: list[str]):
    volcano = ()

    for row in range(len(tiles)):
        for col in range(len(tiles[0])):
            if tiles[row][col] == '@':
                volcano = (row, col)
    
    touched = set()

    for r in range(1, 11):
        for dr in range(-1 * r, r+1):
            for dc in range(-1*r, r+1):
                if dr == 0 and dc == 0: continue

                if (-1*dr)**2 + (-1*dc)**2 <= r**2:
                    touched.add((volcano[0]+dr, volcano[1]+dc))

    return sum(int(tiles[row][col]) for row, col in touched)


def solution_2(lines: list[str]):
    volcano = ()
    tiles = {}
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '@':
                volcano = (row, col)
            else:
                tiles[(row,col)] = int(lines[row][col])

    max_burned = (0, 0)
    r = 1

    while any(v != 0 for v in tiles.values()):
        touched = set()
        for dr in range(-1 * r, r+1):
            for dc in range(-1*r, r+1):
                if dr == 0 and dc == 0: continue

                row, col = volcano[0]+dr, volcano[1]+dc

                if (row,col) not in tiles: continue
                if tiles[(row, col)] == 0: continue

                if (-1*dr)**2 + (-1*dc)**2 <= r**2:
                    touched.add((row, col))
        
        s = sum(int(tiles[(row,col)]) for row, col in touched)
        if s > max_burned[0]:
            max_burned = (s, r)

        for row, col in touched:
            tiles[(row, col)] = 0

        r += 1

    return max_burned[0]*max_burned[1]

def solution_3(lines: list[str]):
    pass

