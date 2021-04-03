    
def print_turn(turn):
    if turn == 1:
        return "red"
    if turn == -1:
        return "white"

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


def print_board(board,turn):
        return f'''  +---+---+---+---+---+---+---+---+
8 |   | {print_piece(board[28],turn)} |   | {print_piece(board[29],turn)} |   | {print_piece(board[30],turn)} |   | {print_piece(board[31],turn)} |
  |---+---+---+---+---+---+---+---|   
7 | {print_piece(board[24],turn)} |   | {print_piece(board[25],turn)} |   | {print_piece(board[26],turn)} |   | {print_piece(board[27],turn)} |   |
  |---+---+---+---+---+---+---+---|
6 |   | {print_piece(board[20],turn)} |   | {print_piece(board[21],turn)} |   | {print_piece(board[22],turn)} |   | {print_piece(board[23],turn)} |
  |---+---+---+---+---+---+---+---|   
5 | {print_piece(board[16],turn)} |   | {print_piece(board[17],turn)} |   | {print_piece(board[18],turn)} |   | {print_piece(board[19],turn)} |   |
  |---+---+---+---+---+---+---+---|
4 |   | {print_piece(board[12],turn)} |   | {print_piece(board[13],turn)} |   | {print_piece(board[14],turn)} |   | {print_piece(board[15],turn)} |
  |---+---+---+---+---+---+---+---|   
3 | {print_piece(board[8],turn)} |   | {print_piece(board[9],turn)} |   | {print_piece(board[10],turn)} |   | {print_piece(board[11],turn)} |   |
  |---+---+---+---+---+---+---+---|
2 |   | {print_piece(board[4],turn)} |   | {print_piece(board[5],turn)} |   | {print_piece(board[6],turn)} |   | {print_piece(board[7],turn)} |
  |---+---+---+---+---+---+---+---|
1 | {print_piece(board[0],turn)} |   | {print_piece(board[1],turn)} |   | {print_piece(board[2],turn)} |   | {print_piece(board[3],turn)} |   |
  +---+---+---+---+---+---+---+---+
    A   B   C   D   E   F   G   H'''