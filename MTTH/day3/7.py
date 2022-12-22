x,y = [int(i) for i in input().strip().split(",")]

table = [[i for i in range(y)] for i in range(x)]

for i in range(0,x):
    for j in range(0,y):
        table[i][j] = i*j

print(table)