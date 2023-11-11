s=0

def tictactoe():

    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

def check_game():
    if game_board[0][0]=="o" and game_board[0][1]=="o" and game_board[0][2]=="o":
        print("player 1 is winner")
        s=1
    if game_board[1][0]=="o" and game_board[1][1]=="o" and game_board[1][2]=="o":
        print("player 1 is winner")
        s=1
    if game_board[2][0]=="o" and game_board[2][1]=="o" and game_board[2][2]=="o":
        print("player 1 is winner")
        s=1
    if game_board[0][0]=="o" and game_board[1][0]=="o" and game_board[2][0]=="o":
        print("player 1 is winner")
        s=1
    if game_board[0][1]=="o" and game_board[1][1]=="o" and game_board[2][1]=="o":
        print("player 1 is winner")
        s=1
    if game_board[0][2]=="o" and game_board[1][2]=="o" and game_board[2][2]=="o":
        print("player 1 is winner")
        s=1
    if game_board[0][0]=="o" and game_board[1][1]=="o" and game_board[2][2]=="o":
        print("player 1 is winner")
        s=1
    if game_board[0][2]=="o" and game_board[1][1]=="o" and game_board[2][0]=="o":
        print("player 1 is winner")
        s=1

    if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
        print("player 2 is winner")
        s=1
    if game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
        print("player 2 is winner")
        s=1
    if game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
        print("player 2 is winner")
        s=1
    if game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
        print("player 2 is winner")
        s=1
    if game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
        print("player 2 is winner")
        s=1
    if game_board[0][2]=="x" and game_board[1][2]=="x" and game_board[2][2]=="x":
        print("player 2 is winner")
        s=1
    if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
        print("player 2 is winner")
        s=1
    if game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
        print("player 2 is winner")
        s=1
    return

def tie():
    if game_board[0][0]!="-" and game_board[0][1]!="-" and game_board[0][2]!="-" and game_board[1][0]!="-" and game_board[1][1]!="-" and game_board[1][2]!="-" and game_board[2][0]!="-" and game_board[2][1]!="-" and game_board[2][2]!="-":
        print("No winner!")


game_board=[["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

tictactoe()

while True:
    #player1 => O
    print("player1")
    while True:
        row=int(input("enter row: "))
        col=int(input("enter col: "))
        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]=="-":
                game_board[row][col]= "o"
                tictactoe()
                check_game()
                break
            else: 
                print("choose another home!")
        else:
            print("choose between 0 and 2!")     
    if s==1:
        break

    tie()

    #player2 => x
    print("player2")
    while True:
        row=int(input("enter row: "))
        col=int(input("enter col: "))
        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]=="-":
                game_board[row][col]= "x"
                tictactoe()
                check_game()
                break  
            else: 
                print("choose another home!")
        else:
            print("choose between 0 and 2!")  
    if s==1:
        break    
           
    tie()          
