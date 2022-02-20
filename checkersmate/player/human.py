from checkersmate.game import Game

class human_player():
    def __init__(self,tempfile='hp_move.txt'):
        self.f = tempfile

    def select_move(self,boards):
        '''Given a list of boards, returns a randomly chosen board'''
        print(f"###### Move Options ######", file=open(self.f, 'w'))
        for i,b in enumerate(boards):
            print(f"##-- Board {i} --##", file=open(self.f, 'a'))
            print(Game(b), file=open(self.f, 'a'))
            print("\n \n", file=open(self.f, 'a'))
        move = int(input("Choose move: "))
        return boards[move]