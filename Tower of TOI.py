XEarth = []
YEarth = []

XWater = []
YWater = []

XWind = []
YWind = []

XFire = []
YFire = []

def CheckIfMoreOrLess(x):
    for i in range(len(x)):
        if x[i] < -500000 or x[i] > 500000:
            return True


def split_into_even_and_odd_lists(x,y,z):
    for i in range(len(x)):
        if (i+1)%2:
            y.append(x[i])
            # print(x[i],end=" ")
        else:
            z.append(x[i])
            # print(x[i],end=" ")

while True:
    try:
        demon_position_x,yt = [int(x) for x in input("Demon's position : ").split()]
        if demon_position_x < -500000 or demon_position_x > 500000 or yt < -500000 or yt > 500000:
            raise ValueError 
        break
    except ValueError:
        print("-500,000 <= demon_position_x,yt <= 500,000")

while True:
    try:
        N = int(input("N : "))
        if N < 2 or N > 1500:
            raise ValueError
        break
    except ValueError:
        print("2 <= N <= 1500")

#!EARTH
while True:
    try:
        EarthXY = [int(x) for x in input("Earth Element pos : ").split()]
        if CheckIfMoreOrLess(EarthXY) == True:
            raise ValueError
        else:
            split_into_even_and_odd_lists(EarthXY,XEarth,YEarth)
        break
    except ValueError:
        print("-500,000 <= xi,yi <= 500,000")

#!WATER
while True:
    try:
        WaterXY = [int(x) for x in input("Water Element pos : ").split()]
        if CheckIfMoreOrLess(WaterXY):
            raise ValueError 
        else:
            split_into_even_and_odd_lists(WaterXY,XWater,YWater)
        break
    except ValueError:
        print("-500,000 <= xj,yj <= 500,000")
 
#!WIND
while True:
    try:
        WindXY = [int(x) for x in input("Wind Element pos : ").split()]
        if CheckIfMoreOrLess(WindXY):
            raise ValueError 
        else:
            split_into_even_and_odd_lists(WindXY,XWind,YWind)
        break
    except ValueError:
        print("-500,000 <= xk,yk <= 500,000")

#!FIRE
while True:
    try:
        FireXY = [int(x) for x in input("Fire Element pos : ").split()]
        if CheckIfMoreOrLess(FireXY):
            raise ValueError 
        else:
            split_into_even_and_odd_lists(FireXY,XFire,YFire)
        break
    except ValueError:
        print("-500,000 <= xl,yl <= 500,000")



for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if XEarth[i] + XWater[j] + XWind[k] + XFire[l] == demon_position_x and YEarth[i] + YWater[j] + YWind[k] + YFire[l] == yt:
                    print(XEarth[i],YEarth[i])
                    print(XWater[j],YWater[j])
                    print(XWind[k],YWind[k])
                    print(XFire[l],YFire[l])
                    break
                else:
                    continue

