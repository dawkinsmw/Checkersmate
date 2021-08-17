from checkersmate.rules.utils import row_diff

# Simple moves
def update_board(game,i,j):
    '''Takes a checkersmate game and an old and new square,
    returns a board with the piece on the old square moved to the new square'''
    new_board = game.board.copy()
    new_board[i] = 0
    new_board[j] = game.board[i]
    return new_board

def legal_moves_given_square(game,i):
    '''Takes a checkersmate game and a particular square, 
    returns a list of boards that refelct legal states after the current move, 
    limited to simple moves using the piece on that square'''
    legal_moves_list = []
    base,left,right,back_left,back_right = i, i+3+i//4%2, i+4+i//4%2, i-4-(i//4+1)%2, i-3-(i//4+1)%2
    if game.board[base] >= 1:
        if (left <= 31):
            if (row_diff(base,left)==1) & (game.board[left]==0):
                legal_moves_list.append(update_board(game,base,left))
        if (right <= 31):
            if (row_diff(base,right)==1) & (game.board[right]==0):
                legal_moves_list.append(update_board(game,base,right)) 
    if game.board[base] == 2:
        if (back_left >= 0):
            if (row_diff(base,back_left)==-1) & (game.board[back_left]==0):
                legal_moves_list.append(update_board(game,base,back_left))
        if (back_right >= 0):
            if (row_diff(base,back_right)==-1) & (game.board[back_right]==0):
                legal_moves_list.append(update_board(game,base,back_right)) 
    return legal_moves_list

def legal_moves(game):
    '''Takes a checkersmate game, 
    returns a list of boards that refelct legal states after the current move, 
    limited to simple moves'''
    legal_moves_list = []
    for i in range(32):
        legal_moves_list.extend(legal_moves_given_square(game,i))
    return legal_moves_list

