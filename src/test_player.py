from Board import Board
from Player import Player
import pytest


def create_game():
    player1 = Player(1)
    player2 = Player(2)
    my_board = Board([player1, player2])
    player1.config(board=my_board)
    player2.config(board=my_board)
    return player1, player2, my_board


def test_player_has_color():
    player1, player2, board = create_game()

    assert player1.number is 1


def test_payer_can_add_piece_to_a_column():
    player1, player2, board = create_game()

    player1.add_to_column(2)
    assert board.board[0][2] is 1


def test_playerscan_win_horizontally():
    player1, player2, board = create_game()
    assert player1.won is False
    assert player2.won is False
    # 1
    player1.add_to_column(1)
    assert player1.won is False
    player2.add_to_column(1)
    assert player2.won is False
    # 2
    player1.add_to_column(2)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 3
    player1.add_to_column(3)
    assert player1.won is False
    player2.add_to_column(3)
    assert player2.won is False
    # 4
    player1.add_to_column(4)
    assert player1.won is True
    player2.add_to_column(4)
    assert player2.won is True


def test_players_can_win_vertically():
    player1, player2, board = create_game()
    assert player1.won is False
    assert player2.won is False
    # 1
    player1.add_to_column(1)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 2
    player1.add_to_column(1)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 3
    player1.add_to_column(1)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 4
    player1.add_to_column(1)
    assert player1.won is True
    player2.add_to_column(2)
    assert player2.won is True

def test_players_can_win_diagonally():
    player1, player2, board = create_game()
    assert player1.won is False
    assert player2.won is False
    # 1
    player1.add_to_column(1)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 2
    player1.add_to_column(2)
    assert player1.won is False
    player2.add_to_column(3)
    assert player2.won is False
    # 3
    player1.add_to_column(3)
    assert player1.won is False
    player2.add_to_column(4)
    assert player2.won is False
    # 4
    player1.add_to_column(3)
    assert player1.won is False
    player2.add_to_column(4)
    assert player2.won is False
    # 5
    player1.add_to_column(4)
    assert player1.won is False
    player2.add_to_column(5)
    assert player2.won is True
    # 6
    player1.add_to_column(4)
    assert player1.won is True
    player2.add_to_column(5)
    assert player2.won is True

def test_players_can_win_diagonally_2():
    player1, player2, board = create_game()
    assert player1.won is False
    assert player2.won is False
    # 1
    player1.add_to_column(5)
    assert player1.won is False
    player2.add_to_column(4)
    assert player2.won is False
    # 2
    player1.add_to_column(4)
    assert player1.won is False
    player2.add_to_column(3)
    assert player2.won is False
    # 3
    player1.add_to_column(3)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 4
    player1.add_to_column(3)
    assert player1.won is False
    player2.add_to_column(2)
    assert player2.won is False
    # 5
    player1.add_to_column(2)
    assert player1.won is False
    player2.add_to_column(1)
    assert player2.won is True
    # 6
    player1.add_to_column(2)
    assert player1.won is True
    player2.add_to_column(1)
    assert player2.won is True

# TODO: add the apropiate function for this:
#       the last test wont work if these are  in the same order:
#       [1,4][2,3][3,2][4,1]
# def test_players_can_win_diagonally_3():
#     player1, player2, board = create_game()
#     assert player1.won is False
#     assert player2.won is False
#     # 1
#     player1.add_to_column(4)
#     assert player1.won is False
#     player2.add_to_column(3)
#     assert player2.won is False
#     # 2
#     player1.add_to_column(3)
#     assert player1.won is False
#     player2.add_to_column(2)
#     assert player2.won is False
#     # 3
#     player1.add_to_column(2)
#     assert player1.won is False
#     player2.add_to_column(1)
#     assert player2.won is False
#     # 4
#     player1.add_to_column(2)
#     assert player1.won is False
#     player2.add_to_column(1)
#     assert player2.won is False
#     # 5
#     player1.add_to_column(1)
#     assert player1.won is False
#     player2.add_to_column(6)
#     assert player2.won is True
#     # 6
#     player1.add_to_column(1)
#     assert player1.won is True
#     player2.add_to_column(6)
#     assert player2.won is True







