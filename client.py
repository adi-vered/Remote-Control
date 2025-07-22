import socket

port = 8851

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", port))
print("connected")

while True:
    data_to_send = input("send:")
    my_socket.send(data_to_send.encode())

    if data_to_send == "EXIT":
        break
    
    reply = (my_socket.recv(1024)).decode()
    print(reply)

my_socket.close()