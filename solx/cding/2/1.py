s = int(input())
l = [int(x) for x in input().split()]
txt = input()
a = []
v = []
temp = ""
for i in range(0,len(txt),s):
    a.append(txt[i:i+s])
for i in range(len(a)):
    x = []
    for j in range(s):
        while len(a[i]) != s:
            a[i]+=" "
        x.append(a[i][j])
    v.append(x)
for j in range(len(v)) :
    temp = a[j]
    for k in range(s) :
        R = l[k]-1
        v[j][k] = temp[R]
for i in v:
    for j in i :
        print(j,end="")