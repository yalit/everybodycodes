import os
import sys


def import_module(name):
    mod = __import__(name)
    components = name.split(".")
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


runType = sys.argv[1]
day = sys.argv[2]

sys.path.append(os.path.abspath(os.path.join("..")))

dayScript = import_module(f"{day}.ec")

if runType == "test":
    print(f"Running day {day} --- TEST")
    file1 = open(f"{day}/input_test_1.txt", "r")
    file2 = open(f"{day}/input_test_2.txt", "r")
    file3 = open(f"{day}/input_test_3.txt", "r")
else:
    print(f"Running day {day}")
    file1 = open(f"{day}/input_1.txt", "r")
    file2 = open(f"{day}/input_2.txt", "r")
    file3 = open(f"{day}/input_3.txt", "r")


if len(sys.argv) == 3 or sys.argv[3] == "1":
    lines = [x.strip("\n") for x in file1.readlines()]
    print("Solution part 1 : ", dayScript.solution_1(lines))

if len(sys.argv) == 3 or sys.argv[3] == "2":
    lines = [x.strip("\n") for x in file2.readlines()]
    print("Solution part 2 : ", dayScript.solution_2(lines))

if len(sys.argv) == 3 or sys.argv[3] == "3":
    lines = [x.strip("\n") for x in file3.readlines()]
    print("Solution part 3 : ", dayScript.solution_3(lines))
