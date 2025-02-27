import eventlet

from backend.server import Server

from flask import Flask, request
from flask_socketio import SocketIO, join_room
import random
import string
import json


from game import Game

def get_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class Server:
    """
    Server for Moregoat.app

    methods handle_(event) are triggred on given event

    Attributes:
        socketio:
    """
    def __init__(self, app_name: str) -> None:
        self.games: dict[str, Game ] = { }
        self.app = Flask(app_name)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*", async_mode="eventlet")

        self.socketio.on_event("connect", self.handle_connect)
        self.socketio.on_event("disconnect", self.handle_disconnect)
        self.socketio.on_event("ping", self.handle_ping)
        self.socketio.on_event("create_game", self.handle_create_game)
        self.socketio.on_event("join_game", self.handle_join_game)

    def start_server(self, port: int, debug=False) -> None:
        self.socketio.run(self.app, port=port, debug=debug)

    def handle_connect(self, _):
        print("Client connected")

    def handle_disconnect(self, _):
        print("Client disconnected")

    def handle_ping(self, payload):
        print(f"Recieved test {payload}, retransmitting")
        socketio.emit("PING", payload, room=request.sid)

    def handle_create_game(self, payload):
        data = json.loads(payload)
        player_count, board_size = data["player_count"], data["board_size"]
        assert player_count in range(2, 6)
        assert board_size in range(5, 21, 2)
        while (game_id := get_random_string(3)) in self.games: pass
        self.games[game_id] = Game(game_id, player_count, board_size)
        player_id = self.games[game_id].request_player_id()
        print(f"Game created { self.games[game_id].__repr__() }")
        socketio.emit("JOIN_GAME", "{" + f"game_id : { game_id }, player_id : { player_id }" + "}", room=request.sid)

    def handle_join_game(self, game_id: str):
        join_room(game_id)
        player_id = self.games[game_id].request_player_id()
        socketio.emit("JOIN_GAME", "{" + f"game_id : { game_id }, player_id : { player_id }" + "}", room=request.sid)

