import re


def get_count_in_line(line: str, w: str):
    m = re.findall(r"" + w, line)
    return len(m) if m else 0


def solution_1(lines: list[str]):
    words = lines[0].split(":")[1].split(",")

    return sum(get_count_in_line(lines[2], w) for w in words)


def solution_2(lines: list[str]):
    words = lines[0].split(":")[1].split(",")

    return sum(len(w) * get_count_in_line(line, w) for line in lines[2:] for w in words)


def solution_3(lines: list[str]):
    pass
