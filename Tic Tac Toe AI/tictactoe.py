def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + '|' + board[i+1] + '|' + board[i+2] + '\n' + '-----')
def check_win(board, player):
    for i in range(0, 9, 3):
        if(board[i] == player and board[i+1] == player and board[i+2] == player):
            return True
    for i in range(3):
        if(board[i] == player and board[i+3] == player and board[i+6] == player):
            return True
    if((board[0] == player and board[4] == player and board[8] == player) or (board[2] == player and board[4] == player and board[6] == player)):
        return True
    return False
def is_board_full(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True
def minimax(board, depth, maximizingPlayer):
    if(is_board_full(board) or check_win(board, 'X') or check_win(board, 'O')):
        if check_win(board, 'O'):
            return 10
        elif check_win(board, 'X'):
            return -10
        else:
            return 0
    if maximizingPlayer:
        value = -100000000
        for i, n in enumerate(board):
            if n == ' ':
                board[i] = 'O'
                minimaxValue = minimax(board, depth+1, False)
                if(value < minimaxValue):
                    value = minimaxValue
                board[i] = ' '
        return value
    else:
        value = 100000000
        for i, n in enumerate(board):
            if n == ' ':
                board[i] = 'X'
                minimaxValue = minimax(board, depth+1, True)
                if(value > minimaxValue):
                    value = minimaxValue
                board[i] = ' '
        return value
state = [' ', ' ', ' ', 
         ' ', ' ', ' ', 
         ' ', ' ', ' ']
while not (is_board_full(state) or check_win(state, 'X') or check_win(state, 'O')):
    print_board(state)
    move = input("Enter a number 0-8 as your next move: ")
    if(move.isdigit() and int(move) >= 0 and int(move) <= 8 and state[int(move)] == ' '):
        state[int(move)] = 'X'
        value = -10000
        bestMove = 0
        for i, n in enumerate(state):
            if n == ' ':
                state[i] = 'O'
                score = minimax(state, 0, False)
                state[i] = ' '
                if(score > value):
                    value = score
                    bestMove = i
        state[bestMove] = 'O'
    else:
        print("Invalid Move")
print_board(state)
if(check_win(state, 'X')):
    print("You Won! :D")
elif(check_win(state, 'O')):
    print("You Lost! :(")
else:
    print("You Tied!")