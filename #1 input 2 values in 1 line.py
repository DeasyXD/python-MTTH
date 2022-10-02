import math
x, y = [int(x) for x in input("Enter two values: ").split()]
z = x/y
afterdecimal = z%1
beforedecimal = z//1
#print (afterdecimal, beforedecimal)
print(afterdecimal+beforedecimal)
