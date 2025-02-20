import eventlet
eventlet.monkey_patch()

from flask import Flask, request
from flask_socketio import SocketIO

from game import Game

# Create a Flask application
app = Flask(__name__)

# Set up Flask-SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

game = Game(2,3)

# @app.route('/manual_send')
# def manual_send():
#     # Send a message to all connected clients
#     socketio.send('sending msg with send')
#     return "Message sent!"


@socketio.on("connect")
def handle_connect():
    print("Client connected")
    socketio.emit("Hello from Flask-SocketIO! [connect]")

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

@socketio.on("stone_placed")
def stone_placed(payload):
    print(payload)
    socketio.emit("ACK-testing", "msg recieved")

# @app.before_request
# def log_request():
#     # Log the incoming HTTP request before it reaches any route
#     if request.headers.get("Upgrade") == "websocket":
#         print("WebSocket handshake initiated")
#         print("Request Headers:", dict(request.headers))
#     else:
#         print("HTTP Request:", request)

# Handle a message from the client
# @socketio.on('message')
# def handle_message(msg):
#     print(f"Received message: {msg}")
#     socketio.emit("Hello from Flask-SocketIO!")

# Run the app with SocketIO
if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
