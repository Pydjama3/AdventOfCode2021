import numpy as np

with open("data") as f:
    a = [x for x in f.read().split("\n")]
    final = []
    for i in a:
        b = [x for x in i]
        final.append(b)

# Part 1
def FuncPartI(l):
    l = np.array(l)
    steps = 0
    while True:
        last = l.copy()
        easts = np.argwhere(l=='>')
        for y, x in easts:
            if x == len(l[0])-1:
                if l[y][0]==".":
                    l[y][x]="."
                    l[y][0]=">"   
            else:
                if l[y][x+1]==".":
                    l[y][x]="."
                    l[y][x+1]=">"
        souths = np.argwhere(l=="v")
        for y,x in souths:
            if y == len(l)-1:
                if l[0][x]==".":
                    l[y][x]="."
                    l[0][x]="v" 
            else:
                if l[y+1][x]==".":
                    l[y][x]="."
                    l[y+1][x]="v"
        steps +=1
        if np.array_equal(l,last):
            return(steps)

# Init
if __name__ == "__main__":
    print(FuncPartI(final))
