x = 2000
y = 3200

for i in range(x,y+1):
    if i%7==0 and i%5!=0:
        if i == y-1 :
            print(i,end="")
        else:
            print(i,end = ",")


