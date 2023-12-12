Nt = [["A1","A2","A3","A4"],["B1","B2"],["C1","C2","C3"]]
t = sum(Nt, [])
customer = ["A","B","A","B","1","2","3","B","B","B","A"]
i = 5
length = 0
if not (ord((customer[i]).lower()) - 97 >= 0 and ord((customer[i]).lower()) - 97 <= 26) :
    for j in range(len(Nt)):
        length = len(Nt[j])