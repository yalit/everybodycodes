import math

def solution_1(lines: list[str]):
    mills = [int(x) for x in lines]

    ratios = get_ratios(mills)

    n = 2025
    for r in ratios:
        n *= r
    return int(n)

def solution_2(lines: list[str]):
    mills = [int(x) for x in lines]
    ratios = get_ratios(mills)

    target = 10000000000000
    for r in reversed(ratios):
        target = target/r

    return math.ceil(target)

def solution_3(lines: list[str]):
    mills = [(int(x),int(x)) if not '|' in x else (int(x.split('|')[0]), int(x.split('|')[1])) for x in lines]

    ratios = []
    first = mills[0]

    for i in range(1, len(mills)):
        second = mills[i]
        ratios.append(first[1]/second[0])
        first = second

    n = 100
    for r in ratios:
        n *= r
    return int(n)

def get_ratios(mills):
    ratios = []
    first = mills[0]

    for i in range(1, len(mills)):
        ratios.append(first/mills[i])
        first = mills[i]

    return ratios
