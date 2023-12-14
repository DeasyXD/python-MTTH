def check(A,n,j):
    total_length = 0
    for k in range(0, n):
        total_length += len(A[k])
    if isinstance(A[n], list):
        total_length += j+1
    else:
        total_length += 1
    return total_length

def check2(A, n):
  row_index = int((n - 1) / len(A[0]))
  column_index = (n - 1) % len(A[0])
  if row_index < len(A) and column_index < len(A[row_index]):
    A[row_index][column_index] = 5
x = [[0,4,0],[0,0,0,0],[0,0]]

print(check(x,2,0))
print(check2(x,2))
print(x)