def solution_1(lines: list[str]):
    return strength(lines[0])[0]


def solution_2(lines: list[str]):
    strengths = [strength(line)[0] for line in lines]

    return max(strengths) - min(strengths)


def solution_3(lines: list[str]):
    strengths = list(reversed(sorted([strength(line) for line in lines])))

    n = 0
    for i, s in enumerate(strengths, start=1):
        n+=(i)*s[-1]

    for s in strengths:
        print(s)
    return n


def strength(line) -> int:
    elements = [int(x) for x in line.split(":")[1].split(",")]

    spines = []

    for x in elements:
        for spine in spines:
            if x < spine[1] and spine[0] is None:
                spine[0] = x
                break
            if x > spine[1] and spine[2] is None:
                spine[2] = x
                break
        else:
            spines.append([None,x,None])

    
    return int("".join([str(s[1]) for s in spines])), *tuple([int("".join(["" if x is None else str(x) for x in s])) for s in spines]), int(line.split(':')[0])

