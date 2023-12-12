w, t = input().split()
w, t = int(w), int(t)
z = []
ntypeoftable = [int(x) for x in input().split()]
for i in range(len(ntypeoftable)):
    z.append([0]*int(ntypeoftable[i]))
customer = input().split()
temp = customer[0]
Queue = []
j = 0
for i in range(len(customer)):
   if customer[i] != temp:
      j = 0
   else: 
      if i!=0: 
         j+=1
   temp = customer[i]
   if len(z[ord((customer[i]).lower()) - 97]) > sum(z[ord((customer[i]).lower()) - 97]) :
      for h in range(len(z[ord((customer[i]).lower()) - 97])):
         if z[ord((customer[i]).lower()) - 97][h] == 0:
            z[ord((customer[i]).lower()) - 97][h] = 1
            break
   if j >= len(z[ord((customer[i]).lower()) - 97]):
      j = 0 
      Queue.append(customer[i])
   z[ord((customer[i]).lower()) - 97][j] = 1
print(z)
print(Queue)