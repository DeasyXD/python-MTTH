N,k = [int(i) for i in input().split()]

my_list = [[0 for _ in range(k)] for _ in range(N)]

for i in range(N):
    K = [int(x) for x in input().split()]
    my_list[i] = K

# print(my_list)

SumTable = []
for i in range(len(my_list)):
    Sum = 0
    for j in range(len(my_list[i])):
        Sum = Sum + my_list[i][j]
    SumTable.append(Sum)

# print(SumTable)

def Check(n):
    Max = 0
    l = 0
    Max_time = 0
    Ath = 0

    for i in range(len(SumTable)):
        if SumTable[i] > l :
            l = SumTable[i]
            Max = i
    
    for i in range(k):
        for j in range(len(my_list[i])):
            if my_list[Max][i] >= my_list[i][j]:
                Max_time += 1

    return l,Max_time 
    

print(Check(SumTable))



