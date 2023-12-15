g,n = input().split()
g,n = int(g),int(n)

s = []
e = []
w = []
for i in range(n):
    x = [a for a in input().replace(" ","")]
    s.append(int(x[0])),e.append(int(x[1])),w.append(int(x[-1]))
se = []
p = []
d = []
if not g in e:
    print("-1")
else:
    for i in range(n):
        x = []
        x.append(s[i]),x.append(e[i])
        se.append(x)
    for i in range(n-1):
        for j in range(n-1) :    
            if se[i][-1] == se[j][0]:
                p.append([se[i],se[j]])
                d.append(w[i] + w[j])
    for k in range(len(p)) :
        for j in range(n-1) :
            if p[k][-1][-1] == se[j][0]:
                p[k].append(se[j])
print(se)
print(p)
print(min(d))

        

         