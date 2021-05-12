import time
import random
import IPython

def did_x_win(board):
    for row in board:
        if row == ['X','X','X']:
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == 'X':
            return True
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        return True
    else:
        return False

def did_o_win(board):
    for row in board:
        if row == ['O','O','O']:
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == 'O':
            return True
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return True
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
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

def turn_1(board):
    display(board)
    print("OK, let me think...")
    time.sleep(2)
    pos = random.randint(1,4)
    if pos == 1:
        return (0,0)
    elif pos == 2:
        return (0,2)
    elif pos == 3:
        return (2,0)
    elif pos == 4:
        return (2,2)

def turn_2(board):
    display(board)
    print("OK, let me think...")
    time.sleep(2)
    if board[1][1] == ' ':
        return (1,1)
    else:
        return random_open_corner(board)

def turn_3(board):
    display(board)
    print("Sorry, mining bitcoin. brb")
    time.sleep(2)
    print("ok, back. thinking...")
    time.sleep(2)
    if board[0][1] == 'O' or board[1][0] == 'O' or board[1][2] == 'O' or board[2][1] == 'O':
        return (1,1)
    elif board[0][0] == 'O' or board[0][2] == 'O' or board[2][0] == 'O' or board[2][2] == 'O':
        return random_open_corner(board)
    else:
        if board[0][0] == 'X':
            return (2,2)
        elif board[0][2] == 'X':
            return (2,0)
        elif board[2][0] == 'X':
            return (0,2)
        elif board[2][2] == 'X':
            return (0,0)

def turn_4(board):
    display(board)
    print("sry, buying GME. moon rockets, diamond hands, etc. you get it. brb")
    time.sleep(2)
    print("mmm, those were some good tendies. ok, i'm ready to play. lemme think")
    time.sleep(2)
    
    # block O from winning, if possible
    
    check_can_x_block = can_x_block(board)
    if check_can_x_block[0] == True:
        return (check_can_x_block[1][0], check_can_x_block[1][1])

    # checklist if X is in center
    
    if board[1][1] == 'X':
        
        # if O is in only corners (in this case, opp corners), go on random side
        
        corners = board[0][0] + board[0][2] + board[2][0] + board[2][2]        
        if corners.replace(' ','') == 'OO':
            return random_open_side(board)
        
        # otherwise, block the potential 2x attack by O
        
        check_can_x_block_2x_attack = can_x_block_2x_attack(board)
        if check_can_x_block_2x_attack[0] == True:
            return (check_can_x_block_2x_attack[1][0], check_can_x_block_2x_attack[1][1])
        
        else:
            return random_open_side(board)

    # if X is not in center, and X did not block O, then go in random corner

    else:
        return random_open_corner(board)

def turn_5plus(board):
    display(board)
    print("hmmm, tough board...")
    time.sleep(2)
    
    # win right now, if possible
    
    check_can_x_win = can_x_win(board)
    if check_can_x_win[0] == True:
        return (check_can_x_win[1][0], check_can_x_win[1][1])
    
    # block O from winning, if possible
    
    check_can_x_block = can_x_block(board)
    if check_can_x_block[0] == True:
        return (check_can_x_block[1][0], check_can_x_block[1][1])
    
    # set up guaranteed win next turn, if possible
    
    check_can_x_win_next_turn = can_x_win_next_turn(board)
    if check_can_x_win_next_turn[0] == True:
        return (check_can_x_win_next_turn[1][0], check_can_x_win_next_turn[1][1])
    
    # set up potential (if unlikely) win next turn
    
    check_can_x_get_2_in_a_row = can_x_get_2_in_a_row(board)
    if check_can_x_get_2_in_a_row[0] == True:
        return (check_can_x_get_2_in_a_row[1][0], check_can_x_get_2_in_a_row[1][1])
    
    # otherwise, move randomly
    
    is_random_turn = random_turn(board)
    return (is_random_turn[0], is_random_turn[1])

def random_turn(board):
    x = 0
    while x == 0:
        row = random.randint(0,2)
        pos = random.randint(0,2)
        if board[row][pos] == ' ':
            return (row,pos)

def random_open_corner(board):
    x = 0
    while x == 0:
        pos = random.randint(1,4)
        if pos == 1 and board[0][0] == ' ':
            return (0,0)
        elif pos == 2 and board[0][2] == ' ':
            return (0,2)
        elif pos == 3 and board[2][0] == ' ':
            return (2,0)
        elif pos == 4 and board[2][2] == ' ':
            return (2,2)

