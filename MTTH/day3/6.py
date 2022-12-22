C = 50
H = 30
D = [int(x) for x in input("D : ").strip().split(",")]

def Formula():
    for i in D:
        q = ((2*C*i)/H)**(1/2)
        q = "{:.0f}".format(q)
        print(q)

Formula()