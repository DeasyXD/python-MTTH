import math 
distance = []
Point = int(input("จำนวนจุด : "))

for i in range(Point) :
    x,y = [float(j) for j in input("x,y : ").split()]
    x = x**2
    y = y**2
    distance.append(math.sqrt(x + y))

for i in distance:
    if i > 1:
        distance.remove(i)

ans = len(distance)/Point
ans = "{:.3f}".format(ans)
print("สัดส่วน = ", ans)


    