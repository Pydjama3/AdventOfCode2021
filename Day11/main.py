import numpy as np

with open("data") as f:
    a = [x for x in f.read().split("\n")]
    final = []
    for i in a:
        b = [int(y) for y in i]
        final.append(b)

# Part 1

def FuncPartI(a, times):
    total = 0
    A = np.array(a)
    snapshots = []

    def fill_entry(i,j):
        if 0 <= i < 10 and 0 <= j < 10 :
            A[i][j] += 1


    for z in range(times):
        spoted = []
        for y in range(len(A)):
            for x in range(len(A[y])):
                A[y][x] += 1
        while len(np.argwhere(A>9)) != 0:
            for i,j in np.argwhere(A>9):
                if [i,j] not in spoted:
                    fill_entry(i-1,j)  
                    fill_entry(i,j-1)  
                    fill_entry(i,j+1) 
                    fill_entry(i+1,j)
                    fill_entry(i-1,j-1)  
                    fill_entry(i-1,j+1)
                    fill_entry(i+1,j+1)
                    fill_entry(i+1,j-1)
                    spoted.append([i,j])
                    total += 1
            for y,x in spoted:
                A[y][x] = 0
    return total

# Part 2

def FuncPartII(a):
    times = 0
    A = np.array(a)
    snapshots = []

    def fill_entry(i,j):
        if 0 <= i < 10 and 0 <= j < 10 :
            A[i][j] += 1


    while np.count_nonzero(A) != 0:
        spoted = []
        for y in range(len(A)):
            for x in range(len(A[y])):
                A[y][x] += 1
        while len(np.argwhere(A>9)) != 0:
            for i,j in np.argwhere(A>9):
                if [i,j] not in spoted:
                    fill_entry(i-1,j)  
                    fill_entry(i,j-1)  
                    fill_entry(i,j+1) 
                    fill_entry(i+1,j)
                    fill_entry(i-1,j-1)  
                    fill_entry(i-1,j+1)
                    fill_entry(i+1,j+1)
                    fill_entry(i+1,j-1)
                    spoted.append([i,j])
            for y,x in spoted:
                A[y][x] = 0
        times+=1
    return times

# Init
if __name__ == "__main__":
    print("--Part 1--","Result:",FuncPartI(final, 100))
    print("--Part 2--","Result:",FuncPartII(final))