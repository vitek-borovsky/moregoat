import eventlet

eventlet.monkey_patch()

from .server import Server

PORT = 5000
KEY_LENGTH = 3

if __name__ == '__main__':
    print("[CREATING SERVER]")
    server = Server("MoreGoat")
    print("[STARTING SERVER]")
    server.start_server(PORT)
