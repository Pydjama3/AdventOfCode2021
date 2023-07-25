with open("data.txt") as raw:
    readable = [x for x in raw.read().split("\n")]

class Result:
    def __init__(self, x, y):
        self.x = 0
        self.z = 0

#Part 1

def InputToPosI(list):
    result = Result(0,0)
    for i in list:
        a = i.split(' ')
        if a[0] == "forward":
            result.x += int(a[1])
        elif a[0] == "up":
            result.z -= int(a[1])
        else:
            result.z += int(a[1])
    return result

# Part 2
def InputToPosII(list):
    result = Result(0, 0)
    aim = 0
    for i in list:
        a = i.split(' ')
        if a[0] == "forward":
            result.x += int(a[1])
            result.z += aim * int(a[1])
        elif a[0] == "up":
            aim -= int(a[1])
        else:
            aim += int(a[1])
        print(a[0], a[1], aim)
    return result

#Init
if __name__ == "__main__":
    print("--Part 1--", "Result:", "X:", InputToPosI(readable).x,"Z:", InputToPosI(readable).z,"Multi:",  InputToPosI(readable).x*InputToPosI(readable).z)
    print("--Part 2--", "Result:", "X:", InputToPosII(readable).x,"Z:", InputToPosII(readable).z,"Multi:",  InputToPosII(readable).x*InputToPosII(readable).z)