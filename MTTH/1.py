Parcel = int(input("น้ำหนักพัสดุ : "))
def Check(x):
    if x <= 1: 
        return x*50    
    elif x > 1 and x <= 10 :
        return (x-1) * 40 + 50
    else :
        return x * 30

print(Check(Parcel))