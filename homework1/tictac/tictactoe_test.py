from unittest import TestCase, main
from tictactoe import tic_tac_toe, Field


class TicTacToeTest(TestCase):
    def test_field(self):
        field = Field(3, 3)
        field.set_value(0, 0, "x")
        self.assertEqual(field.check_if_over(0, 0), False)
        field.set_value(1, 1, "x")
        self.assertEqual(field.check_if_over(1, 1), False)
        field.set_value(1, 2, "o")
        self.assertEqual(field.check_if_over(1, 2), False)
        field.set_value(0, 2, "o")
        self.assertEqual(field.check_if_over(0, 2), False)
        field.set_value(2, 2, "x")
        self.assertEqual(field.check_if_over(2, 2), True)
        right_answer = "|x| |o|\n| |x|o|\n| | |x|\n"
        self.assertEqual(field.print_field(), right_answer)
        self.assertEqual(field.check_if_draw(), False)
        field.set_value(0, 1, "x")
        field.set_value(1, 0, "x")
        field.set_value(2, 1, "x")
        field.set_value(2, 0, "x")
        self.assertEqual(field.check_if_draw(), True)

    def test_wrong_size(self):
        self.assertEqual(tic_tac_toe(-1, 2, "1", [], True), "The field must to be square and positive!")
        self.assertEqual(tic_tac_toe(3, 2, "1", [], True), "The field must to be square and positive!")
        self.assertEqual(tic_tac_toe(3, -2, "1", [], True), "The field must to be square and positive!")

    def test_wrong_turn(self):
        self.assertEqual(tic_tac_toe(3, 3, "0", [], True), "Turn must be 1 or 2!")
        self.assertEqual(tic_tac_toe(3, 3, "3", [], True), "Turn must be 1 or 2!")

    def test_lose(self):
        first_right_answer = ("The winner is 2 player!", ['|x| | |\n| |o| |\n| | | |\n',
                                                          '|x| | |\n|x|o| |\n|o| | |\n',
                                                          '|x|x|o|\n|x|o| |\n|o| | |\n'])
        self.assertEqual(tic_tac_toe(3, 3, "1", [(1, 1), (2, 1), (1, 2)], True), first_right_answer)

    def test_draw(self):
        right_answer = ("There is no winner, it's a draw!", ['|x| | |\n| |o| |\n| | | |\n',
                                                             '|x|o|x|\n| |o| |\n| | | |\n',
                                                             '|x|o|x|\n|o|o| |\n| |x| |\n',
                                                             '|x|o|x|\n|o|o|x|\n| |x|o|\n',
                                                             '|x|o|x|\n|o|o|x|\n|x|x|o|\n'])
        self.assertEqual(tic_tac_toe(3, 3, "1", [(1, 1), (1, 3), (3, 2), (2, 3), (3, 1)], True),
                         right_answer)


if __name__ == "__main__":
    main()
