
def solution_1(lines: list[str]):
    feed = tuple([int(x) for x in lines[0].split(',')])

    r = (0,0)

    for _ in range(3):
        r = cycle(r, feed, 10)

    return r

def solution_2(lines: list[str]):
    start = tuple([int(x) for x in lines[0].split(',')])

    engraved = 0
    for x in range(0,1010, 10):
        for y in range(0,1010, 10):
            pos = add(start, (x,y))
            v = (0,0)
            c = 0
            while c < 100 and abs(v[0]) <= 1000000 and abs(v[1]) <= 1000000:
                v = cycle(v, pos, 100000)
                c += 1
            
            if c >= 100 and  abs(v[0]) <= 1000000 and abs(v[1]) <= 1000000:
                engraved +=1

    return engraved


def solution_3(lines: list[str]):
    start = tuple([int(x) for x in lines[0].split(',')])

    engraved = 0
    for x in range(1001):
        for y in range(1001):
            pos = add(start, (x,y))
            v = (0,0)
            c = 0
            while c < 100 and abs(v[0]) <= 1000000 and abs(v[1]) <= 1000000:
                v = cycle(v, pos, 100000)
                c += 1
            
            if c >= 100 and  abs(v[0]) <= 1000000 and abs(v[1]) <= 1000000:
                engraved +=1

    return engraved


def add(A, B):
    return (A[0]+B[0], A[1]+B[1])

def mul(A, B):
    return ((A[0]*B[0])-(A[1]*B[1]), (A[0]*B[1])+(A[1]*B[0]))

def div(A, B):
    return (int(A[0]/B[0]), int(A[1]/B[1]))

def cycle(r, feed, divisor):
    r = mul(r,r)
    r = div(r,(divisor, divisor))
    r = add(r,feed)

    return r
