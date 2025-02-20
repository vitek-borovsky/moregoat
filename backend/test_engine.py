import pytest
from engine import MoreGoatBoard

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

def full_game():
    # TODO
    # stone not captured when not supposed to
    pass

# these tests should be written on the wrapper
# can pass
# correct player is placing stone
# doing incorrect move doesn't change player on turn

