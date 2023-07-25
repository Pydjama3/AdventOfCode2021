import cv2
import numpy as np

with open("data.txt") as f:
    a = [x for x in f.read().split("\n")]
    final = []
    for i in a:
        b = [int(x) for x in i]
        final.append(b)
    finalII = final
    for i in final:
        i.insert(0,9)
        i.append(9)
    final.insert(0,[9] * len(final[0]))
    final.append([9] * len(final[0]))

# Part1

def FuncPartI(list_):
    total = 0
    for i in range(1,len(list_)-1):
        for z in range(1,len(list_[i])-1):
            if list_[i][z]<min([list_[i-1][z],list_[i+1][z],list_[i][z-1],list_[i][z+1]]):
                total += list_[i][z]+1 
    return total

# Part 2

def FuncPartII(list_):
    contrasted = np.where(np.array(list_) < 9, 255, 0).astype(np.uint8)
    _, _, stats, _ = cv2.connectedComponentsWithStats(contrasted, connectivity=4)
    ordered = sorted([i[-1] for i in stats[1:]])[-3:]
    return ordered[0]*ordered[1] * ordered[2]

# Init

if __name__ == "__main__":
    print("--Part 1--", "Result:",FuncPartI(final))
    print("--Part 2--", "Result:",FuncPartII(finalII))