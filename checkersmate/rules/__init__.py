from checkersmate.rules.utils import *
import checkersmate.rules.simple_move 
import checkersmate.rules.jump


def legal_moves(game):
    legal_moves = jm.legal_jumps(game)
    if len(legal_moves)==0:
        legal_moves = sm.legal_simple_moves(game)
    return legal_moves