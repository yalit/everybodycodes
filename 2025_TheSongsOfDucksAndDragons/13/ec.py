from collections import deque

def solution_1(lines: list[str]):
    wheel = deque([1]) 

    for i, v in enumerate(lines):
        if i % 2 == 0:
            wheel.append(int(v))
        else:
            wheel.appendleft(int(v))

    index = wheel.index(1)
    wheel = list(wheel)[index:] + list(wheel)[:index]

    return wheel[2025 % len(wheel)]

def solution_2(lines: list[str]):
    wheel = deque([1]) 

    for i, v in enumerate(lines):
        f, t = list(map(int, v.split('-')))

        if i % 2 == 0:
            for x in range(f, t+1):
                wheel.append(x)
        else:
            for x in range(f, t+1):
                wheel.appendleft(x)

    index = wheel.index(1)
    wheel = list(wheel)[index:] + list(wheel)[:index]

    return wheel[20252025 % len(wheel)]


def solution_3(lines: list[str]):
    wheel = deque([1]) 

    s = 1
    for i, v in enumerate(lines):
        f, t = list(map(int, v.split('-')))

        if i % 2 == 0:
            wheel.append((f,t))
        else:
            wheel.appendleft((t,f))
        s += t - f + 1

    index = wheel.index(1)
    wheel = list(wheel)[index:] + list(wheel)[:index]

    mod = 202520252025 % s

    d = 0
    for f,t in wheel[1:]:
        d += (abs(t-f) + 1)
        if d > mod:
            if f < t:
                return t - (d-mod)
            return t + (d-mod)

