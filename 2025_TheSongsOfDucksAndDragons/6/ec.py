def solution_1(lines: list[str]):
    cap_a = 0
    n = 0

    for c in lines[0]:
        if c == 'A':
            cap_a += 1

        if c == 'a':
            n += cap_a

    return n

def solution_2(lines: list[str]):
    letters = {}

    for c in lines[0]:
        if c not in letters:
            letters[c] = 0

        if c.isupper():
            letters[c]+=1

        if c.islower():
            letters[c] += 0 if c.upper() not in letters else letters[c.upper()]

    return sum([n for x,n in letters.items() if x.islower()])

def solution_3(lines: list[str]):
    mul = 1000
    dist = 1000

    selection = lines[0] * mul
    caps = {'A': [], 'B': [], 'C': []}
    lows = {'a': 0, 'b': 0, 'c': 0}

    for i in range(len(selection) + dist):
        # trim caps indexes
        for letter,ids in caps.items():
            limit = i - (2*dist)
            a = 0
            while a < len(ids) and ids[a] < limit:
                a += 1
            caps[letter] = ids[max(0,a):]


        if i < len(selection) and selection[i].isupper():
            caps[selection[i]].append(i)

        if i < dist:
            continue

        l = selection[i - dist]
        if l.isupper():
            continue

        lows[l] += len(caps[l.upper()])


    print(lows)
    return sum(lows.values())
