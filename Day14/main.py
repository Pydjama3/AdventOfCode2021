import numpy as np
from functools import cache
from collections import Counter

with open("data") as f:
    a = [i for i in f.read().split("\n")]
    initial = a.pop(0)
    a.pop(0)
    final=[]
    for i in a:
        b = i.split(" -> ")
        final.append(b)
    ref = {}
    for i in final:
        ref[i[0]]=(i[1])

# Part 1

def FuncPartI(init, ref):
    init = [x for x in init]
    for a in range(10):
        insert = []
        for i in range(len(init)-1):
            pair = init[i]+init[i+1]
            insert.append(ref[pair])
        add = 0
        for i in range(len(insert)):
            init.insert(i+1+add,insert[i])
            add+=1
    counts = []
    for i in ref.values():
        counts.append(len(np.argwhere(np.array(init)==i)))
    return max(counts)-min(counts)

# Part 2

def FuncPartII(init, ref):
    Mtime = 40
    @cache
    def new_count(pair, times):
        if times == Mtime or pair not  in ref:
            return Counter()
        times += 1
        merge = ref[pair]
        new_counter = Counter(merge)
        new_counter.update(new_count(merge + pair[1], times))
        new_counter.update(new_count(pair[0] + merge, times))
        return new_counter
    
    counter = Counter(init)
    for first, second in zip(init, init[1:]):
        counter.update(new_count(first + second, 0))
    return max(counter.values())-min(counter.values())

# Init
if __name__ == "__main__":
    print("--Part 1--","Result:",FuncPartI(initial, ref))
    print("--Part 2--","Result:",FuncPartII(initial, ref))