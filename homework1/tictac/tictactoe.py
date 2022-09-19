from copy import deepcopy
from field import Field

CHANGE = {"x": "o", "o": "x"}


class Game:
    def __init__(self, rows, columns):
        self.not_over = True
        self.field = Field(rows, columns)
        self.turn = "x"
        self.winner = None

    def is_not_over(self):
        return self.not_over

    def set_turn(self, turn):
        self.turn = turn

    def print_field(self):
        return self.field.print_field()

    def make_opponent_turn(self, row, column):
        self.field.set_value(row - 1, column - 1, self.turn)
        self.chek_if_over(row - 1, column - 1)
        self.change_turn()

    def change_turn(self):
        self.turn = CHANGE[self.turn]

    def chek_if_over(self, row, col):
        if self.field.check_if_over(row, col):
            self.winner = "1"
            if self.turn == "o":
                self.winner = "2"
        if self.field.check_if_draw():
            self.winner = "draw"
        if self.winner:
            self.not_over = False

    def present_winner(self):
        if self.winner == "draw":
            return "There is no winner, it's a draw!"
        return f"The winner is {self.winner} player!"

    def turn_is_not_available(self, row, column):
        if self.field.data[row - 1][column - 1] != " ":
            return True
        return False

    def make_my_turn(self):
        if not self.not_over:
            return
        available_moves = set()
        for i in range(self.field.row):
            for j in range(self.field.column):
                if self.field.data[i][j] == " ":
                    available_moves.add((i, j))
        _, res = find_best_turn(self.field, available_moves, True, self.turn)
        self.field.set_value(res[0], res[1], self.turn)
        self.chek_if_over(res[0], res[1])
        self.change_turn()


def find_best_turn(field, available_moves, is_my_turn, my_char, depth=0):
    if depth == 5:
        return (-1 if is_my_turn else 1), (None, None)
    best_val = None
    res = (None, None)
    for (i, j) in deepcopy(available_moves):
        if field.data[i][j] == " ":
            field.set_value(i, j, my_char if is_my_turn else CHANGE[my_char])
            available_moves.discard((i, j))
            if field.check_if_over(i, j):
                field.set_value(i, j, " ")
                available_moves.add((i, j))
                return 1 if is_my_turn else -1, (i, j)
            val = find_best_turn(field, available_moves, not is_my_turn, my_char, depth + 1)[0]
            available_moves.add((i, j))
            field.set_value(i, j, " ")
            if is_my_turn and (not best_val or val > best_val):
                best_val = val
                res = (i, j)
            if not is_my_turn and (not best_val or val < best_val):
                best_val = val
                res = (i, j)
    if not best_val:
        return 0, res
    return best_val, res


def tic_tac_toe(optional_rows=None, optional_columns=None, optional_turn=None, optional_game_progress=None,
                is_testing=False):
    if is_testing:
        rows = optional_rows
        columns = optional_columns
    else:
        rows = int(input("Enter number of rows\n"))
        columns = int(input("Enter number of columns\n"))
    if rows != columns or rows <= 0 or columns <= 0:
        return "The field must to be square and positive!"
    game = Game(rows, columns)
    if is_testing:
        turn = optional_turn
    else:
        turn = input("Select your turn 1 or 2\n")
    if turn not in ["1", "2"]:
        return "Turn must be 1 or 2!"
    fields = list()
    if turn == "2":
        game.make_my_turn()
        fields.append(game.print_field())
        if not is_testing:
            print(fields[-1])
    number_of_turns = 0
    while game.is_not_over():
        if is_testing:
            row, column = optional_game_progress[number_of_turns]
        else:
            row = int(input("Select a row\n"))
            column = int(input("Select a column\n"))
        if column <= 0 or row <= 0 or row > rows or column > columns or game.turn_is_not_available(row, column):
            print("Incorrect row or column\n")
        else:
            game.make_opponent_turn(row, column)
            game.make_my_turn()
            fields.append(game.print_field())
            if not is_testing:
                print(fields[-1])
        number_of_turns += 1
    return game.present_winner(), fields


if __name__ == "__main__":
    result, fields = tic_tac_toe()
    print(result)
