height = int(input('height of triangle : '))

def halfL():
  for i in range(height):
    for c in range(i+1): #สร้างความกว้างของสามเหลี่ยม
     print('*',end='')
    print() #เพื่อเว้นบรรทัด
def fullTriangle():
  s=0
  for i in range(1, height+1): #for i in range(start,stop,step) / เริ่มที่,หยุดที่(ตามบรรทัด),เพิ่มที่
    for space in range(1, (height-i)+1): #สร้างขนาดของเว้นวรรคในแต่ละแถว
      print(end=" ")
    while s != ((2*i)-1): #สร้างจำนวนของดาว
      print("*",end="")
      s+1
    s=0
    print()



def halfR():
  s=0
  for i in range(height):
    for space in range(1,(height-i)+1):
      print(end=" ")
    while s!=i+1:
      print("*",end="")
      s+=1
    s=0
    print()
  

fullTriangle()
halfL()
halfR()
