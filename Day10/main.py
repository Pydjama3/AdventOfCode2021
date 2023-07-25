from statistics import median

with open("data.txt") as f:
    a = [x for x in f.read().split("\n")]
    final=[]
    for i in a:
        b = [x for x in i]
        final.append(b)


# Part1
def FuncPartI(list_):
    total = 0
    ref = [int(x) for x in "3 57 1197 25137".split(" ")]
    wrongs = {}
    start = list('([{<')
    end = list(')]}>')
    poped =0
    for line in range(len(list_)):
        order = []
        for i in list_[line-poped]:
            if i in start:
                order.append(i)
            elif i in end:
                if order.pop() != start[end.index(i)]:
                    wrongs[i] = wrongs[i] +1 if i in wrongs else 1
                    list_.pop(line-poped)
                    poped +=1
                    break
    for a in ref:
        total+=a*wrongs[end[ref.index(a)]]
    return total

# Part 2

def FuncPartII(list_):
    start = list('([{<')
    end = list(')]}>')
    totals = []
    for i in list_:
        total = 0
        follow = []
        for y in i:
            if y in start:
                follow.append(y)
            elif y in end:
                follow.pop()
        follow.reverse()
        for z in follow:
            total *= 5
            total += start.index(z)+1
        totals.append(total)
        print(total, follow)
    return median(totals)


# Init
if __name__ == '__main__':
    print(FuncPartI(final))
    print(FuncPartII(final))