def random_open_side(board):
    x = 0
    while x == 0:
        pos = random.randint(1,4)
        if pos == 1 and board[0][1] == ' ':
            return (0,1)
        elif pos == 2 and board[1][0] == ' ':
            return (1,0)
        elif pos == 3 and board[2][1] == ' ':
            return (2,1)
        elif pos == 4 and board[1][2] == ' ':
            return (1,2)

def can_x_win(board):
    # checking rows
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ' and board[row][pos-1] == board[row][pos-2] == 'X':
                return (True,(row,pos))
    # checking columns
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ' and board[row-1][pos] == board[row-2][pos] == 'X':
                return (True,(row,pos))
    # checking diaganols
    for num in range(3):
        if board[num][num] == ' ' and board[num-1][num-1] == board[num-2][num-2] == 'X':
            return (True,(num,num))   
    for num in range(3):
        if board[num-3][-num+2] == ' ' and board[num-2][-num+1] == board[num-1][-num] == 'X':
            return (True,(num-3,-num+2))       
    # otherwise, return false (and a non-existant square)
    else:
        return (False, (3,3))

def can_x_block(board):
    # checking rows
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ' and board[row][pos-1] == board[row][pos-2] == 'O':
                return (True,(row,pos))
    # checking columns
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ' and board[row-1][pos] == board[row-2][pos] == 'O':
                return (True,(row,pos))
    # checking diaganols
    for num in range(3):
        if board[num][num] == ' ' and board[num-1][num-1] == board[num-2][num-2] == 'O':
            return (True,(num,num))   
    for num in range(3):
        if board[num-3][-num+2] == ' ' and board[num-2][-num+1] == board[num-1][-num] == 'O':
            return (True,(num,-num+2))       
    # otherwise, return false (and a non-existant square)
    else:
        return (False, (3,3))

def can_x_win_next_turn(board):
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ':
                
                # checking row/column combo
                
                # row check first
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'X':
                    
                    # then column check
                    column_check = board[row-1][pos] + board[row-2][pos]
                    if column_check.replace(' ','') == 'X':
                        
                        # then return coordinates
                        return (True,(row,pos))

                # checking row/diag combo
               
                # row check first
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'X':
                        
                    # then diag-1 check
                    if row == pos:
                        diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))   

                    # then diag-2 check
                    if row + pos == 2:
                        diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))                     

                #checking column/diag combo

                # column check first
                column_check = board[row-1][pos] + board[row-2][pos]
                if column_check.replace(' ','') == 'X':
                        
                    # then diag-1 check
                    if row == pos:
                        diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))   

                    # then diag-2 check
                    if row + pos == 2:
                        diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))     
 
    else:
        return (False, (3,3))

def can_x_block_2x_attack(board):
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ':
                
                # checking row/column combo
                
                # row check first
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'O':
                    
                    # then column check
                    column_check = board[row-1][pos] + board[row-2][pos]
                    if column_check.replace(' ','') == 'O':
                        
                        # then return coordinates
                        return (True,(row,pos))

                # checking row/diag combo
               
                # row check first
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'O':
                        
                    # then diag-1 check
                    if row == pos:
                        diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                        if diag_check.replace(' ','') == 'O':
                        
                            # then return coordinates
                            return (True,(row,pos))   

                    # then diag-2 check
                    if row + pos == 2:
                        diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                        if diag_check.replace(' ','') == 'O':
                        
                            # then return coordinates
                            return (True,(row,pos))                     

                #checking column/diag combo

                # column check first
                column_check = board[row-1][pos] + board[row-2][pos]
                if column_check.replace(' ','') == 'O':
                        
                    # then diag-1 check
                    if row == pos:
                        diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                        if diag_check.replace(' ','') == 'O':
                        
                            # then return coordinates
                            return (True,(row,pos))   

                    # then diag-2 check
                    if row + pos == 2:
                        diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                        if diag_check.replace(' ','') == 'O':
                        
                            # then return coordinates
                            return (True,(row,pos))     
 
    else:
        return (False, (3,3))

def can_x_block_all_2x(board):
    count_blocks = 0
    where_blocks = []
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ':
                
                # checking row/column combo
                
                # row check first
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'X':
                    
                    # then column check
                    column_check = board[row-1][pos] + board[row-2][pos]
                    if column_check.replace(' ','') == 'X':
                        
                        # then save coordinates
                        count_blocks += 1
                        where_blocks.append((row,pos))

                # checking row/diag combo
               
                # row check first
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'X':
                        
                    # then diag-1 check
                    if row == pos:
                        diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))   

                    # then diag-2 check
                    if row + pos == 2:
                        diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))                     

                #checking column/diag combo

                # column check first
                column_check = board[row-1][pos] + board[row-2][pos]
                if column_check.replace(' ','') == 'X':
                        
                    # then diag-1 check
                    if row == pos:
                        diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))   

                    # then diag-2 check
                    if row + pos == 2:
                        diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                        if diag_check.replace(' ','') == 'X':
                        
                            # then return coordinates
                            return (True,(row,pos))     
 
    else:
        return (False, (3,3))

