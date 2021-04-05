
def legal_moves(game):
    legal_moves = legal_jumps(game)
    if len(legal_moves)==0:
        legal_moves = legal_simple_moves(game)
    return legal_moves

# Utilities 
def row_diff(x,y):
    return (y//4) - (x//4)


# Simple moves
def legal_simple_moves(game):
    legal_simple_moves = []
    for i in range(32):
        legal_simple_moves.extend(potential_simple_move(game,i))


def update_simple_move(game,i,j):
    new_board = game.board.copy()
    new_board[i] = 0
    new_board[j] = game.board[i]
    return new_board

def potential_simple_move(game,i):
        legal_simple_moves = []
        base,left,right,back_left,back_right = i, i+3+i//4%2, i+4+i//4%2, i-4-(i//4+1)%2, i-3-(i//4+1)%2
        if game.board[base] >= 1:
            if (left <= 31):
                if (row_diff(base,left)==1) & (game.board[left]==0):
                    legal_simple_moves.append(update_simple_move(game,base,left))
            if (right <= 31):
                if (row_diff(base,right)==1) & (game.board[right]==0):
                    legal_simple_moves.append(update_simple_move(game,base,right)) 
        if game.board[base] == 2:
            if (back_left >= 0):
                if (row_diff(base,back_left)==-1) & (game.board[back_left]==0):
                    legal_simple_moves.append(update_simple_move(game,base,back_left))
            if (back_right >= 0):
                if (row_diff(base,back_right)==-1) & (game.board[back_right]==0):
                    legal_simple_moves.append(update_simple_move(game,base,back_right)) 
        return legal_simple_moves



# Jumps
def update_jump(game,i,s,j):
    new_board = game.board.copy()
    new_board[i] = 0
    new_board[s] = 0
    new_board[j] = game.board[i]
    return new_board

def legal_jumps(game,i):
    legal_jumps = []
    base = i
    left,right,back_left,back_right = i+7,i+9,i-9,i-7
    left_skip,right_skip,back_left_skip,back_right_skip = i+3+i//4%2, i+4+i//4%2, i-4-(i//4+1)%2, i-3-(i//4+1)%2
    for i in range(32):
        if game.board[base] >= 1:
            if (left <= 31):
                if (row_diff(base,left)==2) & (game.board[left]==0) & (game.board[left_skip]<0):
                    legal_jumps.append(update_jump(game,base,left_skip,left))
            if (right <= 31):
                if (row_diff(base,right)==2) & (game.board[right]==0) & (game.board[right_skip]<0):
                    legal_jumps.append(update_jump(game,base,right_skip,right)) 
        if game.board[base] == 2:
            if (back_left >= 0):
                if (row_diff(base,back_left)==-2) & (game.board[back_left]==0) & (game.board[back_left_skip]<0):
                    legal_jumps.append(update_jump(game,base,back_left_skip,back_left))
            if (back_right >= 0):
                if (row_diff(base,back_right)==-2) & (game.board[back_right]==0) & (game.board[back_right_skip]<0):
                    legal_jumps.append(update_jump(game,base,back_right_skip,back_right)) 
        return legal_jumps
