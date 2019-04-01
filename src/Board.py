class Board():

    def __init__(self, players):
        self.board = None
        self.create_board()
        self.players = players
        self.turn = self.players[0]

    def create_board(self):
        self.board = [[None for i in range(7)] for j in range(6)]

    def check_for_index_out_of_range(self, column):
        if column > len(self.board[0]):
            raise Exception("invalid move: column does not exist")

    def toggle_turn(self):
        if self.turn == self.players[0]:
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]

    def check_for_right_player(self, player):
        if not self.turn == player:
            raise Exception("invalid move: it's not your turn")

    # def check_for_overflow(self , column):
    #     # if self.board[column-1][0] in [self.players[0].number,self.players[1].number]:
    #     #     raise Exception("invalid move: column is already full")

    #     for x in self.board:
    #         if x[column] is not None:
    #             if x == len(self.board)-1:
    #                 raise Exception("invalid move: column is already full")

    def add_to_column(self, column, player):
        self.check_for_index_out_of_range(column)
        self.check_for_right_player(player)
        # self.check_for_overflow(column)
        # TODO: get rid of this try/catch block and exchange it with check_for_overflow method
        try:
            for x in range(len(self.board)+1):
                if x == len(self.board):
                    raise Exception("invalid move: column is already full")
                if self.board[x][column] is None:
                    self.board[x][column] = player.number
                    break
            self.toggle_turn()
            self.won(player)
        except:
            raise Exception("invalid move: column is already full")

    def won(self, player):
        self.check_for_horizontal_match(player)
        self.check_for_vertical_match(player)
        self.check_for_diagonal_match(player)


    def check_for_horizontal_match(self,player):
        items = 0

        for x in self.board:
            for y in x:
                if y == player.number:
                    items += 1
                else:
                    items = 0
                if items == 4:
                    player.won = True
                    return
    
    def check_for_vertical_match(self, player):
        items = 0

        for y in range(len(self.board[0]) - 1):
            for x in range(len(self.board) - 1):
                if self.board[x][y] == player.number:
                    items += 1
                else:
                    items = 0
                if items == 4:
                    player.won = True
                    return

    def check_for_diagonal_match(self,player):

        # searching for four diagonal match in one direction
        for y in range(len(self.board[0]) - 4):
            for x in range(len(self.board) - 4):
                if (self.board[x    ][y    ] ==
                    self.board[x + 1][y + 1] ==
                    self.board[x + 2][y + 2] ==
                    self.board[x + 3][y + 3] == player.number):
                        player.won = True

        # searching for four diagonal match in other direction
        for y in range(4,len(self.board[0])):
            for x in range(len(self.board) - 4):
                if (self.board[x    ][y    ] ==
                    self.board[x + 1][y - 1] ==
                    self.board[x + 2][y - 2] ==
                    self.board[x + 3][y - 3] == player.number):
                    player.won = True
                    return

