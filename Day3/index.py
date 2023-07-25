with open("data.txt") as raw:
    readable = [x for x in raw.read().split("\n")]

class ResultI:
    def __init__(self, gamma, epsilon):
        self.gamma = ""
        self.epsilon = ""

class ResultII:
    def __init__(self, oxygen, co2):
        self.oxygen = 0
        self.co2 = 0

#Part 1

def FuncPartI(list):
    result = ResultI("", "")
    for i in range(0, len(list[0])):
        zero = 0
        one = 0

        for a in list:
            if a[i] == "0":
                zero +=1
            else:
                one +=1

        if zero > one:
            result.gamma = result.gamma + "0"
            result.epsilon = result.epsilon + "1"

        else:
            result.gamma = result.gamma + "1"
            result.epsilon = result.epsilon + "0"
            
    result.gamma = int(result.gamma, 2)
    result.epsilon = int(result.epsilon, 2)
    return result

#Part2

def FuncPartII(list):
    result = ResultII(0, 0)
    oxygen = list
    co2 = list
    for i in range(0, len(list[0])):
        zeros = 0
        ones = 0
        zero = []
        one = []
        for y in oxygen:
            if y[i] == "0":
                zeros += 1
                zero.append(y)
            else:
                ones += 1
                one.append(y)
            

        if ones > zeros:
            oxygen = one
        elif ones == zeros:
            oxygen = one
        else:
            oxygen = zero

        zeros = 0
        ones = 0
        zero = []
        one = []
        if len(co2)>1:
            for y in co2:
                if y[i] == "0":
                    zeros += 1
                    zero.append(y)
                else:
                    ones += 1
                    one.append(y)

            if ones < zeros:
                co2 = one
            elif ones == zeros:
                co2 = zero
            else:
                co2 = zero

    result.co2 = int(co2[0], 2)
    result.oxygen = int(oxygen[0], 2)
    return result


#Result


if __name__ == "__main__":
    print("--Part 1--", "Result:", "Gamma:", FuncPartI(readable).gamma, "Epsilon:", FuncPartI(readable).epsilon, "Multi:", FuncPartI(readable).gamma*FuncPartI(readable).epsilon)
    print("--Part 2--", "Result:", "Oxygen", FuncPartII(readable).oxygen, "CO2", FuncPartII(readable).co2, "Multi:", FuncPartII(readable).oxygen*FuncPartII(readable).co2)