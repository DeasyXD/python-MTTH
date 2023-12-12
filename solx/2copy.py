Nt = []
table = [0]*26
finish = []
Q = []
All = []
w, t = input().split()
w, t = int(w), int(t)
ntypeoftable = [int(x) for x in input().split()]
for i in range(len(ntypeoftable)):
    Nt.append([0]*int(ntypeoftable[i]))
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
    for k in range(1, n + 1):
        total_length += len(A[k])
    if isinstance(A[n], list):
        total_length += j+1
    else:
        total_length += 1
    return total_length

temp = customer[0]
for i in range(len(customer)):
    if ord((customer[i]).lower()) - 97 >= 0 and ord((customer[i]).lower()) - 97 <= 26 :
        table[ord((customer[i]).lower()) - 97] += 1
        a = find_not_one(Nt[ord((customer[i]).lower()) - 97])
        All.append(customer[i]+str(table[ord((customer[i]).lower()) - 97]))
        # if a is not None:
        #     Nt[ord((customer[i]).lower()) - 97][a] = 1
        #     print(check(Nt,ord((customer[i]).lower()) - 97,a))
        # else:
        #     Q.append(customer[i]+str(table[ord((customer[i]).lower()) - 97]))
        #     print(check(Nt,ord((customer[i]).lower()) - 97,a))
    else:
        finish.append(customer[i])
        # print(check(Nt,ord((customer[i]).lower()) - 97,a))
print(customer)
print(f"table : \n{table}")
print(f"Nt : \n{Nt}")
print(f"finish : \n{finish}")
print(f"Q : \n{Q}")

print(All)
