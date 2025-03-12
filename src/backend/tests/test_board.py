from ..src.board import Board
from ..src.error import *
import pytest

@pytest.fixture
def board():
    board = Board(3, 5)
    board.board = [
        [ -1, 0, 1, 2, 2],
        [ -1, 1, 1, 1, 2],
        [  2, 2, 2, 1, 2],
        [  0, 0, 1, 2, 2],
        [  2, 2, 2, 2, 2]]
    return board

def test_get_structure(board):
    assert board._get_structure(0, 0) == { (0, 0), (0, 1) }
    assert board._get_structure(1, 0) == { (1, 0) }
    assert board._get_structure(1, 1) == {(1, 1), (2, 0), (2, 1), (3, 1), (3, 2) }
    assert board._get_structure(0, 2) == { (0, 2), (1, 2), (2, 2) }
    assert board._get_structure(0, 3) == { (0, 3), (1, 3) }
    assert board._get_structure(0, 4) == { (0, 4), (1, 4), (2, 4), (3, 4),
         (4, 4), (4, 0), (4, 3), (4, 2), (3, 0), (4, 1), (3, 3) }

    assert board._get_structure(-1, 0) == set()
    assert board._get_structure(0, -1) == set()
    assert board._get_structure(5, 0) == set()
    assert board._get_structure(0, 5) == set()

def test_is_strucure_alive(board):
    helper = lambda x, y: board._is_structure_alive(board._get_structure(x, y))

    assert helper(0, 0)
    assert not helper(0, 4)

def test_remove_strucure(board):
    board._remove_structure(board._get_structure(0, 4))
    assert board.board == [
        [ -1, 0, 1,-1,-1],
        [ -1, 1, 1, 1,-1],
        [  2, 2, 2, 1,-1],
        [  0, 0, 1,-1,-1],
        [ -1,-1,-1,-1,-1]]

def test_place_stone():
    board = Board(3, 5)
    # This one is diffrent
    # careful when transitioning to fixtures
    board.board = [
        [ -1, 0, 1, 2, 2],
        [ -1, 1, 1, 1, 2],
        [  2, 2, 2, 1, 2],
        [  0, 0, 1,-1, 2],
        [  2, 2, 2, 2, 2]]

    assert board.place_stone(3, 3, 0) == ([0, 1, 10], \
      { (4, 4), (2, 4), (4, 0), (0, 4), (3, 4), (4, 3), \
        (4, 2), (3, 0), (2, 3), (1, 4), (4, 1) })
    assert board.board == [
        [ -1, 0, 1,-1,-1],
        [ -1, 1, 1, 1,-1],
        [  2, 2, 2, 1,-1],
        [  0, 0,-1, 0,-1],
        [ -1,-1,-1,-1,-1]]

def test_square_occupied(board):
    """Check for all squeres that are occupied and try to put stone in them, expect error"""
    board_raw = board.board
    for row, row_data in enumerate(board_raw):
        for col, squere in enumerate(row_data):
            if squere == -1: continue
            with pytest.raises(SquareOccuptied):
                board.place_stone(col, row, 0)

def test_cant_place_in_eye():
    board = Board(3, 5)
    board.board = [
        [ -1, 1,-1, 0, 0],
        [  0,-1, 0, 0, 0],
        [ -1, 1, 0, 0, 0],
        [  0, 0, 0, 0, 0],
        [  0, 0, 0, 0, 0]]

    with pytest.raises(SelfCapture):
        board.place_stone(0, 0, 2) # corner

    with pytest.raises(SelfCapture):
        board.place_stone(2, 0, 2) # side

    with pytest.raises(SelfCapture):
        board.place_stone(1, 1, 2) # in the middle

    # No changes to the board were made when errors happened
    assert board.board == [
        [ -1, 1,-1, 0, 0],
        [  0,-1, 0, 0, 0],
        [ -1, 1, 0, 0, 0],
        [  0, 0, 0, 0, 0],
        [  0, 0, 0, 0, 0]]
