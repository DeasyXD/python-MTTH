sub = input()
w = []

for i in range(int(input())):
    x = input()
    a=0
    for j in range(len(x)):
        if x[j] in sub :
            a += 1
        if a >= len(sub):
            break
    if a >= len(sub):
        w.append("YES")
    else:
        w.append("NO")
for i in w:
    print(i)