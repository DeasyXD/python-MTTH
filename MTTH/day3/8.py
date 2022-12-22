word = [x for x in input().strip().split(",")]

for i in range(len(word)-1,-1,-1):
    if i == 0:
        print(word[i],end="")
    else :
        print(word[i],end=", ")