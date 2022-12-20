f = 0
number1, number2 = [int(i) for i in input("").split()]

for j in range(number1,number2+1):
    f = 0
    for z in range(len(str(j))):
        GetSingleNumber = int(str(j)[z]) 
        # print("GetSingleNumber",GetSingleNumber)
        f = f + GetSingleNumber**len(str(j))
        # print(len(str(j))," ",GetSingleNumber, " ", j, " ",f)
    if j == f : 
        print(j)
        



