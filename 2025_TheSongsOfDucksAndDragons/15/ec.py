from collections import deque

def solution_1(lines: list[str]):
    start = (0,0)
    walls, target = get_walls(lines[0], start)
    return a_star(start, target, walls)



def solution_2(lines: list[str]):
    return solution_1(lines)


def solution_3(lines: list[str]):
    return solution_1(lines)


def a_star(start, goal, walls):
    to_visit = set([start])
    visited = set()

    g = {start: 0}
    h = {start: dist(start, goal)}
    f = {start: g[start]+h[start]}

    while to_visit:
        node = sorted(list(to_visit), key=lambda x: f[x])[0]

        if node == goal:
            return g[node]

        visited.add(node)
        to_visit.remove(node)

        for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0)]:
            next = (node[0]+dr, node[1]+dc)

            if next in visited or next in walls:
                continue

            g_next = g[node]+1
            h_next = dist(next, goal)
            f_next = g_next+h_next

            if next not in to_visit:
                g[next] = g_next
                h[next] = h_next
                f[next] = f_next
                to_visit.add(next)

            elif g_next < g[next]:
                g[next] = g_next
                f[next] = g_next + h[next]

    return None
                

def dist(start, goal):
    return abs(goal[0]-start[0]) + abs(goal[1]-start[1])

def get_walls(path, origin):
    walls = set()
    s=origin
    direction = (-1,0)

    changes = {(-1,0) : {'R': (0,1), 'L': (0,-1)}, (0,1): {'R':(1,0), 'L': (-1,0)}, (1,0): {'R':(0,-1), 'L': (0,1)}, (0,-1):{'R':(-1,0), 'L': (1,0)}}
    for e in path.split(','):
        d = e[0]
        n = int(e[1:])
        direction = changes[direction][d]
        for _ in range(n):
            s = (s[0]+direction[0], s[1]+direction[1])
            walls.add(s)

    walls.remove(s)
    return walls, s

def display_walls(grid, start, goal, visited):
    walls = set(grid)
    walls.add(start)
    walls.add(goal)

    min_row = min(x for x,_ in walls)
    min_col = min(y for _,y in walls)
    max_row = max(x for x,_ in walls)
    max_col = max(y for _,y in walls)


    grid = []
    for r in range(min_row, max_row+1):
        grid.append(['#' if (r, c) in walls else ('X' if (r,c) in visited else ' ') for c in range(min_col, max_col+1)])

    grid[start[0]-min_row][start[1]-min_col] = 'S'
    grid[goal[0]-min_row][goal[1]-min_col] = 'E'

    for row in grid:
        print("".join(row))


