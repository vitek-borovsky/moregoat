import eventlet

eventlet.monkey_patch()

from .server import Server

PORT = 5000
KEY_LENGTH = 3

print("[CREATING SERVER]")
server = Server("MoreGoat")
# server.start_server(PORT, True)
print("[STARTING SERVER]")
server.start_server(PORT)
