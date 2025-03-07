from board import Board

class Game:
    def __init__(self, game_id: str, player_count: int, board_size: int) -> None:
        self.game_id = game_id
        self.player_count = player_count
        self.board_size = board_size
        self.next_player_id = 0

        # TODO remove this it's for testing only
        self._start_game()

    def __repr__(self) -> str:
        return f"Game({ self.game_id }, { self.player_count }, board_size={ self.board_size })"

    def _increase_player_on_turn(self) -> None:
        self.player_on_turn = (self.player_on_turn + 1) % self.player_count

    def _start_game(self):
        self.points = [ 0 for _ in range(self.player_count) ]
        self.board = Board(self.player_count, self.board_size)
        self.player_on_turn = 0

    def request_player_id(self) -> int:
        id = self.next_player_id
        self.next_player_id += 1
        return id

    def place_stone(self, col: int, row: int, player_id):
        if player_id == self.player_on_turn:
            raise RuntimeError("Not your turn") #TODO
        points_changes = self.board.place_stone(col, row, player_id)
        for i, points in enumerate(points_changes):
            # Add points to the player that played a move
            # for each captured stone
            self.points[player_id] += points
            # Remove point from each player if his stone was captured
            self.points[i] -= points

        self._increase_player_on_turn()

