id = input()
total = 0
for i in range(len(id)-1):
    x = ord(id[i])-64
    if  x < 1 and x > 26:
        x = int(id[i])
    total += x
N11 = 0 
c = total%11
if c <= 1:
    N11 = 1-c
else:
    N11 = 11-c
if N11 == int(id[-1]):
    print("T",end = " ")
else:
    print("F",end = " ")
print(total)
