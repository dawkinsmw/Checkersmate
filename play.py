from checkersmate.game import Game
# from checkersmate.Rules import legal_moves

if __name__ == '__main__':
    # players = {1:Player(),-1:Player()}
    result = 0
    current_state = Game()
    while result==0:
        print(current_state)
        # potential_states = legal_moves(current_state) 
        # new_state = players[current_state.turn].choose_move(potential_new_states)
        new_state = current_state
        # state.msc update
        # current_state = new_state.change_turn()