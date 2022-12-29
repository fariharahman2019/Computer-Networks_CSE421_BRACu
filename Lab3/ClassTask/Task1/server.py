import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRS= (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'End'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRS)

server.listen()
print("[LISTENING] Server is listening")

while True:
    conn, adrs = server.accept()
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected - False
                conn.send('Goodbye'.encode(FORMAT))
            else:
                print(msg)
                conn.send('Message received'.encode(FORMAT))
    conn.close()