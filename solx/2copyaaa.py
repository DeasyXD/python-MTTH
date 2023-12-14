Nt = []
table = [0]*26
finish = []
Q = []
Qtype = []
count = []
All = []
FAll = []
w, t = input().split()
w, t = int(w), int(t)
ntypeoftable = [int(x) for x in input().split()]
for i in range(len(ntypeoftable)):
    count.append([0]*int(ntypeoftable[i]))
    Nt.append([])
    

customer = [x for x in input().split()]
print("--------------------------------")

def find_not_one(A):
  for k in range(len(A)):
    if A[k] == 1:
      continue
    else:
      return k
  return None

def check(A,n,j):
    total_length = 0
    for k in range(0, n):
        total_length += len(A[k])
    if isinstance(A[n], list):
        total_length += j+1
    else:
        total_length += 1
    return total_length

def check2(A, n, m ,m2):
  row_index = int((n - 1) / len(A[0]))
  column_index = (n - 1) % len(A[0])
  if row_index < len(A) and column_index < len(A[row_index]):
        if m2 == "--" :
            A[row_index][column_index] = m
            print(f"{m} {check(A,row_index,column_index)}")
            Q.pop(0),Qtype.pop(0)
        else :
            if ord((m2).lower()) - 97 == row_index:
                A[row_index][column_index] = m
                print(f"{m} {check(A,row_index,column_index)}")
                Q.pop(0),Qtype.pop(0)
            else:
                A[row_index][column_index] = "--"
                print(f"-- {check(A,row_index,column_index)}")

for i in range(len(customer)):
    if ord((customer[i]).lower()) - 97 >= 0 and ord((customer[i]).lower()) - 97 <= 26 :
        table[ord((customer[i]).lower()) - 97] += 1
        All.append(customer[i]+str(table[ord((customer[i]).lower()) - 97]))
        FAll.append(customer[i])
    else:
        finish.append(customer[i])
        
for i in range(len(All)):
    if customer[i] == 0 :
        break
    if ord((customer[i]).lower()) - 97 >= 0 and ord((customer[i]).lower()) - 97 <= 26 :
        index = ord((customer[i]).lower()) - 97
        if len(Nt[index]) < ntypeoftable[index]:
            Nt[index].append(All[i])
            ch = check(count,index,len(Nt[index])-1)
            print(f"{All[i]} {ch}")
        else:
            if All[i] not in Nt[index]:
                Q.append(All[i])
                Qtype.append(customer[i])
                print(f"{All[i]} w")
            
    else:
        if len(Q) != 0 :
            ch = check(count,index,len(Nt[index])-1)
            check2(Nt,int(customer[i]),Q[0],Qtype[0])
            
        else:
            check2(Nt,int(customer[i]),"--","--")
            

print(ntypeoftable)
print(f"table : \n{table}")
print(f"Nt : \n{Nt}")
print(f"finish : \n{finish}")
print(f"Q : \n{Q}")

print(All)
