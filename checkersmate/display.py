    
def print_turn(turn):
    if turn == 1:
        return "red (x)"
    if turn == -1:
        return "white (o)"

def print_piece(piece,turn):
    if piece*turn == 0:
        return " "
    if piece*turn == 1:
        return "x"
    if piece*turn == 2:
        return "x̂"
    if piece*turn == -1:
        return "o"
    if piece*turn == -2:
        return "ô"


def print_board(game):
    if(game.turn==1): 
      board = game.board
    else:
      board = [p for p in game.board[::-1]]
    return f'''  +---+---+---+---+---+---+---+---+
8 |   | {print_piece(board[28],game.turn)} |   | {print_piece(board[29],game.turn)} |   | {print_piece(board[30],game.turn)} |   | {print_piece(board[31],game.turn)} |
  |---+---+---+---+---+---+---+---|   
7 | {print_piece(board[24],game.turn)} |   | {print_piece(board[25],game.turn)} |   | {print_piece(board[26],game.turn)} |   | {print_piece(board[27],game.turn)} |   |
  |---+---+---+---+---+---+---+---|
6 |   | {print_piece(board[20],game.turn)} |   | {print_piece(board[21],game.turn)} |   | {print_piece(board[22],game.turn)} |   | {print_piece(board[23],game.turn)} |
  |---+---+---+---+---+---+---+---|   
5 | {print_piece(board[16],game.turn)} |   | {print_piece(board[17],game.turn)} |   | {print_piece(board[18],game.turn)} |   | {print_piece(board[19],game.turn)} |   |
  |---+---+---+---+---+---+---+---|
4 |   | {print_piece(board[12],game.turn)} |   | {print_piece(board[13],game.turn)} |   | {print_piece(board[14],game.turn)} |   | {print_piece(board[15],game.turn)} |
  |---+---+---+---+---+---+---+---|   
3 | {print_piece(board[8],game.turn)} |   | {print_piece(board[9],game.turn)} |   | {print_piece(board[10],game.turn)} |   | {print_piece(board[11],game.turn)} |   |
  |---+---+---+---+---+---+---+---|
2 |   | {print_piece(board[4],game.turn)} |   | {print_piece(board[5],game.turn)} |   | {print_piece(board[6],game.turn)} |   | {print_piece(board[7],game.turn)} |
  |---+---+---+---+---+---+---+---|
1 | {print_piece(board[0],game.turn)} |   | {print_piece(board[1],game.turn)} |   | {print_piece(board[2],game.turn)} |   | {print_piece(board[3],game.turn)} |   |
  +---+---+---+---+---+---+---+---+
    A   B   C   D   E   F   G   H'''