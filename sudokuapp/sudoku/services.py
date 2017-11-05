
class SudokuBoard(object):

    DIGITS = set(range(1, 10))

    def __init__(self, values):
        self.values = values

    def row(self, n):
        return self.values[n]

    def rows(self):
        return self.values

    def cols(self):
        return [self.col(i) for i in xrange(9)]

    def col(self, n):
        return [self.values[i][n] for i in xrange(len(self.values))]

    def groups(self):
        return [self.group(i) for i in xrange(9)]

    def group(self, n):
        start_r = (n / 3) * 3
        start_c = n * 3 % 9
        values = []
        for row in xrange(start_r, start_r + 3):
            for col in xrange(start_c, start_c + 3):
                values.append(self.values[row][col])
        return values

    def is_correct(self):
        for row in self.rows():
            if self.DIGITS - set(row):
                return False
        for col in self.cols():
            if self.DIGITS - set(col):
                return False
        for group in self.groups():
            if self.DIGITS - set(group):
                return False
        return True
