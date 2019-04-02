import tkinter
from tkinter import messagebox
from Board import Board
from Player import Player


class Game:
    def __init__(self, master):

        self.master = master
        self.app_frame = tkinter.Frame(self.master, bg='white')
        self.app_frame.pack(fill=tkinter.BOTH, expand=True)
        self.create_game()
        self.create_board()
        self.build_grid()
        self.update_board()

    def create_board(self):
        self.push_button = [None for i in range(len(self.board.board[0]))]
        for y in range(len(self.board.board[0])):
            self.push_button[y] = tkinter.Button(self.app_frame, text='put here', command=self.set_adder(y))
            self.push_button[y].grid(column=y, row=(len(self.board.board[0]) - 1), sticky='news')

    def set_adder(self, column):
        switcher = {
            0: self.adder0,
            1: self.adder1,
            2: self.adder2,
            3: self.adder3,
            4: self.adder4,
            5: self.adder5,
            6: self.adder6,
        }
        return switcher[column]

    def create_game(self):
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.board = Board([self.player1, self.player2])
        self.player1.config(board=self.board)
        self.player2.config(board=self.board)

    def check_for_winner(self):
        if self.player1.won:
            messagebox.showinfo('GAME OVER!', 'Player1 Won!')
            self.create_game()
            self.update_board()
        if self.player2.won:
            messagebox.showinfo('GAME OVER!', 'Player2 Won!')
            self.create_game()
            self.update_board()

    def update_board(self):
        REVERSER = len(self.board.board) - 1
        for x in range(len(self.board.board)):
            for y in range(len(self.board.board[0])):
                piece = tkinter.Label(self.app_frame,
                                      text=self.board.board[REVERSER - x][y],
                                      background=self.choose_color(self.board.board[REVERSER - x][y])
                                      )
                piece.grid(row=x, column=y, sticky='news', padx=2, pady=2, )
        self.check_for_winner()

    def choose_color(self, player_number):
        player_colors = {
            None: 'white',
            1: 'red',
            2: 'blue'
        }
        return player_colors[player_number]

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

    def adder0(self):
        self.board.turn.add_to_column(0)
        self.update_board()

    def adder1(self):
        self.board.turn.add_to_column(1)
        self.update_board()

    def adder2(self):
        self.board.turn.add_to_column(2)
        self.update_board()

    def adder3(self):
        self.board.turn.add_to_column(3)
        self.update_board()

    def adder4(self):
        self.board.turn.add_to_column(4)
        self.update_board()

    def adder5(self):
        self.board.turn.add_to_column(5)
        self.update_board()

    def adder6(self):
        self.board.turn.add_to_column(6)
        self.update_board()


root = tkinter.Tk()
Game(master=root)
root.mainloop()
