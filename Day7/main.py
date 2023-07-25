from statistics import median

with open("data.txt") as f:
    final = [int(x) for x in f.read().split(",")]

# Part1

def FuncPartI(final_):
    ma = max(final_)
    mi = min(final_)
    med = median(final_)
    fuel = 100000000
    for y in range(mi, ma):
        total = 0
        for i in final_:
            total += i-y if i>y else y-i
        fuel = total if total<fuel else fuel
    return fuel

# Part2

def FuncPartII(final_):
    ma = max(final_)
    mi = min(final_)
    fuel = 10000000000000000
    for y in range(mi, ma):
        total = 0
        for i in final_:
            total += (i-y)*(i-y+1)/2 if i>y else (y-i)*(y-i+1)/2
        fuel = total if total<fuel else fuel
    return fuel

# Init

if __name__ == '__main__':
    print(final)
    print("--Part 1--", "Result:", FuncPartI(final))
    print("--Part 1--", "Result:", FuncPartII(final))