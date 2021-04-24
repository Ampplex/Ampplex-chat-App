import socket
import threading
import pyttsx3

HEADER = 64
PORT = 8080
BUFFER_SIZE = 2048
SERVER = socket.gethostname()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def speak(audio):
    pyttsx3.speak()


def handleClient(client_socket, addr):
    print(f'[NEW CONNECTION] {addr}')
    speak("New Connection")


def start():
    server.listen()
    print(f'[LISTENING] server is listening on {socket.gethostbyname(SERVER)}')
    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(
            target=handleClient, args=(client_socket, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')


if __name__ == '__main__':
    # Starting the server by calling the start function
    print('[STARTING] server is starting')
    start()
