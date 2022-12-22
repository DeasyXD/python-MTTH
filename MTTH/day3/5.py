
class number1:
    def __init__(self) -> None:
        pass
    def getString(self):
        self.message = input()
    def printString(self):
        print(self.message.upper())

msg = number1()
msg.getString()
msg.printString()


