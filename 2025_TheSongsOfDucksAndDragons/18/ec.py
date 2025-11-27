import re

def solution_1(lines: list[str]):
    input = "\r\n".join(lines)
    root, plants, _ = get_plants(input)

    return get_energy(root, plants)

def solution_2(lines: list[str]):
    input = "\r\n".join(lines)
    root, plants, cases = get_plants(input)

    return sum(get_energy(root, plants, case) for case in cases)


def solution_3(lines: list[str]):
    input = "\r\n".join(lines)
    root, plants, cases = get_plants(input)

    conns = {}
    for id, plant in plants.items():
        for b, t in plant["branches"]:
            if len(plants[b]["branches"]) == 0:
                if b not in conns:
                    conns[b] = []
                conns[b].append(t)
    max_case = [1 if all([x > 0 for x in c]) else 0 for c in conns.values()]
    
    max_energy = get_energy(root, plants, max_case)

    print("Max energy = ", max_energy)
    total = 0
    for case in cases:
        energy = get_energy(root, plants, case)
        print(energy)
        if energy == 0:
            continue
        total += max_energy - energy 

    return total

def get_plants(lines):
    input = lines.split("\r\n\r\n")

    plants = {}
    cases = []

    for i, plant_datas in enumerate(input):

        data = plant_datas.split('\r\n')

        if data[0] == "Cases": break

        m_plant = re.match("Plant ([0-9]+) with thickness ([0-9]+):", data[0])
        idx = int(m_plant.groups()[0])
        thickness = int(m_plant.groups()[1])
        plants[idx] = {}
        plants[idx]["thickness"] = thickness
        plants[idx]["branches"] = []
        for branch in data[1:]:
            m_branch = re.match("- branch to Plant ([0-9]+) with thickness (-?[0-9]+)", branch)

            if m_branch:
                plants[idx]["branches"].append((int(m_branch.groups()[0]), int(m_branch.groups()[1])))

    if input[i].startswith("Cases"):
        cases = [list(map(int, line.split(' '))) for line in input[i].split('\r\n')[1:]]

    return idx, plants, cases
    
def get_energy(id, plants, case = None):
    plant = plants[id]

    if len(plant["branches"]) == 0:
        if case is None:
            return 1
        return case[id-1]

    total = 0
    for id_linked, t_linked in plant["branches"]:
        total += t_linked * get_energy(id_linked, plants, case)

    if total < plant["thickness"]:
        return 0

    return total
    
