import time
import IPython

def did_player_win(board, letter):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == letter:
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == letter:
            return True
    if board[0][2] == board[1][1] == board[2][0] == letter:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == letter:
        return True
    else:
        return False

def display(board):
    IPython.display.clear_output()
    count = 0
    for row in board:
        row_nice = '|'.join(row)
        print(row_nice)
        count += 1
        if count <3:
            print('-----')
    print('')

def player_turn(board):
    display(board)
    # get player input
    
    open_check = 0
    while open_check == 0:
        # get row input
        row = ''
        row_fail = ''
        while type(row) !=int:
            row = input(f"Please {row_fail}enter a row number (1, 2, or 3): ")
            if row == '1' or row == '2' or row == '3':
                row = int(row)
            else:
                row_fail = 'try a little harder to '

        # get column input
        column = ''
        column_fail = ''
        while type(column) !=int:
            column = input(f"Please {column_fail}enter a column number (1, 2, or 3): ")
            if column == '1' or column == '2' or column == '3':
                column = int(column)
            else:
                column_fail = 'try a little harder to '
        player_move = (row-1,column-1)
        if board[player_move[0]][player_move[1]] == ' ':
            return player_move
        else:
            print("Sorry, this square is not open. Please try a little harder to find an open square.")

def play_again():
    play_again = ''
    while play_again not in ['YES','NO']:
        play_again = input('Would you like to play again? (Yes or No) ').upper()
        if play_again == "YES":
            return 'YES'
        elif play_again == 'NO':
            print('Thanks for playing! I hope you had as much fun as I did!')
            return 'NO'
        else:
            print("Fine, I'll ask again.")

def play_tic_tac_toe():
    
    is_new_game = 'YES'
    print("Welcome to Chris' tic tac toe game!")
    while is_new_game == 'YES':
        play_game()
        is_new_game = play_again()

def play_game():
        
    # empty board before the first turn
    
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    turn = 0
    letter = ''
    while turn <= 8:
        if turn%2 == 0:
            letter = 'X'
        else:
            letter = 'O'
        new_move = player_turn(board)
        board[new_move[0]][new_move[1]] = letter
        
        if did_player_win(board, letter) == True:
            display(board)
            print(f'Player {letter} has won the game.')
            return # 'test'
        
        turn += 1
    
    else:
        display(board)
        print("Cat's game. Meeeeeeeooowwwwww.")

play_tic_tac_toe()

















