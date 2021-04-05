from Checkersmate.Game import Game
# from Checkersmate.Rules import legal_moves
from Checkersmate.Result import check_result

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
        result = check_result(new_state)
        # current_state = new_state.change_turn()