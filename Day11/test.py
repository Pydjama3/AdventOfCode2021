import numpy as np


def FuncPartI(a, times):
    total = 0
    A = np.array(a)   # Initialize an array of zeros.
    snapshots = []          # Copies of the matrix after each change.

    def fill_entry(i,j):
        if 0 <= i < 10 and 0 <= j < 10 :
            A[i][j] += 1


    # Do the reaction until all entries are 1.
    for z in range(times):
        spoted = []
        for y in range(len(A)):
            for x in range(len(A[y])):
                A[y][x] += 1
        # Find the indices of nonzero elements.
        while len(np.argwhere(A>9)) != 0:
            for i,j in np.argwhere(A>9):
                if [i,j] not in spoted:
                    fill_entry(i-1,j)  # Up
                    fill_entry(i,j-1)  # Left
                    fill_entry(i,j+1)  # Right
                    fill_entry(i+1,j)
                    fill_entry(i-1,j-1)  # Down
                    fill_entry(i-1,j+1)
                    fill_entry(i+1,j+1)
                    fill_entry(i+1,j-1)
                    spoted.append([i,j])
                    total += 1
            for y,x in spoted:
                A[y][x] = 0
        print(spoted)
        print(A)
        print()
    return total


with open("data") as f:
    a = [x for x in f.read().split("\n")]
    final = []
    for i in a:
        b = [int(y) for y in i]
        final.append(b)
    print(FuncPartI(final, 100))