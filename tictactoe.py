# main
def main():
    win = False
    board = create_board()
    sign = input("Choose X or O: ")
    player_1 = sign
    player_2 = ""
    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"
    
    while(win!=True):
        print("Player 1's turn. Write row and column of position with space between: ")
        first_row, first_col = map(int, input().split())
        board = move(first_row, first_col, player_1, board)
        print_board(board)

        if win == True:
            break
        
        print("Player 2's turn. Write row and column of position with space between: ")
        second_row, second_col = map(int, input().split())
        board = move(second_row, second_col, player_2, board)
        print_board(board)

        win = winner(win, board)

    print("Congratulations")


def create_board():
    board = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]
    return board

def move(row, col, player_sign, board):
    if board[row][col]=="":
        board[row][col] = player_sign
    else:
        print("Already chosen!")
    return board

def print_board(board):
    for i in range(3):
        print(board[i], "\n")

def winner(winner, board): 
    # main diagonal
    counter = 0
    while(counter!=3):
        if board[counter][counter] != board[0][0]:
            winner = False
            break
        else:
            winner = True
        counter+=1
    
    if winner == True:
        print("Winner based on main diagonal is: ", board[0][0])
        return winner
    
    # secondary diagonal
    row = 0
    col = 2
    while(row!=3):
        if board[row][col] != board[0][2]:
            winner = False
            break
        else:
            winner = True
        row+=1
        col-=1
    
    if winner == True:
        print("Winner based on secondary diagonal is: ", board[0][0])
        return winner
    
    # horizontal
    for i in range(3):
        winner = True
        for j in range(3):
            if board[i][j] == "":
                winner = False
                break
            if board[i][j] != board[i][0]:
                winner = False
                break
        if winner == True:
            print("Winner based on horizontal line is: ", board[i][0])
            return winner
    
    # vertical
    for i in range(3):
        winner = True
        for j in range(3):
            if board[j][i] == "":
                winner = False
                break
            if board[j][i] != board[j][0]:
                winner = False
                break
        if winner == True:
            print("Winner based on vertical line is: ", board[j][i])
            return winner

    return winner

main()