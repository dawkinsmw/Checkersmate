from checkersmate.display import print_turn, print_piece, print_board
from checkersmate.player.random import random_player
from checkersmate.rules import legal_moves
from time import sleep

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
            self.output_df = pd.DataFrame(columns=[i for i in range(32)] + ["result"])

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
        if(self.output_file):
            self.output_df.loc[len(self.output_df)] = chosen_board + [self.turn]
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
            if(not self.silent and result==1): 
                sleep(1)
                print(self)
        if(result==-1): 
            if(not self.silent): print(f"!!{print_turn(-self.turn)} wins!!")
            if(self.output_file):
                self.output_df['result'] = self.output_df['result'] * (-self.turn) 
                self.output_df.to_csv(self.output_file,header=False,index=False, mode='a')
            return -self.turn
        if(result==0): 
            if(not self.silent): print(f"__drawn game__")
            if(self.output_file):
                self.output_df['result'] = 0
                self.output_df.to_csv(self.output_file,header=False,index=False, mode='a')
            return 0