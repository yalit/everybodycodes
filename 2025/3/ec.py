def solution_1(lines: list[str]):
    return sum(list(set([int(x) for x in lines[0].split(',')])))

def solution_2(lines: list[str]):
    return sum(sorted(list(set([int(x) for x in lines[0].split(',')])))[:20])

def solution_3(lines: list[str]):
    crates = [int(x) for x in lines[0].split(',')]

    volumes = {}
    for c in crates:
        if c not in volumes:
            volumes[c] = 0
        volumes[c]+=1

    return max(volumes.values())

