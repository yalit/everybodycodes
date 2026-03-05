def first_phase(arr):
    moved = True 
    rounds = 0

    while moved:
        moved = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                moved = True
                arr[i] -= 1
                arr[i+1] += 1
        if moved:
            rounds += 1
    return rounds

def solution_1(lines: list[str]):
    columns = list(map(int, lines))
    print(columns)

    #1st phase
    rounds = first_phase(columns)
    print(f"Phase 1 : Round {rounds} => columns : {columns} => checksum = {checksum(columns)}")

    moved = True
    while moved and rounds < 10:
        moved = False
        for i in range(len(columns)-1):
            if columns[i] < columns[i+1]:
                moved = True
                columns[i] += 1
                columns[i+1] -= 1

        if moved:   
            rounds += 1
            print(f"Phase 2 : Round {rounds} => columns : {columns} => checksum = {checksum(columns)}")

    return checksum(columns)



def solution_2(lines: list[str]):
    columns = list(map(int, lines))

    rounds = first_phase(columns)

    moved = True
    while moved:
        moved = False
        for i in range(len(columns)-1):
            if columns[i] < columns[i+1]:
                moved = True
                columns[i] += 1
                columns[i+1] -= 1

        if moved:   
            rounds += 1

    return rounds


def solution_3(lines: list[str]):
    columns = list(map(int, lines))
    s = sum(columns)
    w = len(columns)

    delta = columns[-1] - columns[-2]
    target = s // w

    if columns[-2] > target:
        return delta + (columns[-2] - target) * 2
    else:
        return columns[-1] - target

    rounds = 0
    # no 1st phase the input is ascending
    print(f"Round {rounds} => columns : {columns} => checksum = {checksum(columns)}")
    moved = True
    while moved:
        moved = False
        for i in range(len(columns)-1):
            if columns[i] < columns[i+1]:
                moved = True
                columns[i] += 1
                columns[i+1] -= 1

        if moved:   
            rounds += 1
            print(f"Round {rounds} => columns : {columns} => checksum = {checksum(columns)}")

    return rounds
    

def checksum(cols) -> int:
    return sum(i*x for i, x in enumerate(cols, start=1))
