from random import randint

class random_player():

    def select_move(boards):
        return boards[randint(0,len(boards)-1)]