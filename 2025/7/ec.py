def solution_1(lines: list[str]):
    words = lines[0].split(',')

    rules= {}
    for rule in lines[2:]:
        k, next = rule.split(' > ')
        rules[k] = set(next.split(','))


    for word in words:
        if is_allowed(word, rules):
            return word
    return None


def solution_2(lines: list[str]):
    words = lines[0].split(',')

    rules= {}
    for rule in lines[2:]:
        k, next = rule.split(' > ')
        rules[k] = set(next.split(','))


    count = 0
    for idx,word in enumerate(words, start=1):
        if is_allowed(word, rules):
            count += idx
    return count 


def solution_3(lines: list[str]):
    words = lines[0].split(',')

    rules= {}
    for rule in lines[2:]:
        k, next = rule.split(' > ')
        rules[k] = set(next.split(','))


    possibilities = set()

    for word in words:
        if not is_allowed(word, rules):
            continue

        to_visit =  [word]
        visited = set()

        while to_visit:
            next = to_visit.pop()

            if 7 <= len(next) <= 11:
                possibilities.add(next)

            if len(next) == 11:
                continue

            if next[-1] not in rules:
                continue

            for n in rules[next[-1]]:
                to_visit.append(next+n)

            visited.add(next)

    return len(possibilities)


def is_allowed(word, rules) -> bool:
    for i in range(len(word)-1):
        c = word[i]
        n = word[i+1]
        if n not in rules[c]:
            break
    else:
        return True
    
    return False
