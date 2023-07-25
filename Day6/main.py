with open("data.txt") as f:
    final = [int(x) for x in f.read().split(",")]

#Part1

def FuncPartI(final_):
    a = {}
    for y in range(0, 80):
        a[(y)] = final_
        for i in range(0,len(final_)):
            if final_[i] == 0:
                final_.append(8)
                final_[i] = 6
            else:
                final_[i] -= 1
    return len(final_)

#Part2

def FuncPartII(final_):
    dico = {}
    for y in final_:
        dico[y] = dico[y]+1 if y in dico else 1

    final_ = dico;
    for i in range(0,256):
        dico = {}
        for Lfish in final_:
            fishT = Lfish-1
            if fishT == -1:
                dico[8]=final_[Lfish]
                dico[6]=final_[Lfish]+dico[6] if 6 in dico else final_[Lfish]
            else:
                dico[fishT] = final_[Lfish] + dico[fishT] if fishT in dico else final_[Lfish]
        final_ = dico
    return sum(final_.values())


if __name__ == "__main__":
    print("--Part2--", "Result:",FuncPartII(final))
    print("--Part1--", "Result:",FuncPartI(final))