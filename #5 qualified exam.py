Id = []
TotalScore = []
Qualified = []
Sc = 0

N = int(input("จำนวนผู้เข้าสอบ : "))
for i in range(N):
    UserID, Score = [str(x) for x in input("").split()]
    Score = int(Score)
    Id.append(UserID)
    TotalScore.append(Score)

for i in range(len(TotalScore)):
    Sc = Sc + TotalScore[i]

averageScore = Sc/N

for i in range(N):
    if TotalScore[i] >= averageScore:
        Qualified.append(Id[i])

print(len(Qualified))
for i in range(len(Qualified)):
    print(Qualified[i])
