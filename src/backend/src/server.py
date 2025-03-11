from flask import Flask, request
from flask_socketio import SocketIO, join_room
from games_manager import GamesManager
import json


class Server:
    """
    Server for Moregoat.app

    methods handle_(event) are triggred on given event

    Attributes:
        socketio:
    """
    def __init__(self, app_name: str) -> None:
        self.app = Flask(app_name)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*", async_mode="eventlet")
        self.games_manager = GamesManager()

        self.app.add_url_rule("/hello", "hello", lambda : "hello")

        self.socketio.on_event("connect", self.handle_connect)
        self.socketio.on_event("disconnect", self.handle_disconnect)
        self.socketio.on_event("ping", self.handle_ping)
        self.socketio.on_event("create_game", self.handle_create_game)
        self.socketio.on_event("join_game", self.handle_join_game)
        self.socketio.on_event("stone_placed", self.handle_stone_placed)

    def start_server(self, port: int, debug=False) -> None:
        self.socketio.run(self.app, port=port, debug=debug)

    def handle_connect(self, _):
        print("Client connected")

    def handle_disconnect(self):
        print("Client disconnected")

    def handle_ping(self, payload):
        print(f"Recieved test {payload}, retransmitting")
        self.send_PING(payload, request)

    def handle_create_game(self, payload):
        data = json.loads(payload)
        player_count, board_size = data["player_count"], data["board_size"]
        assert player_count in range(2, 6)
        assert board_size in range(5, 21, 2)

        game_id, player_id = self.games_manager.create_game(player_count, board_size)
        self.send_JOIN_GAME(game_id, player_id, request)
        join_room(game_id)

    def handle_join_game(self, game_id: str):
        if game_id not in self.games_manager:
            raise NotImplemented

        join_room(game_id)
        player_id = self.games_manager[game_id].request_player_id()
        self.send_JOIN_GAME(game_id, player_id, request)

    def handle_stone_placed(self, payload: str):
        print("recieved stone_placed", payload)
        data = json.loads(payload)
        game_id, col, row, player_id = data["game_id"], data["col"], data["row"], data["player_id"]
        captured_stones = self.games_manager[game_id].place_stone(col, row, player_id)
        points = self.games_manager[game_id].get_points()
        self.send_STONE_PLACED(game_id, col, row, player_id)
        self.send_STONE_CAPTURED(game_id, captured_stones)
        self.send_POINTS(game_id, points)


    ##############################
    ##############################

    def send_PING(self, payload, request) -> None:
        self.socketio.emit("PING", payload, room=request.sid)

    def send_JOIN_GAME(self, game_id: str, player_id: int, request) -> None:
        data = {
            "game_id": game_id,
            "player_id": player_id,
            "board_size": self.games_manager[game_id].board_size,
            "player_count": self.games_manager[game_id].player_count,
        }
        self.socketio.emit("JOIN_GAME", json.dumps(data), room=request.sid)

    def send_STONE_PLACED(self, game_id: str, col: int, row: int, player_id: int) -> None:
        data = {
            "game_id": game_id,
            "player_id": player_id,
            "col": col,
            "row": row,
        }
        self.socketio.emit("STONE_PLACED", json.dumps(data), room=game_id)

    def send_STONE_CAPTURED(self, game_id: str, captured_stones: set[tuple[int, int]]) -> None:
        if len(captured_stones) == 0: return
        data = {
            "game_id": game_id,
            "captured_stones": list(captured_stones)
        }
        self.socketio.emit("STONE_CAPTURED", json.dumps(data), room=game_id)

    def send_POINTS(self, game_id: str, points: list[int]) -> None:
        data = {
            "game_id": game_id,
            "points": points,
        }
        self.socketio.emit("POINTS", json.dumps(data), room=game_id)

