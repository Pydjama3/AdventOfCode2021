import numpy as np

with open("values.txt") as one:
    two = [x for x in one.read().split("\n")]
    orders = two.pop(0).split(",")
    for i in range(0, two.count('')):
        two.remove('')
    three = []
    for i in two:
        three.append(i.rsplit(" "))
    for i in three:
        for y in range(0, i.count('')):
            i.remove("")
    final = []
    for i in range(0, len(three)//5):
        samp = []
        for y in range(0,5):
            samp.append(three[5*i + y])
        final.append(samp)

    model = []
    for i in range(0, len(three)//5):
        pre = []
        for i in range(0, 5):
            b = []
            for i in range(0, 5):
                b.append(0)
            pre.append(b)
        model.append(pre)

    modelB = np.zeros((len(final), 5, 5 ), dtype=int)
    finalB = final.copy()

class Result:
    def __init__(self, uncalled, last):
        self.last = uncalled
        self.uncalled = last

#Part 1

def FuncPartI(list_, orders_, model_):
    result = Result(0, 0)
    for i in orders_:
        for y in range(0,len(list_)):
            for z in range(0, len(list_[y])):
                for u in range(0, len(list_[y][z])):
                    if list_[y][z][u] == str(i):
                        model_[y][z][u] +=1 
                        for b in range(0, 5):
                            if model_[y][b][0] + model_[y][b][1] + model_[y][b][2] + model_[y][b][3] + model_[y][b][4]== 5 or model_[y][1][b] + model_[y][2][b] + model_[y][3][b] + model_[y][4][b]==4:
                                not_called = 0
                                for t in range(0, 5):
                                    for q in range(0,5):
                                        if model_[y][t][q] == 0:
                                            not_called += int(list_[y][t][q])
                                result.uncalled = not_called
                                result.last = i
                                return result

#Part2

def FuncPartII(list_, orders_, model_):
    result = Result(0, 0)
    iteration = 0
    tot = 0
    ordered = []
    for i in orders_:
        bingoed = 0
        ordered.append(int(i))
        for y in range(len(list_)):
            for z in range(len(list_[y-bingoed])):
                for u in range(len(list_[y-bingoed][z])):
                    if int(list_[y-bingoed][z][u]) == int(i):
                        model_[y-bingoed][z][u] +=1
                        model_[y-bingoed] = np.where(model_[y-bingoed]>1,1, model_[y-bingoed])
                        if max(np.sum(model_[y-bingoed], axis=1)) == 5 or max(np.sum(model_[y-bingoed], axis=0)) == 5:
                            lastL = list_.pop(y-bingoed)
                            model_ = np.delete(model_, y-bingoed, axis=0)
                            bingoed +=1
                        if len(list_)==0:
                            lastL = np.array(lastL)
                            lastL = lastL.astype(np.int_)
                            for I in range(len(lastL)):
                                for J in range(len(lastL[I])):
                                    if lastL[I][J] in ordered:
                                        lastL[I][J] = 0
                            return np.sum(lastL),  i

#Init
if __name__ == '__main__':
    part1 = FuncPartI(final, orders, model)
    part2 = FuncPartII(finalB, orders, modelB)
    print("--Part 1--", "Uncalled:", part1.uncalled, "Last:", part1.last, "Multi:", int(part1.uncalled) * int(part1.last))
    print("--Part 2--", "Uncalled:", part2[0], "Last:", part2[1], "Multi:", int(part2[0]) * int(part2[1]))