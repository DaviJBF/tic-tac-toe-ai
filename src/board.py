import os

SIZE = 9

def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

board = [' ' for _ in range(SIZE)]


def print_board():
    print(
    f"\n3  {board[0]} | {board[1]} | {board[2]}\n" \
    "  -----------\n" \
    f"2  {board[3]} | {board[4]} | {board[5]}\n" \
    "  -----------\n" \
    f"1  {board[6]} | {board[7]} | {board[8]}\n" \
    "   a   b   c\n")

def check_winner():
    x_won = False
    o_won = False
    # Checking rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            if board[i] == 'X':
                x_won = True
            elif board[i] == 'O':
                o_won = True
    # Checking colunms
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            if board[i] == 'X':
                x_won = True
            elif board[i] == 'O':
                o_won = True
    
    # Checking diagonals
    if board[0] == board[4] == board[8]:
        if board[0] == 'X':
                x_won = True
        elif board[0] == 'O':
            o_won = True
    
    if board[2] == board[4] == board[6]:
        if board[2] == 'X':
                x_won = True
        elif board[6] == 'O':
            o_won = True

    if x_won:   return 'X'
    elif o_won: return 'O'
    else:
        if avalible_moves(): return None
        else: return 'draw'
    
def avalible_moves():
    for i in range(SIZE):
        if board[i] == ' ':
            return True
    return False

def read_move(x_turn):
    invalid = False
    while True:
        clear_cli()
        print_board()
        if invalid:
            print("Invalid move, try again.")
        if x_turn:
            move = input("\'X\' Turn. Enter your move: ")
        else:
            move = input("\'O\' Turn. Enter your move: ")
        match move.lower():
            case 'a1': move = 6
            case 'a2': move = 3
            case 'a3': move = 0
            case 'b1': move = 7
            case 'b2': move = 4
            case 'b3': move = 1
            case 'c1': move = 8
            case 'c2': move = 5
            case 'c3': move = 2
            case _:
                invalid = True
                continue
        if board[move] == ' ':
            if x_turn:
                board[move] = 'X'
            else:
                board[move] = 'O'
            return
        else:
            invalid = True
        


def game_loop():
    winner = None
    for i in range(SIZE):
        if i % 2 == 0:
            x_turn = True
        else:
            x_turn = False
        read_move(x_turn)
        if i > 4:
            validator = check_winner()
            match validator:
                case None:
                    continue
                case 'X':
                    winner = 'X'
                case 'O':
                    winner = 'O'
                case _:
                    winner = 'draw'
            break
                
    clear_cli()
    print_board()
    if winner == 'X':
        print("\'X\' won, game over.")
    elif winner == 'O':
        print("\'O\' won, game over.")
    else:
        print("Draw, game over.")


game_loop()