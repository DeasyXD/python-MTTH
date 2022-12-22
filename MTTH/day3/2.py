num = int(input())

def fac(x):
    store = 1
    for i in range(x,0,-1):
        # print(i)
        store = store * i
    return store

print(fac(num))

# 5*4*3*2*1