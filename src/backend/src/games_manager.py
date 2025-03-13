from .game import Game
import string
import random


GAME_ID_LENGTH = 3


def get_random_string(length: int) -> str:
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=length))


class GamesManager:
    def __init__(self) -> None:
        self.games: dict[str, Game] = {}

    def __getitem__(self, key) -> Game:
        return self.games[key]

    def __contains__(self, key) -> bool:
        return key in self.games

    def create_game(
            self, player_count: int, board_size: int
            ) -> tuple[str, int]:
        while (game_id := get_random_string(GAME_ID_LENGTH)) in self.games:
            pass
        self.games[game_id] = Game(game_id, player_count, board_size)
        player_id = self.games[game_id].request_player_id()
        print(f"Game created { self.games[game_id].__repr__() }")
        return game_id, player_id
