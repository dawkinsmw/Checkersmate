from checkersmate.rules.utils import row_diff

# Jumps
def update_board(board,i,s,j):
    '''Takes a checkersmate game board and an old square, a new square and a skip square,
    returns a board with the piece on the old square moved to the new square and the skiped square emptied'''
    new_board = board.copy()
    new_board[i] = 0
    new_board[s] = 0
    if(j>=28):
        new_board[j] = 2
    else:
        new_board[j] = board[i]
    return new_board

def single_jump_moves_given_square(board,base):
    '''Takes a checkersmate game board and a particular square, 
    returns a list of boards that refelct legal states after the current move, 
    limited to jump moves using the piece on that square'''
    legal_moves_list = []
    if board[base] >= 1:
        left,right,back_left,back_right = base+7,base+9,base-9,base-7
        left_skip,right_skip,back_left_skip,back_right_skip = base+3+base//4%2, base+4+base//4%2, base-4-(base//4+1)%2, base-3-(base//4+1)%2
        if (left <= 31):
            if (row_diff(base,left)==2) & (board[left]==0) & (board[left_skip]<0):
                legal_moves_list.append((update_board(board,base,left_skip,left),left))
        if (right <= 31):
            if (row_diff(base,right)==2) & (board[right]==0) & (board[right_skip]<0):
                legal_moves_list.append((update_board(board,base,right_skip,right),right)) 
    if board[base] == 2:
        if (back_left >= 0):
            if (row_diff(base,back_left)==-2) & (board[back_left]==0) & (board[back_left_skip]<0):
                legal_moves_list.append((update_board(board,base,back_left_skip,back_left),back_left))
        if (back_right >= 0):
            if (row_diff(base,back_right)==-2) & (board[back_right]==0) & (board[back_right_skip]<0):
                legal_moves_list.append((update_board(board,base,back_right_skip,back_right),back_right)) 
    return legal_moves_list


def recursive_jump_moves_given_square(board,base):
    new_boards = single_jump_moves_given_square(board,base)
    if(new_boards==[]):
        return board
    else:
        for new_board,new_base in new_boards:
            return recursive_jump_moves_given_square(new_board,new_base)
    

def legal_moves_given_square(board,base):
    legal_moves_list = []
    for new_board, j in single_jump_moves_given_square(board,base):
        legal_moves_list.append(recursive_jump_moves_given_square(new_board,j))
    return legal_moves_list


def legal_moves(game):
    '''Takes a checkersmate game, 
    returns a list of boards that refelct legal states after the current move, 
    limited to jump moves'''
    legal_moves_list = []
    for i in range(32):
        legal_moves_list.extend(legal_moves_given_square(game.board,i))
    return legal_moves_list
