import eventlet

eventlet.monkey_patch()

# silence linter error import not on top of a file
from src.server import Server  # noqa: E402

PORT = 5000
KEY_LENGTH = 3

if __name__ == '__main__':
    print("[CREATING SERVER]")
    server = Server("MoreGoat")
    print("[STARTING SERVER]")
    server.start_server(PORT)
