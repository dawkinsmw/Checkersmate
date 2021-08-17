from checkersmate.rules.utils import row_diff

# Jumps
def update_board(game,i,s,j):
    '''Takes a checkersmate game and an old square, a new square and a skip square,
    returns a board with the piece on the old square moved to the new square and the skiped square emptied'''
    new_board = game.board.copy()
    new_board[i] = 0
    new_board[s] = 0
    if(j>=28):
        new_board[j] = 2
    else:
        new_board[j] = game.board[i]
    return new_board

def legal_moves_given_square(game,i):
    '''Takes a checkersmate game and a particular square, 
    returns a list of boards that refelct legal states after the current move, 
    limited to jump moves using the piece on that square'''
    legal_jumps = []
    base = i
    left,right,back_left,back_right = i+7,i+9,i-9,i-7
    left_skip,right_skip,back_left_skip,back_right_skip = i+3+i//4%2, i+4+i//4%2, i-4-(i//4+1)%2, i-3-(i//4+1)%2
    for i in range(32):
        if game.board[base] >= 1:
            if (left <= 31):
                if (row_diff(base,left)==2) & (game.board[left]==0) & (game.board[left_skip]<0):
                    legal_jumps.append(update_board(game,base,left_skip,left))
            if (right <= 31):
                if (row_diff(base,right)==2) & (game.board[right]==0) & (game.board[right_skip]<0):
                    legal_jumps.append(update_board(game,base,right_skip,right)) 
        if game.board[base] == 2:
            if (back_left >= 0):
                if (row_diff(base,back_left)==-2) & (game.board[back_left]==0) & (game.board[back_left_skip]<0):
                    legal_jumps.append(update_board(game,base,back_left_skip,back_left))
            if (back_right >= 0):
                if (row_diff(base,back_right)==-2) & (game.board[back_right]==0) & (game.board[back_right_skip]<0):
                    legal_jumps.append(update_board(game,base,back_right_skip,back_right)) 
        return legal_jumps

def legal_moves(game):
    '''Takes a checkersmate game, 
    returns a list of boards that refelct legal states after the current move, 
    limited to jump moves'''
    legal_moves_list = []
    for i in range(32):
        legal_moves_list.extend(legal_moves_given_square(game,i))
    return legal_moves_list
