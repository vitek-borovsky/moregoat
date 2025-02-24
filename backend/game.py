class Game:
    def __init__(self, game_id, player_count: int, board_size: int) -> None:
        self.game_id = game_id
        self.player_count = player_count
        self.board_size = board_size

    def __repr__(self) -> str:
        return f"Game(game_id={ self.game_id }, player_count={ self.player_count }, board_size={ self.board_size }"
