from backend.game import Game

def test_get_structure():
    g = Game("tsarta", 3, 5)
    g.board = [
        [ -1, 0, 1, 2, 2],
        [ -1, 1, 1, 1, 2],
        [  2, 2, 2, 1, 2],
        [  0, 0, 1, 2, 2],
        [  2, 2, 2, 2, 2]]

    assert g._get_structure(0, 0) == { (0, 0), (0, 1) }
    assert g._get_structure(1, 0) == { (1, 0) }
    assert g._get_structure(1, 1) == {(1, 1), (2, 0), (2, 1), (3, 1), (3, 2) }
    assert g._get_structure(0, 2) == { (0, 2), (1, 2), (2, 2) }
    assert g._get_structure(0, 3) == { (0, 3), (1, 3) }
    assert g._get_structure(0, 4) == { (0, 4), (1, 4), (2, 4), (3, 4),
         (4, 4), (4, 0), (4, 3), (4, 2), (3, 0), (4, 1), (3, 3) }

    assert g._get_structure(-1, 0) == set()
    assert g._get_structure(0, -1) == set()
    assert g._get_structure(5, 0) == set()
    assert g._get_structure(0, 5) == set()

def test_is_strucure_alive():
    g = Game("tsarta", 3, 5)
    g.board = [
        [ -1, 0, 1, 2, 2],
        [ -1, 1, 1, 1, 2],
        [  2, 2, 2, 1, 2],
        [  0, 0, 1, 2, 2],
        [  2, 2, 2, 2, 2]]

    helper = lambda x, y: g._is_structure_alive(g._get_structure(x, y))

    assert helper(0, 0)
    assert not helper(0, 4)

def test_remove_strucure():
    g = Game("tsarta", 3, 5)
    g.board = [
        [ -1, 0, 1, 2, 2],
        [ -1, 1, 1, 1, 2],
        [  2, 2, 2, 1, 2],
        [  0, 0, 1, 2, 2],
        [  2, 2, 2, 2, 2]]

    g._remove_structure(g._get_structure(0, 4))
    assert g.board == [
        [ -1, 0, 1,-1,-1],
        [ -1, 1, 1, 1,-1],
        [  2, 2, 2, 1,-1],
        [  0, 0, 1,-1,-1],
        [ -1,-1,-1,-1,-1]]
