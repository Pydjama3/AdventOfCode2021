from functools import cache
from collections import defaultdict

with open("data") as f:
    data = f.read().split("\n")
    final = []
    for i in data:
        a = i.split("-")
        final.append(a)

# Part 1

def FuncPartI(l):
    ref = defaultdict(list)
    for i in l:
        ref[i[0]].append(i[1]) if i[0] in ref.keys() and i[1] not in  ref[i[0]] else ref.update({i[0]:[i[1]]})
        ref[i[1]].append(i[0]) if i[1] in ref.keys() and i[0] not in  ref[i[1]] else ref.update({i[1]:[i[0]]})

    @cache
    def N_paths(point, visited):
        if point.islower():
            visited = visited.union({point})
        nb_paths = 0
        for next_point in ref[point]:
            if next_point == "end":
                nb_paths += 1
            elif next_point not in visited:
                nb_paths += N_paths(next_point, visited)
        return nb_paths
    return N_paths("start", frozenset())

# Part 2 

def FuncPartII(l):
    ref = defaultdict(list)
    for i in l:
        ref[i[0]].append(i[1]) if i[0] in ref.keys() and i[1] not in  ref[i[0]] else ref.update({i[0]:[i[1]]})
        ref[i[1]].append(i[0]) if i[1] in ref.keys() and i[0] not in  ref[i[1]] else ref.update({i[1]:[i[0]]})

    @cache
    def N_paths(point, visited, second):
        if point.islower():
            visited = visited.union({point})
        nb_paths = 0
        for next_point in ref[point]:
            if next_point == "end":
                nb_paths += 1
            elif next_point not in visited:
                nb_paths += N_paths(next_point, visited, second)
            elif next_point != "start" and second:
                nb_paths += N_paths(next_point, visited, False)
        return nb_paths
    return N_paths("start", frozenset(), True)

# Init

if __name__ == "__main__":
    print("--Part 1--", "Result:", FuncPartI(final))
    print("--Part 2--", "Result:", FuncPartII(final))