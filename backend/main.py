from flask import Flask
from flask_socketio import SocketIO, send

# Create a Flask application
app = Flask(__name__)

# Set up Flask-SocketIO
socketio = SocketIO(app)

# Handle a message from the client
@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")
    send("Hello from Flask-SocketIO!")

# Run the app with SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True)
