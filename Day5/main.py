import numpy as np

with open("data.txt") as raw:
    readable = [x for x in raw.read().split("\n")]
    two =[]
    for i in readable:
        two.append(i.split(","))
    final=[]
    for i in two:
        e = []
        e.append(int(i[0]))
        a = i[1].split(" -> ")
        e.append(int(a[0]))
        e.append(int(a[1]))
        e.append(int(i[2]))
        final.append(e)

#Part1

def FuncPartI(data):
    grid = np.zeros((1000, 1000))
    total = 0
    for x1,y1,x2,y2 in data:
        if x1 == x2:
            if y1>y2: y1,y2=y2,y1
            for y in range(y1, y2+1):
                grid[y][x1] +=1
        elif y1 == y2:
            if x1>x2: x1, x2 = x2, x1
            for y in range(x1, x2+1):
                grid[y1][y] +=1
    for i in grid:
        for y in i:
            if y > 1:
                total+=1
    return total

#Part2

def FuncPartII(data):
    mat = {}
    total = 0
    for x1,y1,x2,y2 in data:
        if x1==x2:
            if y1>y2: y1,y2=y2,y1
            for y in range(y1,y2+1):
                mat[(x1,y)]=mat.get((x1,y),0)+1
        elif y1==y2:
            if x1>x2: x1,x2=x2,x1
            for x in range(x1,x2+1):
                mat[(x,y1)]=mat.get((x,y1),0)+1
        else:
            if x1>x2: x1,x2, y1,y2 = x2,x1, y2,y1
            for x in range(x1,x2+1):
                if y2>y1: y = y1+(x-x1)
                else:     y = y1-(x-x1)
                mat[(x,y)]=mat.get((x,y),0)+1
    total = sum(v>1 for v in mat.values())
    return total

#Init

if __name__ == "__main__":
    print("--Part 1--", "Result:", FuncPartI(final))
    print("--Part 2--", "Result:", FuncPartII(final))
