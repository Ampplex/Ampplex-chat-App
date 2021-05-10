import socket
import threading
import pyttsx3
from plyer import notification

HEADER = 64
PORT = 5050

# gethostbyname() converts computer name/host name to ip address
# gethostname() returns the computer name/host name
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = socket.gethostname()
# DESKTOP-C0IK9J8
# print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def speak(audio):
    pyttsx3.init()
    pyttsx3.speak(audio)


def notify_user(addr):
    notification.notify(
        title="New Connection",
        message=f"{addr}",
        app_icon=None,
        timeout=7
    )


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    speak("New Connection")
    notify_user(addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            Message = msg.split()
            if '@' not in Message:
                with open("user_names.txt", "a") as user_name:
                    user_name.write(msg)
                    print(msg)
                    speak(msg)
            conn.send(input("Enter message: ").encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


if __name__ == '__main__':
    print("[STARTING] server is starting...")
    start()
