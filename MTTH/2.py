weightIC = [int(x) for x in input().split()]
    
totalW = 0
totalM = 0

for i in range(len(weightIC)):
    totalW = totalW + weightIC[i]
    if totalW > 1000:
        weightIC.remove(weightIC[i])
        i = i-1

LastTotalW = 0

for i in range(len(weightIC)):
    LastTotalW = LastTotalW + weightIC[i]
print("LastTotalWeight =",LastTotalW)

def Check(x):
    if x <= 1: 
        return x*50    
    elif x > 1 and x <= 10 :
        return (x-1) * 40 + 50
    else :
        return x * 30

for i in range(len(weightIC)):
    totalM = totalM + Check(weightIC[i])

print("Total Money : ",totalM)

