num = int(input())

def dictionary(x):
    for i in range(1, x+1):
        if i == x:
            # Last value, don't print the comma
            print(str(i)+":"+str(i*i))
        else:
            print(str(i)+":"+str(i*i), end=", ")


dictionary(num)