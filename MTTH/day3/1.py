t = int(input())
N = []
L = []


for i in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    N.append(n)
    L.append(l)

print("n :",N," ","l :",L)

def Ref(a):
    for i in range(len(a)):
        # print(a[i])
        Check(a[i])

def Check(b):
    default = b[0]
    for j in range(len(b)):
        if b[j] < default:
            default = b[j]
    for i in range(len(b)):
        if not CheckForDupe(b):
            if b[i] != default:
                b[i] = b[i] - 1
        else:
            print("index of ",b[i],"is",b.index(b[i]))
    print(b,default)


def CheckForDupe(c):
    for i in range(0, len(c)):    
        for j in range(i+1, len(c)): 
            if c[i] == c[j]:
                return True

Ref(L)

