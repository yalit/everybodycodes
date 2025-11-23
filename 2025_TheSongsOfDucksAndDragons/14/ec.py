
def solution_1(lines: list[str]):
    tiles, width, height = set_tiles(lines)

    total = 0
    for _ in range(10):
        new_tiles = set()

        for row in range(height):
            for col in range(width):
                neighbours = get_neighbours(tiles, row,col, width, height)

                if (row, col) in tiles and len(neighbours) %2 == 1:
                    new_tiles.add((row,col))
                if (row,col) not in tiles and len(neighbours) % 2 == 0:
                    new_tiles.add((row,col))

        total += len(new_tiles)       
        tiles = set(new_tiles)

    return total

def solution_2(lines: list[str]):
    tiles, width, height = set_tiles(lines)

    total = 0
    for _ in range(2025):
        new_tiles = set()

        for row in range(height):
            for col in range(width):
                neighbours = get_neighbours(tiles, row,col, width, height)

                if (row, col) in tiles and len(neighbours) %2 == 1:
                    new_tiles.add((row,col))
                if (row,col) not in tiles and len(neighbours) % 2 == 0:
                    new_tiles.add((row,col))

        total += len(new_tiles)       
        tiles = set(new_tiles)

    return total


def solution_3(lines: list[str]):
    pattern, _, _ = set_tiles(lines)

    tiles = set()
    width = 34
    height = 34

    turns = {}
    patterns = []
    
    def get_center():
        return set([(row-13, col-13) for row, col in tiles if 13 <= row < 21 and 13 <= col < 21])

    i = 0
    while tuple(tiles) not in turns:
        turns[tuple(tiles)] = i
        tiles = get_next_turn(tiles, width, height)
        i += 1
        if get_center() == pattern:
            patterns.append((i, len(tiles)))
    r = i - turns[tuple(tiles)]
    mult = 1000000000 // r
    delta = 1000000000 - (mult * r) 
    total = mult * sum(x for _,x in patterns)

    return total + sum(x  for a,x in patterns if a < delta)
    
    
    

def display_grid(tiles, width, height):
    for row in range(height):
        r = ['.' if (row, col) not in tiles else '#' for col in range(width)]
        print("".join(r))


def get_next_turn(tiles, width, height):
    new_tiles = set()

    for row in range(height):
        for col in range(width):
            neighbours = get_neighbours(tiles, row, col, width, height)

            if (row, col) in tiles and len(neighbours) %2 == 1:
                new_tiles.add((row,col))
            if (row,col) not in tiles and len(neighbours) % 2 == 0:
                new_tiles.add((row,col))

    return new_tiles

def set_tiles(lines):
    tiles = set([(row,col) for row, line in enumerate(lines) for col, v in enumerate(line) if v == '#'])
    width = len(lines[0])
    height = len(lines)
    return tiles, width, height

def get_neighbours(tiles, row, col, width, height):
    n = []
    for dr, dc in [(-1,-1), (-1, 1), (1, -1), (1, 1)]:
        nr, nc = row+dr, col+dc
        if (nr,nc) in tiles:
            n.append((nr,nc))

    return n
