from Board import Board


class Player:

    def __init__(self, number):
        self.pieces = []
        self.number = number
        self.board = None
        self.won = False

    def config(self, board=None):
        self.board = board

    def check_if_board_is_set(self):
        if not isinstance(self.board, Board):
            raise Exception("Error: you should use config method on this class to add the board")

    def add_to_column(self, column):
        self.check_if_board_is_set()
        self.board.add_to_column(column, self)
