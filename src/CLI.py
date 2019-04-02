from Board import Board
from Player import Player


def print_game_board(board):
    for x in reversed(board.board):
        for y in x:
            if y is None:
                print("|", end="\t")
            else:
                print(y, end="\t")
        print()


def create_game():
    player1 = Player(1)
    player2 = Player(2)
    my_board = Board([player1, player2])
    player1.config(board=my_board)
    player2.config(board=my_board)
    return player1, player2, my_board


player1, player2, board = create_game()

while player1.won == player2.won:
    try:
        col = int(input("please enter column number: "))
    except:
        pass
        
    player = board.turn

    try:
        player.add_to_column(col)
    except:
        pass
    print_game_board(board)

if player1.won:
    print("player1 won!")
if player2.won:
    print("player2 won!")


