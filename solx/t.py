w, t = input().split()
w, t = int(w), int(t)

Max = [int(x) for x in input().split()]
present = [0]*len(Max)
data = []
for i in range(len(Max)):
    data.append([0]*Max[i])
listing = [x for x in input().split()]

def Index(A):
    return ord((A).lower()) - 97
for i in range(len(listing)):
    if present[Index(listing[i])] < Max[Index(listing[i])]:
        data[Index(listing[i])][present[Index(listing[i])]] = listing[i]
        present[Index(listing[i])] += 1
        

print(data)