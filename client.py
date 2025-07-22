import socket

port = 8851

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", port))