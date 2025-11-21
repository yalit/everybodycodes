from collections import deque

def solution_1(lines: list[str]):
    return len(get_exploded_count(lines, [(0,0)]))

def solution_2(lines: list[str]):
    return len(get_exploded_count(lines, [(0,0), (len(lines) - 1, len(lines[0]) - 1)]))


def solution_3(lines: list[str]):
    exploded = set()


    for _ in range(3):
        best_start = set()
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                if (row,col) in exploded: continue
                s_exploded = get_exploded_count(lines, [(row,col)], exploded)
                if len(s_exploded) > len(best_start):
                    best_start = set(s_exploded)

        exploded |= best_start

    return len(exploded)



def get_exploded_count(grid, starting_points, already_exploded = set()):
    height = len(grid)
    width = len(grid[0])
    to_explode = deque(starting_points)
    exploded = set(already_exploded)

    while to_explode:
        r,c = to_explode.popleft()

        strength = grid[r][c]
        if (r,c) in exploded: continue

        for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= height or nc < 0 or nc >= width: continue
            if grid[nr][nc] > strength: continue
            if (nr,nc) not in exploded:
                to_explode.append((nr,nc))
        
        exploded.add((r,c))

    return exploded
