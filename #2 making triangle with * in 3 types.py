def UpsidehalfL():
	for i in range(height * -1, 0, -1):  #คูณ-1เพื่อเปลี่ยนให้กลายเป็นบวก
		for c in range(0, i):  #สร้างความกว้างของสามเหลี่ยม
			print('*', end='')
		print()  #เพื่อเว้นบรรทัด


def UpsidefullTriangle():
    s=0
    for i in range((height*-1+1),1,-1):
        for space in range(0,((height*-1+1)-i)):
            print(end=" ")
        for c in range(i,(2*i)-1):
            print("*",end="")
        for c in range(1,i-1):
            print("*",end="")
        print()

def UpsidehalfR():
	s = 0
	for i in range(height*-1+1,1,-1):
		for space in range(0, (height*-1+1) -i):
			print(end=" ")
		while s != i - 1:
			print("*", end="")
			s += 1
		s = 0
		print()
		
		

def halfL():
	for i in range(height):
		for c in range(i + 1):  #สร้างความกว้างของสามเหลี่ยม
			print('*', end='')
		print()  #เพื่อเว้นบรรทัด


def fullTriangle():
	s = 0
	for i in range(1, height + 1):  #for i in range(start,stop,step) / เริ่มที่,หยุดที่(ตามบรรทัด),เพิ่มที่
		for space in range(1,(height - i) + 1):  #สร้างขนาดของเว้นวรรคในแต่ละแถว
			print(end=" ")
		while s != ((2 * i) - 1):  #สร้างจำนวนของดาว
			print("*", end="")
			s += 1
		s = 0
		print()


def halfR():
	s = 0
	for i in range(height):
		for space in range(1, (height - i) + 1):
			print(end=" ")
		while s != i + 1:
			print("*", end="")
			s += 1
		s = 0
		print()


def PositiveHeight():
	fullTriangle()
	halfL()
	halfR()


def NegativeHeight():
    UpsidefullTriangle()
    UpsidehalfL()
    UpsidehalfR()
    



while True:
	try:
		height = int(input('height of triangle : '))
	except ValueError:
		print("Please try again. Don't input 1,0 and -1 ")
		continue
	if height < 2 and height > -2:
		print("Please try again. Don't input 1,0 and -1 ")
		continue
	else:
		break

if height >= 2:
	PositiveHeight()
else:
	NegativeHeight()
