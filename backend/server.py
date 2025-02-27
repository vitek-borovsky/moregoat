import eventlet
eventlet.monkey_patch()

from flask import Flask, request
from flask_socketio import SocketIO, join_room
import random
import string
import json

from game import Game

PORT = 5000
KEY_LENGTH = 3

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# TODO add locking to this variable
games: dict[str, Game ] = { }

def get_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@socketio.on("connect")
def handle_connect():
    print("Client connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

@socketio.on("ping")
def handle_test(payload):
    print(f"Recieved test {payload}, retransmitting")
    socketio.emit("PING", payload, room=request.sid)

@socketio.on("create_game")
def create_game(payload):
    data = json.loads(payload)
    player_count, board_size = data["player_count"], data["board_size"]
    assert player_count in range(2, 6)
    assert board_size in range(5, 21, 2)
    while (game_id := get_random_string(3)) in games: pass
    games[game_id] = Game(game_id, player_count, board_size)
    print(f"Game created { games[game_id].__repr__() }")

@socketio.on("join_game")
def join_game(game_id: str):
    join_room(game_id)
    player_id = games[join_room].request_player_id()
    socketio.emit("JOIN_GAME", "{" + f"game_id = { game_id }, player_id = { player_id }" + "}", room=request.sid)


if __name__ == '__main__':
    socketio.run(app, port=PORT, debug=True)
