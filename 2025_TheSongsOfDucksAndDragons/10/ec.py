import functools

def solution_1(lines: list[str]):
    width = len(lines[0])
    height = len(lines)

    dragon = (0,0)
    sheeps = set()

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == 'D':
                dragon = (row, col)
            if c == 'S':
                sheeps.add((row,col))


    next = [dragon]
    visited = set()
    attacked_sheeps = 0

    for _ in range(4):
        attacked = set()
        for r, c in next:
            for dr in [2,-2, 1, -1]:
                for dc in [2,-2, 1,-1]:
                    if abs(dr) == abs(dc): continue
                    nr,nc = r+dr, c+dc
                    if (nr,nc) in visited: continue
                    if 0<=nr<height and 0<=nc<width:
                        attacked.add((nr,nc))
                        if (nr,nc) in sheeps:
                            attacked_sheeps+=1
                    visited.add((nr,nc))
            visited.add((r,c))
        next = attacked
    return attacked_sheeps

def solution_2(lines: list[str]):
    width = len(lines[0])
    height = len(lines)

    dragon = (0,0)
    sheeps = set()
    hideouts = set()

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == 'D':
                dragon = (row, col)
            if c == 'S':
                sheeps.add((row,col))
            if c == '#':
                hideouts.add((row, col))


    dragon_positions = set([dragon])
    eaten_sheeps = 0


    for _ in range(3 if width == 13 else 20):
        # dragon's turn
        turn_dragon_positions = set()
        for r, c in dragon_positions:
            for dr in [2,-2, 1, -1]:
                for dc in [2,-2, 1,-1]:
                    if abs(dr) == abs(dc): continue
                    nr,nc = r+dr, c+dc
                    if 0<=nr<height and 0<=nc<width:
                        turn_dragon_positions.add((nr,nc))
                        if (nr,nc) in sheeps and (nr,nc) not in hideouts:
                            eaten_sheeps += 1
                            sheeps.remove((nr,nc))
        dragon_positions = turn_dragon_positions

        #sheeps turn
        new_sheeps = set()
        for r,c in sheeps:
            nr, nc = r + 1, c
            if nr > height: continue
            if (nr,nc) in dragon_positions and (nr,nc) not in hideouts: 
                eaten_sheeps += 1
                continue
            new_sheeps.add((nr,nc))
        sheeps = new_sheeps

    return eaten_sheeps

def solution_3(lines: list[str]):
    width = len(lines[0])
    height = len(lines)

    DRAGON = (0,0)
    SHEEPS = []

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == 'D':
                DRAGON = (row, col)
            if c == 'S':
                SHEEPS.append((row,col))

    bottoms = [height for i in range(width)]

    for i in range(width):
        h = height - 1
        while lines[h][i] == '#':
            h -= 1

        bottoms[i] = h

    @functools.cache
    def nb_sequences(dragon, sheeps, who):
        if len(sheeps) == 0:
            return 1 

        nb_eaten = 0 

        if who == 'S':
            moved = False
            for i, (r,c) in enumerate(sheeps):
                # tentatively move the sheep
                nr = r + 1

                # outside
                if r == bottoms[c]:
                    moved = True
                # not a dragon
                elif dragon != (nr,c) or lines[nr][c] == '#':
                    nb_eaten += nb_sequences(dragon, (*sheeps[:i], (nr,c), *sheeps[i+1:]), 'D')
                    moved = True

            if not moved:
                nb_eaten += nb_sequences(dragon, sheeps, 'D')

        if who == 'D':
            r, c = dragon

            for dr in [2,-2, 1, -1]:
                for dc in [2,-2, 1,-1]:
                    if abs(dr) == abs(dc): continue
                    nr,nc = r+dr, c+dc
                    if 0<=nr<height and 0<=nc<width:
                        nb_eaten += nb_sequences((nr,nc), tuple([(sr,sc) for sr,sc in sheeps if (sr,sc) != (nr,nc) or lines[sr][sc] == '#']), 'S')

        return nb_eaten

    return nb_sequences(DRAGON, tuple(SHEEPS), 'S')


