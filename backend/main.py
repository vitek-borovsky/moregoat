import eventlet

eventlet.monkey_patch()

from server import Server

PORT = 5000
KEY_LENGTH = 3

server = Server("MoreGoat")
# server.start_server(PORT, True)
server.start_server(PORT)
