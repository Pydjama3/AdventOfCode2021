with open("values.txt") as raw:
    readable = [int(x) for x in raw.read().split()]

# Part 1

def FuncPartI(list):
    total = 0
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            total +=1
    return total

# Part 2

def FuncPartII(list):
    total = 0
    for x in range(0, len(list)-3):
        current = list[x] + list[x+1] + list[x+2]
        after = list[x+1] + list[x+2] + list[x+3]
        if current < after:
            total +=1
    return total

#Results

print("--Part 1--", "Result:", FuncPartI(readable))
print('--Part 2--', "Result:", FuncPartII(readable))