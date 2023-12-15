n = int(input())
s1,s2 = input(),[x for x in input()]
count = 0
t = []
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j] or s1[i] == "?" or s2[j] == "?" :
            count+=1
            s2[j] = ""
            break
print(count)