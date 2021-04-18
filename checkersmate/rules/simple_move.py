from checkersmate.rules.utils import row_diff

# Simple moves
def update_board(game,i,j):
    new_board = game.board.copy()
    new_board[i] = 0
    new_board[j] = game.board[i]
    return new_board

def legal_moves_given_square(game,i):
    legal_moves = []
    base,left,right,back_left,back_right = i, i+3+i//4%2, i+4+i//4%2, i-4-(i//4+1)%2, i-3-(i//4+1)%2
    if game.board[base] >= 1:
        if (left <= 31):
            if (row_diff(base,left)==1) & (game.board[left]==0):
                legal_moves.append(update_board(game,base,left))
        if (right <= 31):
            if (row_diff(base,right)==1) & (game.board[right]==0):
                legal_moves.append(update_board(game,base,right)) 
    if game.board[base] == 2:
        if (back_left >= 0):
            if (row_diff(base,back_left)==-1) & (game.board[back_left]==0):
                legal__moves.append(update_board(game,base,back_left))
        if (back_right >= 0):
            if (row_diff(base,back_right)==-1) & (game.board[back_right]==0):
                legal_moves.append(update_board(game,base,back_right)) 
    return legal_moves

def legal_moves(game):
    legal_moves = []
    for i in range(32):
        legal_moves.extend(legal_moves_given_square(game,i))
    return legal_moves

