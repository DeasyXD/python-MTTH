def main():
    board = []
    for i in range(8):
        board.append(["◻"] * 8)

    # place first queen
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    board[row - 1][col - 1] = "♛"

    # place_queens จะ return True ถ้าเจอว่าสามารถวางได้ แต่ถ้าไม่สามารถวางได้จะ return False 
    place_queens(board, 1) # 1 คือจำนวนครั้งที่เราได้วาง queen ไว้แล้ว

    # print board
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()


def place_queens(board, queen_num):

    # base case
    # ถ้าวาง queen ได้ 8 ตัวแล้ว จะ return True
    if queen_num == 8:
        return True

    # place queen
    for i in range(8):
        for j in range(8):
            if board[i][j] == "◻":
                if is_safe(board, i, j):
                    board[i][j] = "♛"
                    if place_queens(board, queen_num + 1):
                        return True
                    board[i][j] = "◻"

    return False


def is_safe(board, row, col):

    # check row
    for i in range(8):
        if board[row][i] == "♛":
            return False

    # check column
    for i in range(8):
        if board[i][col] == "♛":
            return False

    # check diagonal
    for i in range(8):
        for j in range(8):
            if board[i][j] == "♛":
                if abs(row - i) == abs(col - j): # เช็คว่าอยู่ในเส้นทแยงมุมไหม ถ้าใช่จะมีค่าเท่ากัน แต่ถ้าไม่ใช่จะมีค่าไม่เท่ากัน และมีค่าต่างกันเท่ากับระยะห่างของแถวและคอลัมน์
                    return False

    return True


# ↓↓↓ ไปเจอมาใน youtube ครับ ↓↓↓
if __name__ == "__main__":
    main()

