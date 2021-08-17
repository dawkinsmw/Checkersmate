from checkersmate.rules.utils import *
import checkersmate.rules.simple_move as sm
import checkersmate.rules.jump_move as jm


def legal_moves(game):
    '''Takes a checkersmate game, 
    returns a touple with a flag for whether a capture will take place 
    and list of boards that reflect legal states after the current move'''
    legal_moves = jm.legal_moves(game)
    if len(legal_moves)==0:
        legal_moves = sm.legal_moves(game)
        return False, legal_moves
    else:
        return True, legal_moves