from random import randint

class random_player():

    def select_move(self,boards):
        '''Given a list of boards, returns a randomly chosen board'''
        return boards[randint(0,len(boards)-1)]