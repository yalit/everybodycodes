def solution_1(lines: list[str]):
    nodes = [int(x) for x in lines[0].split(',')]
    edges = list(zip(nodes, nodes[1:]))
    size = max(nodes)

    return len([x for x in edges if abs(x[0]-x[1]) == int(size/2)])

def solution_2(lines: list[str]):
    steps = [int(x) for x in lines[0].split(',')]
    edges = list(zip(steps, steps[1:]))
    size = max(steps)
    nodes = list(range(1,size+1))
    
    knots = 0

    for i, edge in enumerate(edges):
        s,f = sorted(edge)
        dist = abs(f-s)
        between = set([x for x in nodes if s < x < f])
        outside = set([x for x in nodes if x < s or x > f])

        for ns,nf in edges[:i]:
            if (ns in between and nf in outside) or (ns in outside and nf in between):
                knots += 1
    return knots

def solution_3(lines: list[str]):
    steps = [int(x) for x in lines[0].split(',')]
    edges = list(zip(steps, steps[1:]))
    size = max(steps)
    nodes = list(range(1,size+1))

    max_cuts = 0
    for s in range(1, size - 1):
        for f in range(s + 2, size + 1):
            cuts = 0
            dist = abs(f-s)
            between = set([x for x in nodes if s < x < f])
            outside = set([x for x in nodes if x < s or x > f])

            for ns, nf in edges:
                if (ns == s and nf == f) or (nf ==s and ns ==f):
                    cuts +=1
                    continue

                if (ns in between and nf in outside) or (ns in outside and nf in between):
                    cuts += 1

            max_cuts = max(max_cuts, cuts)

    return max_cuts
