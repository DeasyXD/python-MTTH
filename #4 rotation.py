LineTable = []
row,column = [int(x) for x in input("Row, Column : ").split()]
NewLine = []
# print(NewLine)
for i in range(row):
    line = [int(y) for y in input().split()]
    LineTable.append(line)

for i in range(len(LineTable[0])-1,-1,-1):
    for j in range(len(LineTable)):
        NewLine.append(LineTable[j][i])
# NewLine = [[LineTable[j][i] for j in range(len(LineTable))] for i in range(len(LineTable[0])-1,-1,-1)]
# print(NewLine)
print()
for i in range(len(NewLine)):
    if (i+1)%(row) :
        print(NewLine[i],end=" ")
    else:
        print(NewLine[i], end=" ")
        print()
