import unittest
from checkersmate.game import Game
from checkersmate.display import print_board
from checkersmate.rules import legal_moves
import checkersmate.rules.simple_move as sm 
from data.sample_boards import sample_boards


class TestSimpleMove(unittest.TestCase):

    def simple_move_test(self,board,square,correct_result):
        print()
        state = Game(sample_boards[board])
        produced_result = sm.legal_moves_given_square(state,square)
        self.assertEqual(len(produced_result),len(correct_result),"incorrect number of legal simple moves")
        for i in range(len(correct_result)):
            if (produced_result[i]!=correct_result[i]):
                print(f"board {i} of {len(correct_result)} is incorrect:")
                print("starting board")
                print(state)
                print("produced board")
                print(Game(produced_result[i],state.turn))
                print("correct board")
                print(Game(correct_result[i],state.turn))
            self.assertEqual(produced_result[i],correct_result[i],"Inspect above boards, correct result not produced")

    def test_start_10(self):
        correct_result = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ]
        self.simple_move_test("start",10,correct_result)

    def test_start_5(self):
        correct_result = []
        self.simple_move_test("start",5,correct_result)

    def test_simple_capture_13(self):
        correct_result = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.simple_move_test("simple_capture",13,correct_result)
    
    def test_simple_king_26(self):
        correct_result = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
        ]
        self.simple_move_test("simple_king",26,correct_result)

    def test_multiple_capture_13(self):
        correct_result = []
        self.simple_move_test("multiple_capture",13,correct_result)

    def test_double_capture_13(self):
        correct_result = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]
        ]
        self.simple_move_test("double_capture",13,correct_result)

    def test_double_v_single_capture_13(self):
        correct_result = []
        self.simple_move_test("double_v_single_capture",13,correct_result)

    def test_king_capture_13(self):
        correct_result = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.simple_move_test("king_capture",13,correct_result)
        
    
if __name__ == '__main__':
    unittest.main()