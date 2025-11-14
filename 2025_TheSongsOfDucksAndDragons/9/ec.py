from collections import deque

def solution_1(lines: list[str]):
    scales = [line[2:] for line in lines]

    for i in range(len(scales)):
        for j in range(i+1, len(scales)):
            for k in range(len(scales)):
                if i == k or j == k: continue
                p_1 = scales[i]
                p_2 = scales[j]
                child = scales[k]
                if all(a == c or b == c for a, b, c in zip(p_1, p_2, child)):
                    return sum(x == y for x,y in zip(p_1, child)) * sum(x == y for x,y in zip(p_2, child))

def solution_2(lines: list[str]):
    scales = [line.split(':')[1] for line in lines]

    degrees = 0
    for i in range(len(scales)):
        for j in range(i+1, len(scales)):
            for k in range(len(scales)):
                if i == k or j == k: continue
                p_1 = scales[i]
                p_2 = scales[j]
                child = scales[k]
                if all(a == c or b == c for a, b, c in zip(p_1, p_2, child)):
                    similarity_a = sum(x == y for x, y in zip(p_1, child))
                    similarity_b = sum(x == y for x, y in zip(p_2, child))
                    degrees += similarity_a * similarity_b

    return degrees

def solution_3(lines: list[str]):
    scales = [line.split(':')[1] for line in lines]

    childs = {}
    parents = {}

    for i in range(len(scales)):
        for j in range(i+1, len(scales)):
            for k in range(len(scales)):
                if i == k or j == k: continue
                p_1 = scales[i]
                p_2 = scales[j]
                child = scales[k]
                for a, b, c in zip(p_1, p_2, child):
                    if not (a == c or b == c):
                        break
                else:
                    childs[k] = (i,j)
                    if i not in parents:
                        parents[i] = set()
                    parents[i].add(k)
                    if j not in parents:
                        parents[j] = set() 
                    parents[j].add(k)

    population = set(list(range(len(scales))))

    max_family = [] 
    while len(population) > 0:
        n = list(population)[0]
        to_visit = deque([((n,), (n,))])
        visited = set()

        while to_visit:
            nodes, degrees = to_visit.popleft();

            additional_nodes = set()

            for n in nodes:
                if n in childs:
                    for parent in childs[n]:
                        if parent in visited or parent not in population:
                            continue
                        additional_nodes.add(parent)
                if n in parents:
                    for child in parents[n]:
                        if child in visited or child not in population:
                            continue
                        additional_nodes.add(child)

                visited.add(n)
            if len(additional_nodes) > 0:
                to_visit.append((tuple(additional_nodes), degrees + tuple(additional_nodes)))

            if len(to_visit) == 0:
                members = list(set(degrees))
                max_family = max_family if len(max_family) > len(members) else members

        population -= visited

    return sum(x+1 for x in max_family) 



