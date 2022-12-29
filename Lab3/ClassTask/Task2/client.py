import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #ip dey nam dey
ADDRS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'End'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRS)

def send(msg):
    message = msg.encode(FORMAT) # sending byte
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length = send_length + b' '*(HEADER - len(send_length)) #byte format (converting 16 byte)
    client.send(send_length) #server ke 2 ta jinish pathay, 16 byte header and
    client.send(message) #actual message send
    print(client.recv(2048).decode(FORMAT))

connected = True

while connected:
    input_message = input("Enter your message: ")
    if input_message != "I'm done":
        send(input_message)
    else:
        connected = False
        send(DISCONNECT_MESSAGE)