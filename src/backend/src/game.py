from .board import Board
from .error import PlayerOutOfTurn


class Game:
    def __init__(
            self, game_id: str, player_count: int, board_size: int
            ) -> None:
        self._game_id = game_id
        self._player_count = player_count
        self._board_size = board_size
        self._next_player_id = 0

    def __repr__(self) -> str:
        return f"""Game(
            { self._game_id },
            { self._player_count },
            board_size={ self._board_size })"""

    def _increase_player_on_turn(self) -> None:
        self.player_on_turn = (self.player_on_turn + 1) % self._player_count

    def try_start_game(self) -> bool:
        return self._next_player_id == self._player_count

    def _start_game(self):
        self.points = [0 for _ in range(self._player_count)]
        self.board = Board(self._player_count, self._board_size)
        self.player_on_turn = 0

    def request_player_id(self) -> int:
        id = self._next_player_id
        self._next_player_id += 1
        return id

    def place_stone(
            self, col: int, row: int, player_id: int
            ) -> set[tuple[int, int]]:
        if player_id != self.player_on_turn:
            raise PlayerOutOfTurn(
                f"""Player plays but not on turn.
                Player who played={player_id}
                Player on turn={self.player_on_turn}""")

        points_changes, captured_stones = \
            self.board.place_stone(col, row, player_id)

        for i, points in enumerate(points_changes):
            # Add points to the player that played a move
            # for each captured stone
            self.points[player_id] += points
            # Remove point from each player if his stone was captured
            self.points[i] -= points

        self._increase_player_on_turn()
        return captured_stones

    def get_points(self) -> list[int]:
        """
        returns COPY of points, can be modified

        Returns:
          rv[i] <-> points of player with i id

        """
        return self.points[:]

    def player_pass(self, player_id: int) -> None:
        """
        Throws PlayerOutOfTurn exception if wrong player passed
        """
        if player_id != self.player_on_turn:
            raise PlayerOutOfTurn(
                f"""Player {player_id} passed, but not on turn
                Player on turn {self.player_on_turn}""")

        self._increase_player_on_turn()
