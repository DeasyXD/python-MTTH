x,y = input().split()
x,y = int(x),int(y)
table = []
for i in range(x):
    table.append(input().split())
print(table)
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == "1":
            print(i+1,j+1)
            