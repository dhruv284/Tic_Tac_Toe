def tic_tac_toe():
    board=[]

    for i in range(3):
        a=[]
        for j in range(3):
            a[j]=str(input("Enter X or O"))
        board.append(a)

    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        return "X"
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        return "O"
        
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        return "X"
    if board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
        return "X"
    if board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
        return "X"
    if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        return "O"
    if board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        return "O"
    if board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        return "O"
        
    if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        return "X"
    if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        return "X"
    if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        return "X"
        
    if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        return "O"
    if board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
        return "O"
    if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        return "O"

