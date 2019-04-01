import pytest
from Board import Board
from Player import Player


def create_game():
    player1 = Player(1)
    player2 = Player(2)
    my_board = Board([player1, player2])
    player1.config(board=my_board)
    player2.config(board=my_board)
    return player1, player2, my_board


    player1, player2, board = create_game()


def test_game_has_a_7_by_6_board():
    player1, player2, board = create_game()

    # it has 6 rows...
    assert len(board.board) == 6
    # with 7 column each
    for i in board.board:
        assert len(i) == 7


def test_you_cant_add_to_a_column_that_dows_not_exist():
    player1, player2, board = create_game()

    with pytest.raises(Exception):
        board.add_to_column(100, player2)

def test_you_cant_add_to_a_column_that_is_full():
    player1, player2, board = create_game()

    with pytest.raises(Exception):
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)
        player1.add_to_column(1)
        player2.add_to_column(1)




