with open("data") as f:
    a = [x for x in f.read().split(" ")]
    a.pop(0)
    a.pop(0)
    x = (int(a[0].split("..")[0].replace("x=", "")), int(a[0].split("..")[1].replace(",","")))
    y = (int(a[1].split("..")[0].replace("y=", "")), int(a[1].split("..")[1].replace(",","")))

# Part 1
def FuncPartI(targetX, targetY):
    def VelocityTry(x, y):
        pos = [0,0]
        m = pos[1]
        while pos[0]<=targetX[1] and pos[1] >= targetY[0]:
            pos[0] += x
            pos[1] += y
            x-=1 if x>0 and x!=0 else -1
            y-=1
            m = pos[1] if pos[1]>m else m
            if targetX[0]<=pos[0]<=targetX[1] and targetY[0]<=pos[1]<=targetY[1]:
                return "Possible", m
        return "Impossible"
    poss = []
    for i in range(9999):
        for j in range(9999):
            result = VelocityTry(i, j)
            if len(result) == 2:
                poss.append(result[1])
    return max(poss)



# Init 

if __name__ == "__main__":
    print(FuncPartI(x,y))