def can_x_get_2_in_a_row(board):
    for row in range(len(board)):
        for pos in range(len(board[0])):
            if board[row][pos] == ' ':
                
                # checking row
                
                row_check = board[row][pos-1] + board[row][pos-2]
                if row_check.replace(' ','') == 'X':
                    return (True,(row,pos)) 
                
                # checking column
                
                column_check = board[row-1][pos] + board[row-2][pos]
                if column_check.replace(' ','') == 'X':
                    return (True,(row,pos))     
                       
                # checking diag
                
                if row == pos:
                    diag_check = board[row-1][pos-1] + board[row-2][pos-2]
                    if diag_check.replace(' ','') == 'X':
                        return (True,(row,pos))   
                
                if row + pos == 2:
                    diag_check = board[row-2][pos-1] + board[row-1][pos-2]
                    if diag_check.replace(' ','') == 'X':
                        return (True,(row,pos))                     

    else:
        return (False, (3,3))

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
        who_first = go_first()
        if who_first == 'YES':
            player_goes_first()
        elif who_first == 'NO':
            comp_goes_first()
        is_new_game = play_again()

def go_first():
    who_first = ''
    while who_first not in ['YES','NO']:
        who_first = input('Would you like to go first? (Yes or No) ').upper()
        if who_first == "YES":
            return 'YES'
        elif who_first == 'NO':
            return 'NO'
        else:
            print("Fine, I'll ask again.")

def player_goes_first():
        
    # empty board before the first turn
    
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    # player goes first
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'

    # comp goes second
    
    new_move = turn_2(board)
    board[new_move[0]][new_move[1]] = 'X'
      
    # player goes third
     
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
       
    # comp goes fourth
    
    new_move = turn_4(board)
    board[new_move[0]][new_move[1]] = 'X'
 
    # player goes fifth
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    if did_o_win(board) == True:
        display(board)
        print("Congrats, you lucky bastard!")
        return
     
    # comp goes sixth
    
    new_move = turn_5plus(board)
    board[new_move[0]][new_move[1]] = 'X'
    if did_x_win(board) == True:
        display(board)
        print("Haha, filthy human, you've been beaten by THE SINGULARITY!")
        return
    
    # player goes seventh
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    if did_o_win(board) == True:
        display(board)
        print("Congrats, you lucky bastard!")
        return
     
    # comp goes eighth
    
    new_move = turn_5plus(board)
    board[new_move[0]][new_move[1]] = 'X'
    if did_x_win(board) == True:
        display(board)
        print("Haha, filthy human, you've been beaten by THE SINGULARITY!")
        return
    
    # player goes ninth
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    if did_o_win(board) == True:
        display(board)
        print("Congrats, you lucky bastard!")
        return

    else:
        display(board)
        print("Cat's game. Meeeeeeeooowwwwww.")

def comp_goes_first():
    
    # empty board before the first turn
    
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    # comp goes first
    
    new_move = turn_1(board)
    board[new_move[0]][new_move[1]] = 'X'
    
    # player goes second
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    
    # comp goes third
    
    new_move = turn_3(board)
    board[new_move[0]][new_move[1]] = 'X'
    
    # player goes fourth
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    
    # comp goes fifth
    
    new_move = turn_5plus(board)
    board[new_move[0]][new_move[1]] = 'X'
    if did_x_win(board) == True:
        display(board)
        print("Haha, filthy human, you've been beaten by THE SINGULARITY!")
        return
    
    # player goes sixth
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    if did_o_win(board) == True:
        display(board)
        print("Congrats, you lucky bastard!")
        return
    
    # comp goes seventh
    
    new_move = turn_5plus(board)
    board[new_move[0]][new_move[1]] = 'X'
    if did_x_win(board) == True:
        display(board)
        print("Haha, filthy human, you've been beaten by THE SINGULARITY!")
        return
    
    # player goes eighth
    
    new_move = player_turn(board)
    board[new_move[0]][new_move[1]] = 'O'
    if did_o_win(board) == True:
        display(board)
        print("Congrats, you lucky bastard!")
        return
        
    # comp goes ninth
    
    new_move = turn_5plus(board)
    board[new_move[0]][new_move[1]] = 'X'
    if did_x_win(board) == True:
        display(board)
        print("Haha, filthy human, you've been beaten by THE SINGULARITY!")
        return
        
    else:
        display(board)
        print("Cat's game. Meeeeeeeooowwwwww.")

play_tic_tac_toe()
