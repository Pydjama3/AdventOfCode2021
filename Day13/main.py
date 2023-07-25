import numpy as np

with open("data") as f:
    a = f.read().split("\n")
    for i in range(len(a)):
        if a[i] == '':
            rupt = i
            break
    points, folds = [], []
    for i in range(len(a)):
        if i<rupt:
            points.append(a[i].split(","))
        if i>rupt:
            folds.append(a[i].split(" ")[2].split("="))

# Part 1
def FuncPartI(points, fold):
    matr = np.ones((max([int(y) for _,y in points])+1, max([int(x) for x,_ in points])+1))
    for x,y in points:
        matr[int(y)][int(x)] = 0

    if fold[0] == "x":
        second = np.hsplit(matr, [int(fold[1]), int(fold[1])+1])[2]
        first = np.flip(np.hsplit(matr, [int(fold[1]), int(fold[1])+1])[0], axis=1)
    elif fold[0] == "y":
        second = np.vsplit(matr, [int(fold[1]), int(fold[1])+1])[2]
        first = np.flip(np.vsplit(matr, [int(fold[1]), int(fold[1])+1])[0], axis=0)
    for i in range(len(second) if len(second)<len(first) else len(first)):
        for y in range(len(second[i])):
            first[i][y]+=second[i][y]
    return len(np.argwhere(first<2))

# Part 2

def FuncPartII(points, folds):
    matr = np.ones((max([int(y) for _,y in points])+1, max([int(x) for x,_ in points])+1))
    for x,y in points:
        matr[int(y)][int(x)] = 0
    for fold in folds:
        if fold[0] == "x":
            second = np.hsplit(matr, [int(fold[1]), int(fold[1])+1])[2]
            first = np.flip(np.hsplit(matr, [int(fold[1]), int(fold[1])+1])[0], axis=1)
        elif fold[0] == "y":
            second = np.vsplit(matr, [int(fold[1]), int(fold[1])+1])[2]
            first = np.flip(np.vsplit(matr, [int(fold[1]), int(fold[1])+1])[0], axis=0)
        for i in range(len(second)):
            for y in range(len(second[i])):
                first[i][y]+=second[i][y]
        matr = np.where(first < 2, 0, 1)
    return np.flip(np.where(matr==0,"#","-"))

# Init
if __name__ == "__main__":
    print("--Part1--","Result:",FuncPartI(points, folds[0]))
    print()
    for p in FuncPartII(points, folds):
        print(" ".join([str(a) for a in p]))