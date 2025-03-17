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
        self._game_started = False

    def __repr__(self) -> str:
        return f"""Game(
            game_id={ self._game_id },
            started={self._game_started },
            player_count={ self._player_count },
            board_size={ self._board_size })"""

    def _increase_player_on_turn(self) -> None:
        self._player_on_turn = (self._player_on_turn + 1) % self._player_count

    def get_board_size(self) -> int:
        return self._board_size

    def get_player_count(self) -> int:
        return self._player_count

    def get_game_started(self) -> bool:
        return self._game_started

    def try_start_game(self) -> bool:
        if self._next_player_id == self._player_count:
            self._game_started = True
            self._start_game()
        return self._game_started

    def _start_game(self):
        self._points = [0 for _ in range(self._player_count)]
        self._board = Board(self._player_count, self._board_size)
        self._player_on_turn = 0

    def request_player_id(self) -> int:
        id = self._next_player_id
        self._next_player_id += 1
        return id

    def place_stone(
            self, col: int, row: int, player_id: int
            ) -> set[tuple[int, int]]:
        if player_id != self._player_on_turn:
            raise PlayerOutOfTurn(
                f"""Player plays but not on turn.
                Player who played={player_id}
                Player on turn={self._player_on_turn}""")

        points_changes, captured_stones = \
            self._board.place_stone(col, row, player_id)

        for i, points in enumerate(points_changes):
            # Add points to the player that played a move
            # for each captured stone
            self._points[player_id] += points
            # Remove point from each player if his stone was captured
            self._points[i] -= points

        self._increase_player_on_turn()
        return captured_stones

    def get_points(self) -> list[int]:
        """
        returns COPY of points, can be modified

        Returns:
          rv[i] <-> points of player with i id

        """
        return self._points[:]

    def player_pass(self, player_id: int) -> None:
        """
        Throws PlayerOutOfTurn exception if wrong player passed
        """
        if player_id != self._player_on_turn:
            raise PlayerOutOfTurn(
                f"""Player {player_id} passed, but not on turn
                Player on turn {self._player_on_turn}""")

        self._increase_player_on_turn()
