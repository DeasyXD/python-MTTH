import math
x, y = [int(x) for x in input("Enter two values: ").split()]
z = x/y
AF = z%1
string_value = str(AF)
print(string_value)
afterdecimal = string_value.replace('.','')

print(type(afterdecimal))

afterdecimal = int(afterdecimal)

print(type(afterdecimal))

beforedecimal = int(z//1)
#print (afterdecimal, beforedecimal)
print(afterdecimal+beforedecimal)
