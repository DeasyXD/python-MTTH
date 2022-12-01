w = 0 
n = 0
r = 0

while True:
    w = int(input("w : ")) + r
    if w < 0:
        break
    elif w >= 500 and w <= 1000:
        n = 1
        r = 0
    elif w > 1000:
        n = w // 1000
        r = w % 1000
    else:
        n = 0
        r = 0
    print("n =",n)

