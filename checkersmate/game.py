from checkersmate.display import print_turn, print_piece, print_board
from checkersmate.player.random import random_player
from checkersmate.rules import legal_moves

class Game():
    def __init__(self,
    board=[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    turn=1,
    msc=0,
    p1=random_player(),
    p2=random_player()
    ):
        self.board = board
        self.turn = turn
        self.msc = msc
        self.players = {1:p1,-1:p2}

    def __str__(self):
	    return f''' ___________Checkersmate____________
    {print_turn(self.turn)}'s turn 
{print_board(self.board,self.turn)}'''	

    def copy_game(self):
        return Game(self.board,self.turn,self.msc)

    def change_turn(self):
        self.turn = -1 * self.turn
        self.board = [-p for p in self.board[::-1]]

    def next_move(self):
        capture_flag, potential_boards = legal_moves(self) 
        chosen_board = self.players[self.turn].select_move(potential_boards)
        self.board = chosen_board
        self.change_turn()
        if(capture_flag):
            self.msc = 0
        else:
            self.msc += 1
        # check_result(self)