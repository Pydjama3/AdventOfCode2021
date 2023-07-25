with open("data.txt") as f:
    a = [x for x in f.read().split("\n")]
    final=[]
    for i in a:
        c = i.split(" ")
        c.pop(10)
        final.append(c)

def bsplit(word):
    return [char for char in word]

def Alphabeticaly(str):
    characters = sorted(str)
    return "".join(characters)

# function to return key for any value
def get_key(val, dic):
    val = Alphabeticaly(val)
    for key, value in dic.items():
        value = Alphabeticaly(value)
        if val == value:
             return key
 
    return "Not a key"

# Part1

def FuncPartI(final_):
    dico={1:2, 4:4, 7:3, 8:7}
    total=0
    for i in final_:
        for y in range(10, 14):
            total += 1 if len(i[y]) in dico.values() else 0
    return total
        
# Part2

def FuncPartII(final_):
    total = 0
    for i in final_:
        asset = ["a","b", "c","d","e","f","g"]
        leng = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
        ref = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
        plan = {"1":"","2":"","3":"","4":"","5":"","6":"","7":""}
        #  11
        # 6  2
        #  77
        # 5  3
        #  44
        for y in range(10):
            ref[1]=i[y] if len(i[y])==2 else ref[1]
            ref[4]=i[y] if len(i[y])==4 else ref[4]
            ref[7]=i[y] if len(i[y])==3 else ref[7]
            ref[8]=i[y] if len(i[y])==7 else ref[8]
            leng[len(i[y])].append(i[y])

        # "1"
        for z in ref[7]:
            plan["1"] = z if z not in bsplit(ref[1]) else plan["1"]

        # 3
        for y in leng[5]:
            in_one = 0
            for z in y:
                in_one += 1 if z in bsplit(ref[1]) else 0
            
            if in_one == 2:
                ref[3] = y
                leng[5].pop(leng[5].index(y))
        
        # "6" and "2" and "4" and "3" and 5 and 2
        for a in leng[5]:
            in_four = 0
            for z in a:
                in_four += 1 if z in bsplit(ref[4]) else 0
            
            if in_four == 3:
                ref[5] = a
                ref[2] = leng[5][leng[5].index(a)-1]

                for y in ref[5]:
                    if y not in bsplit(ref[4]):
                        if y not in bsplit(ref[7]):
                            plan["4"] = y 
                    plan["6"] = y if y not in bsplit(ref[3]) else plan["6"]
                
                for y in ref[4]:
                    plan["2"] = y if y not in bsplit(ref[5]) else plan["2"]
                    if plan["2"] == y:
                        plan["3"] = bsplit(ref[1])[ref[1].index(y)-1]
                ex = bsplit(ref[3])
                ex.remove(plan["1"])
                ex.remove(plan["2"])
                ex.remove(plan["3"])
                ex.remove(plan["4"])
                plan["7"] = ex[0]
                asset.remove(plan["1"])
                asset.remove(plan["2"])
                asset.remove(plan["3"])
                asset.remove(plan["4"])
                asset.remove(plan["6"])
                asset.remove(plan["7"])
                plan["5"]=asset[0]
                for t in leng[6]:
                    if plan["1"] in bsplit(t) and plan["2"] in bsplit(t) and plan["3"] in bsplit(t) and plan["4"] in bsplit(t) and plan["5"] in bsplit(t) and plan["6"] in bsplit(t):
                        ref[0] = t
                    elif plan["1"] in bsplit(t) and plan["2"] in bsplit(t) and plan["3"] in bsplit(t) and plan["4"] in bsplit(t) and plan["7"] in bsplit(t) and plan["6"] in bsplit(t):
                        ref[9] = t
                    else:
                        ref[6]=t
        tex = ""
        for y in range(10, 14):
            tex = tex+str(get_key(i[y], ref))
        total += int(tex)
    return total

# Init

if __name__ == "__main__":
    print("--Part 1--", "Result:",FuncPartI(final))
    print("--Part 2--", "Result:",FuncPartII(final))