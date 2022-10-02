import math
x, y = [int(x) for x in input("Enter two values: ").split()]
z = x/y
string_value = str(z%1)
print(string_value)
afterdecimal = int(string_value.replace('.',''))

beforedecimal = int(z//1)
#print (afterdecimal, beforedecimal)
print(afterdecimal+beforedecimal)
