import eventlet
eventlet.monkey_patch()

from flask import Flask, request
from flask_socketio import SocketIO

PORT = 5000

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

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


if __name__ == '__main__':
    socketio.run(app, port=PORT, debug=True)
