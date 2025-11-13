
def solution_1(lines: list[str]):
    names = lines[0].split(',')
    directions = [(d[0], int("".join(d[1:]))) for d in lines[2].split(',')]

    max_position = len(names) -1
    position = 0
    for d, n in directions:
        if d == "R":
            position = min(position+n, max_position)
        else:
            position = max(position-n, 0)

    return names[position]

def solution_2(lines: list[str]):
    names = lines[0].split(',')
    directions = [(d[0], int("".join(d[1:]))) for d in lines[2].split(',')]

    position = 0
    for d, n in directions:
        if d == "R":
            position =  (position+n) % len(names)
        else:
            position =  (position-n) % len(names)

    return names[position]

def solution_3(lines: list[str]):
    names = lines[0].split(',')
    directions = [(d[0], int("".join(d[1:]))) for d in lines[2].split(',')]

    for d, n in directions:
        if d == "R":
            position =  n % len(names)
        else:
            position =  (len(names) - n) % len(names)
        temp = names[0]
        names[0] = names[position]
        names[position] = temp

    return names[0]
