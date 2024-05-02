import copy
import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = 0
    o_count = 0
    empty_count = 9

    for row in board:
        for element in row:
            if element == X:
                x_count += 1
                empty_count -= 1 
            elif element == O:
                o_count += 1
                empty_count -= 1
    if x_count > o_count and empty_count != 0:
        return O
    elif x_count <= o_count :
        return X
    if empty_count == 0 :
        return -1
    
    raise NotImplementedError


def actions(board):
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    if len(possible_actions) == 0:
        return -1
    else :
        return possible_actions     
    raise NotImplementedError


def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid move")
    
    new_board = copy.deepcopy(board)
    
    new_board[action[0]][action[1]] = player(board)
    
    return new_board
    raise NotImplementedError


def winner(board):
    for i in board :
        if i.count(X) == 3 :
            return X
        if i.count(O) == 3 :
            return O
    for j in range(3) :
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        if board[0][j] == board[1][j] == board[2][j] == O:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X :
        return X
    if board[2][0] == board[1][1] == board [0][2] == X :
        return X
    if board[0][0] == board[1][1] == board[2][2] == O :
        return O
    if board[2][0] == board[1][1] == board [0][2] == O :
        return O
    return None
        
    raise NotImplementedError


def terminal(board):
    if winner(board) is not None:
        return True
    for row in board :
        if EMPTY in row :
            return False 
    return True    
 
    raise NotImplementedError


def utility(board):
    if winner(board) == X :
        return 1 
    if winner(board) == O :
        return -1
    if winner(board) == None :
        return 0
    raise NotImplementedError

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            break
    return v

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        v = -math.inf
        best_move = None
        for action in actions(board):
            min_val = min_value(result(board, action), -math.inf, math.inf)
            if min_val > v:
                v = min_val
                best_move = action
    else:
        v = math.inf
        best_move = None
        for action in actions(board):
            max_val = max_value(result(board, action), -math.inf, math.inf)
            if max_val < v:
                v = max_val
                best_move = action
    return best_move


    
