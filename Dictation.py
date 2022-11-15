import random
Word = ["cabinet","calculator","calendar","call","campaign","cancellation","candidate","canvass","capability","capacity"]
Synonym = [["cupboard"],["no"],["no"],["no"],["no"],["nullification termination","termination nullification"],["applicant"],["examination"],["ability"],["potential"]]
Word2 = ["date","deadline","dealer","dealing","debate","debris","debt","debut","decade","decision"]
Synonym2 = [["no"],["no"],["merchant"],["no"],["argument discussion","discussion argument"],["rubble ruin","ruin rubble"],["obligation"],["no"],["no"],["determination"]]
def main(w,s):
    while len(w) > 0:
        i = random.randint(0,len(w)-1)
        print("Word are ",w)
        print("Synonym are ",s)  
        print('"',w[i],'"')
        Syn = input("Enter the synonym: ")
        if s[i] == ["no"]:
            print("There is no synonym for this word")
            del w[i]
            del s[i]
        elif Syn in s[i]:
            print("XXX Correct XXX")
            del w[i]
            del s[i]
        else:
            print("!!! Incorrect !!!")
            print("The correct answer is ",s[i])

print("Welcome to the Dictionary")
print("There are two versions of the Dictionary")
print("Version 1: ครึ่งแรก")
print("Version 2: ครึ่งหลัง")
Ask = input("Which version do you want to play? ")
if Ask == "1":
    main(Word,Synonym)
elif Ask == "2":
    main(Word2,Synonym2)
else:
    print("Please enter 1 or 2")
