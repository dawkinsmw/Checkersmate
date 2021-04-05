def check_result(game):
    if check_win(game):
        return 1
    if check_draw(game):
        return 0
    else:
        return None

## Draw
def check_draw(game,n):
    return game.msc > n

## Win
def check_win(game):
    return check_no_opposition_pieces(game) | check_no_opposition_legal_moves(game)
    
def check_no_opposition_pieces(game):
    return sum([p<0 for p in game.board])==0

def check_no_opposition_legal_moves(game):
    