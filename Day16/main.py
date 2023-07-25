import binascii

with open("data") as d:
    a = bin(int(d.read(), base=16))[2:]
    a = "00"+a

# Part 1

def FuncPartI(data):
    total = 0
    A=0
    while True:
        start = A
        version= data[A:A+3]
        total += int(version, 2)
        A+=3
        dID = data[A:A+3]
        print(A, dID)
        A+=3
        if dID == "100":
            con = data[A]
            A+=4
            while con == "1":
                A+=5
                con = data[A]
            A=((((A-start)//4)+1)*4)+start
            print(A)
        if A>len(data):
            break

            



# Init 

if __name__ == "__main__":
    FuncPartI("110100101111111000101000110100101111111000101000")