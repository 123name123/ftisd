class Field:
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.data = [[" "] * column for i in range(row)]
        self.game_over_score = min(row, 5)

    def set_value(self, i, j, val):
        self.data[i][j] = val

    def print_field(self):
        result_field = ""
        for i in range(self.row):
            for j in range(self.column):
                result_field += "|" + self.data[i][j]
            result_field += "|\n"
        return result_field

    def check_if_draw(self):
        for row in self.data:
            if " " in row:
                return False
        return True

    def check_if_over(self, row, col):
        first_win = "x" * self.game_over_score
        second_win = "o" * self.game_over_score
        temp = ""
        for it in self.data[row]:
            temp += it
        if first_win in temp or second_win in temp:
            return True
        temp = ""
        for i in range(self.row):
            temp += self.data[i][col]
        if first_win in temp or second_win in temp:
            return True
        temp = ""
        i, j = row, col
        while i >= 0 and j >= 0:
            temp = self.data[i][j] + temp
            i -= 1
            j -= 1
        i, j = row + 1, col + 1
        while i < self.row and j < self.column:
            temp += self.data[i][j]
            i += 1
            j += 1
        if first_win in temp or second_win in temp:
            return True
        temp = ""
        i, j = row, col
        while i >= 0 and j < self.column:
            temp = self.data[i][j] + temp
            i -= 1
            j += 1
        i, j = row + 1, col - 1
        while i < self.row and j >= 0:
            temp += self.data[i][j]
            i += 1
            j -= 1
        if first_win in temp or second_win in temp:
            return True
        return False
