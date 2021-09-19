from checkersmate.display import print_turn, print_piece, print_board
from checkersmate.player.random import random_player
from checkersmate.rules import legal_moves

class Game():
    def __init__(self,
    board=[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    turn=1,
    msc=0,
    msc_limit=50,
    p1=random_player(),
    p2=random_player(),
    silent=False,
    output=False
    ):
        self.board = board
        self.turn = turn
        self.msc = msc
        self.msc_limit = msc_limit
        self.players = {1:p1,-1:p2}
        self.silent = silent
        self.output_file = output
        if(self.output_file is not None):
            import pandas as pd
            self.output_df = pd.DataFrame(columns=[i for i in range(32)])

    def __str__(self):
	    return f''' ___________Checkersmate____________
    {print_turn(self.turn)}'s turn 
{print_board(self)}'''	

    def copy_game(self):
        return Game(self.board,self.turn,self.msc)

    def change_turn(self):
        self.turn = -1 * self.turn
        self.board = [-p for p in self.board[::-1]]

    def next_move(self):
        capture_flag, potential_boards = legal_moves(self) 
        if(potential_boards==[]): return -1
        chosen_board = self.players[self.turn].select_move(potential_boards)
        self.board = chosen_board
        self.change_turn()
        if(capture_flag):
            self.msc = 0
        else:
            self.msc += 1
        if(self.msc >= self.msc_limit):
            return 0
        return 1

    def play(self):
        if(not self.silent): print(self)
        result = 1
        while(result==1): 
            result = self.next_move()
            if(not self.silent and result==1): print(self)
            if(self.output and result==1):
                self.output_df.loc[len(self.output_df)] = self.board + [None]
        if(result==-1): 
            if(not self.silent): print(f"!!{print_turn(-self.turn)} wins!!")
            self.output_df['result'] = [self.turn*(2*(x%2-0.5)) for x in range(len(self.output_df))]
            self.output_df.to_csv(self.output_file)
            return -self.turn
        if(result==0): 
            if(not self.silent): print(f"__drawn game__")
            self.output_df['result'] = 0
            self.output_df.to_csv(self.output_file)
            return 0