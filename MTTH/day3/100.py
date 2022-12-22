H = 35
L = 94

for i in range(H):
    for j in range(H):
        if H == j+i:
            if L == 4*i + 2*j:
                print("Found the answer!","chicken :",i,"rabbit :",j)

# 35  = x + y
# 94  = x(4) + y(2)