word = input()
SetWord = set(word.split())

def Sorting(x):
    x = [str(i) for i in x]
    x.sort()
    return x
print(Sorting(SetWord))