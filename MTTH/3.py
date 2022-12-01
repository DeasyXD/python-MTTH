parcel = []
cost = 2000
Profit = 0

while True:
    Weight = float(input("น้ำหนัก : "))
    parcel.append(Weight)
    if sum(parcel) > 1000:
        parcel.pop()
        break

distance = int(input("ระยะทาง : ")) * 5

def Check(x):
    if x <= 1: 
        return x*50    
    elif x > 1 and x <= 10 :
        return (x-1) * 40 + 50
    else :
        return x * 30


for i in range(len(parcel)):
    Profit = Profit + Check(parcel[i])

def GorL(x):
    if x > cost + distance:
        return "Gain"
    else :
        return "Lose"

print("ต้นทุนที่ต้องใช้ : ",cost + distance)
print("รายได้จากพัสดุ : ",Profit)
print(GorL(Profit))
print(abs(Profit - (cost + distance)))