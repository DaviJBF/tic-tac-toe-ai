SIZE = 9
board = [''
' ' for _ in range(SIZE)]

def print_board(board):
    print(
    f"3  {board[0]} | {board[1]} | {board[2]}\n" \
    "  -----------\n" \
    f"2  {board[3]} | {board[4]} | {board[5]}\n" \
    "  -----------\n" \
    f"1  {board[6]} | {board[7]} | {board[8]}\n" \
    "   a   b   c")

def check_winner(board):
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

    if x_won:
        if o_won:
            return None
        else:
            return 'X'
    elif o_won:
        return 'O'
    else:
        return 'draw'
    
def get_avalible_moves(board):
    avalible = []
    for i in range(SIZE):
        if board[i] == ' ':
            avalible.append(i)
    return avalible

