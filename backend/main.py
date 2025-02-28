import eventlet

eventlet.monkey_patch()

from server import Server
from flask import Flask

PORT = 5000
KEY_LENGTH = 3

server = Server("MoreGoat")
server.start_server(PORT, True)
