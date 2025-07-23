import socket
import keyboard

def start_server(addr):
    sock = socket.socket()
    sock.bind(addr)
    sock.listen()
    print("server is up and running")
    return sock

def get_client(sock):
    print("waiting for client")
    sock_client, sock_address = sock.accept()
    print(f'Client connected: {sock_address} : {sock_client}')
    return sock_client

def main(addr):
    server_socket = start_server(addr)
    client_socket = get_client(server_socket)
    with open("C://Users//User//Documents//vs code python//Remote Control//check.txt" , "w") as my_file:
        while True:
            request = (client_socket.recv(256)).decode()
            print(request)
            if request:
                print(request)
                my_file.write(request)
                my_file.flush()
    
    server_socket.close()
    client_socket.close()

if __name__ == '__main__':
    port = 8851
    address = ('0.0.0.0', port)
    main(address)
