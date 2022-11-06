tower1 = []
tower2 = []
tower3 = []

disks = int(input("Disk : "))
for i in range(disks, 0, -1):
    tower2.append(i)
def move(n, source, target, spare):
    if n == 1:
        target.append(source.pop())
        print(tower1, tower2, tower3, sep=' ')
    else:
        move(n-1, source, spare, target)
        move(1, source, target, spare)
        move(n-1, spare, target, source)
        
print(tower1, tower2, tower3)
move(disks, tower2, tower3, tower1)
print("Number of moves: ", (2**disks)-1)
