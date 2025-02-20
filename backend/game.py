from moreGoatBoard import MoreGoatBoard

class Game:
    """
    Wrapper for `MoreGoatBoard` class
    to simplify player on turn and handing IDs
    to users
    """

    def __init__(self, player_count: int, board_size: int) -> None:
        self.player_count = player_count
        self.board = MoreGoatBoard(player_count, board_size)
        self._player_on_turn = 1

        self.scores = { id : 0 for id in range(1, self.player_count + 1) }

    def get_player_ids(self):
        """
        Getting player ids players are numbred 1 to player_count inc
        This is helper method to avoid confusion
        """
        return list(range(1, self.player_count + 1))

    def __get_next_player(self) -> int:
        self._player_on_turn += 1
        if self._player_on_turn == self.player_count:
            self._player_on_turn = 1

        return self.get_player_on_turn()

    def get_player_on_turn(self):
        return self._player_on_turn

    def put_stone(self, player_id: int, x, y):
        if player_id != self.get_player_on_turn():
            raise RuntimeError()

        self.board.put_stone(player_id, x, y)
