from re import X
from tkinter.font import BOLD
import numpy as np

Plot = input("Plot : ") 
AforTable = "ABCDEFGH"
NforTable = "12345678"

FirstA = AforTable.find(Plot[0])  + 1
SecondN = NforTable.find(Plot[1]) + 1

print(FirstA,SecondN)

def printcheckboard(n):

    print("board : ")
  
    x = np.zeros((n, n), dtype = object)
    
    for i in range(n):
        for j in range(n):
            x[i][j] = int(NforTable[i] + NforTable[j])
            
    print(x)
    print(Plot +" : " + str(x[(FirstA-1)][(SecondN-1)]))

n = 8
printcheckboard(n)
