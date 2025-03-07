class SquareOccuptied(Exception):
    """
    We are placing a stone on a squere that is not empty
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)

class PlayerOutOfTurn(Exception):
    """
    Player tries to place a stone, but it's not his turn
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NotOnBoard(Exception):
    """
    Player places stone on possition that is not on board (col, row) indexes out of range
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
