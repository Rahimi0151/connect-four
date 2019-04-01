import tkinter
from Board import Board
from Player import Player

class Game:
    def __init__(self,master):
        self.master = master
        self.app_frame = tkinter.Frame(self.master , bg='white')
        self.app_frame.pack(fill=tkinter.BOTH, expand = True)
        self.player1, self.player2, self.board = self.create_game()


        self.player1.add_to_column(1)
        self.player2.add_to_column(1)
        self.player1.add_to_column(1)
        self.player2.add_to_column(1)
        self.player1.add_to_column(1)
        self.player2.add_to_column(2)
        self.player1.add_to_column(2)
        self.player2.add_to_column(2)
        self.player1.add_to_column(3)
        self.player2.add_to_column(2)


        self.build_grid()
        self.update_board()
    
    def create_game(self):
        player1 = Player(1)
        player2 = Player(2)
        my_board = Board([player1, player2])
        player1.config(board=my_board)
        player2.config(board=my_board)
        return player1, player2, my_board

    def update_board(self):
        for x in range(len(self.board.board)):
            for y in range(len(self.board.board[0])):
                piece = tkinter.Label(
                    master = self.app_frame,
                    text = self.board.board[x][y]
                )
                piece.grid(
                    row = x,
                    column = y,
                    sticky = 'news',
                    padx = 10,
                    pady = 10,
                )

    def build_grid(self):
        self.app_frame.columnconfigure(0, weight=1)
        self.app_frame.columnconfigure(1, weight=1)
        self.app_frame.columnconfigure(2, weight=1)
        self.app_frame.columnconfigure(3, weight=1)
        self.app_frame.columnconfigure(4, weight=1)
        self.app_frame.columnconfigure(5, weight=1)
        self.app_frame.columnconfigure(6, weight=1)
        self.app_frame.columnconfigure(7, weight=1)
        self.app_frame.rowconfigure(0, weight=1)
        self.app_frame.rowconfigure(1, weight=1)
        self.app_frame.rowconfigure(2, weight=1)
        self.app_frame.rowconfigure(3, weight=1)
        self.app_frame.rowconfigure(4, weight=1)
        self.app_frame.rowconfigure(5, weight=1)
        self.app_frame.rowconfigure(6, weight=1)
        self.app_frame.rowconfigure(7, weight=1)


root = tkinter.Tk()
Game(master=root)
root.mainloop()




