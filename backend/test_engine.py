import pytest
from moreGoatBoard import MoreGoatBoard
import pdb

def test_board_empty():
    mgb = MoreGoatBoard(2, 3)
    for i in range(3):
        for j in range(3):
            assert mgb[i, j] == mgb.CELL_EMPTY

def test_place_stone():
    mgb = MoreGoatBoard(2, 3)
    mgb.put_stone(1, 0, 0)
    assert mgb[0,0] == 1

def test_place_stone_out_of_range():
    mgb = MoreGoatBoard(2, 3)
    with pytest.raises(IndexError):
        mgb.put_stone(1, 3, 0)

    with pytest.raises(IndexError):
        mgb.put_stone(1, -1, 0)

    with pytest.raises(IndexError):
        mgb.put_stone(1, 0, 3)

    with pytest.raises(IndexError):
        mgb.put_stone(1, 0, -1)

def test_placing_stone_over_stone():
    mgb = MoreGoatBoard(2, 3)
    mgb.put_stone(1, 1, 1)

    with pytest.raises(RuntimeError):
        mgb.put_stone(1, 1, 1)

    with pytest.raises(RuntimeError):
        mgb.put_stone(2, 1, 1)


def test_wrong_player_id():
    mgb = MoreGoatBoard(2, 3)

    with pytest.raises(RuntimeError):
        mgb.put_stone(-1, 0, 0)

    with pytest.raises(RuntimeError):
        mgb.put_stone(3, 0, 0)

def test_no_in_eye_without_capture_placement():
    mgb = MoreGoatBoard(2, 3)
    mgb.put_stone(1, 1, 0)
    mgb.put_stone(1, 0, 1)
    mgb.put_stone(1, 1, 2)
    mgb.put_stone(1, 2, 1)

    with pytest.raises(RuntimeError):
        mgb.put_stone(2, 1, 1)

def test_no_capture():
    """
    Few moves where no capture should occur
    """
    mgb = MoreGoatBoard(2, 3)
    assert mgb.put_stone(1, 1, 0) == set()
    assert mgb.put_stone(2, 2, 0) == set()
    assert mgb.put_stone(1, 0, 1) == set()
    assert mgb.put_stone(2, 1, 2) == set()

    assert mgb[1,0] == 1
    assert mgb[2,0] == 2
    assert mgb[0,1] == 1
    assert mgb[1,2] == 2

def test_capture():
    mgb = MoreGoatBoard(2, 3)
    assert mgb.put_stone(1, 1, 1) == set()
    assert mgb.put_stone(2, 0, 1) == set()
    assert mgb.put_stone(2, 2, 1) == set()
    assert mgb.put_stone(2, 1, 0) == set()
    assert mgb.put_stone(2, 1, 2) == { (1,1) }

def test_cant_capture_self():
    """
    1 1 0
    x 1 0
    2 1 0
    """
    mgb = MoreGoatBoard(2, 3)
    assert mgb.put_stone(1, 0, 0) == set()
    assert mgb.put_stone(1, 1, 0) == set()
    assert mgb.put_stone(1, 1, 1) == set()
    assert mgb.put_stone(1, 1, 2) == set()

    assert mgb.put_stone(2, 0, 1) == set()

    with pytest.raises(RuntimeError):
        mgb.put_stone(2, 0, 1)


def test_full_game():
    mgb = MoreGoatBoard(2, 5)
    # TODO

if __name__ == '__main__':
    pdb.set_trace()
    test_capture()

