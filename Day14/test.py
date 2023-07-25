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

def polymerize(template, rules, max_steps):
    @cache
    def count(pair, step):
        if step == max_steps or pair not in rules:
            return Counter()
        step += 1
        new_element = rules[pair]
        new_counter = Counter(new_element)
        new_counter.update(count(pair[0] + new_element, step))
        new_counter.update(count(new_element + pair[1], step))
        return new_counter

    counter = Counter(template)
    for left, right in zip(template, template[1:]):
        counter.update(count(left + right, 0))
    return counter

print(polymerize(initial, ref, 40))