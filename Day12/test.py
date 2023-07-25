from collections import defaultdict
from functools import cache

def get_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")
    cave_maps = []
    for d in data:
        cave_map = defaultdict(list)
        for line in d.splitlines():
            a, b = line.split("-")
            cave_map[a].append(b)
            cave_map[b].append(a)
        cave_maps.append(cave_map)
    return cave_maps

def count_paths(cave_map, single_small_twice):
    # Use functools.cache to eliminate unnecessary recursive calls.
    @cache
    def count_next_paths(origin, seen, twice):
        if origin.islower():
            seen = seen.union({origin})
            print(seen)
        n_paths = 0
        for target in cave_map[origin]:
            if target == "end":
                n_paths += 1
            elif target not in seen:
                n_paths += count_next_paths(target, seen, twice)
            elif target != "start" and twice:
                n_paths += count_next_paths(target, seen, False)
        return n_paths
    return count_next_paths("start", frozenset(), single_small_twice)

print(get_data("data"))
print(count_paths(get_data("data")[0], False))