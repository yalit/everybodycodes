import functools

def solution_1(lines: list[str]):
    return sum(90// int(x) for x in lines[0].split(','))

def solution_2(lines: list[str]):
    heights = list(map(int, lines[0].split(',')))

    mult = 1
    source = []

    while any(h > 0 for h in heights):
        index = [h > 0 for h in heights].index(True) + 1 # indexed at 0 in python
        mult *= index
        source.append(index)
        for i in range(index-1, len(heights), index):
            heights[i] -= 1

    return mult, source

def solution_3(lines: list[str]):
    _, source = solution_2(lines)

    blocks = 202520252025000
    lo = 0
    hi = blocks

    while lo < hi:
        mi = (lo + hi)//2
        count = sum(mi//n for n in source)
        if count == blocks:
            break
        
        if count > blocks:
            hi = mi - 1
        else:
            lo = mi + 1

    return hi 
