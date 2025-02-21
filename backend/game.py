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

        # self.scores = { id : 0 for id in range(1, self.player_count + 1) }

        self.last_used_id = 0
        self.game_ready_to_start = False

    def get_player_id(self) -> int:
        # All players already joined
        if self.game_ready_to_start: return -1

        self.last_used_id += 1
        if self.last_used_id == self.player_count:
            self.game_ready_to_start = True

        return self.last_used_id

    def __get_next_player(self) -> int:
        self._player_on_turn += 1
        if self._player_on_turn > self.player_count:
            self._player_on_turn = 1

        return self.get_player_on_turn()

    def get_player_on_turn(self):
        return self._player_on_turn

    def put_stone(self, player_id: int, x, y)-> set[tuple[int,int]]:
        if player_id != self.get_player_on_turn():
            raise RuntimeError(f"Player plays out of turn; player on turn `{self.get_player_on_turn()}`, player `{player_id}` played\n{self.board}")

        res = self.board.put_stone(player_id, x, y)
        self.__get_next_player()
        return res
