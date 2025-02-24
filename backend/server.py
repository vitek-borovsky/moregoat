import eventlet
eventlet.monkey_patch()

from flask import Flask, request
from flask_socketio import SocketIO
import random

from game import Game

PORT = 5000

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# TODO add locking to this variable
games = { }

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
def start_game(player_count: int, board_size: int):
    assert player_count in range(2, 6)
    assert board_size in range(5, 21, 2)
    while game_id := random.randint(0, 1_000) in games: pass
    games[game_id] = Game(game_id, player_count, board_size)


if __name__ == '__main__':
    socketio.run(app, port=PORT, debug=True)
