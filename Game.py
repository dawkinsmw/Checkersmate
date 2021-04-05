from Checkersmate.Display import print_turn, print_piece, print_board

class Game():
    def __init__(self,
    board=[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1],
    turn=1,
    msc=0
    ):
        self.board = board
        self.turn = turn
        self.msc = msc

    def __str__(self):
	    return f''' ___________Checkersmate____________
    {print_turn(self.turn)}'s turn 
{print_board(self.board,self.turn)}'''	

    def copy_game(self):
        return Game(self.board,self.turn,self.msc)