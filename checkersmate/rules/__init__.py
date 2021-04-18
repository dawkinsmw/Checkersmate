from checkersmate.rules.utils import *
import checkersmate.rules.simple_move as s
import checkersmate.rules.jump as j


def legal_moves(game):
    legal_moves = j.legal_moves(game)
    if len(legal_moves)==0:
        legal_moves = s.legal_moves(game)
    return legal_moves