day = int(input("จำนวนวันที่จ้าง : "))
TotalMoney = 0
HourPerDay = []


for i in range(day):
    Hour = int(input("จำนวนชั่วโมงที่ทำ : "))
    if Hour >= 0 :
        HourPerDay.append(Hour)
        if i >= 2 :
            if HourPerDay[i-1] < 4 :
                if HourPerDay[i-2] < 4:
                    if HourPerDay[i] < 4:
                        break
    else:
        break

for i in range(len(HourPerDay)):
    if HourPerDay[i] == 8 :
        HourPerDay[i] = 300
    elif HourPerDay[i] >= 4 and HourPerDay[i] < 8 :
        HourPerDay[i] = 150
    elif HourPerDay[i] > 8 :
        if HourPerDay[i] >= 12:
            HourPerDay[i] = 500
        else : 
            HourPerDay[i] = ((HourPerDay[i] - 8) * 50) + 300
    elif HourPerDay[i] < 4 :
        HourPerDay[i] = 0


for i in range(len(HourPerDay)):
    TotalMoney = TotalMoney + HourPerDay[i] 

print(TotalMoney)
