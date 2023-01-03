##CLIENT##

import socket

header = 64
port = 9432
encoding = "utf-8"
removeconn = "disconnect"
address = socket.gethostbyname(socket.gethostname())
bind = (address, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(bind)

def sendmsg(actualmsg):
    message = actualmsg.encode(encoding)
    actualmsg_len = len(message)
    lengthsent = str(actualmsg_len).encode(encoding)
    lengthsent += b' ' * (header - len(lengthsent)) #making sure the message length is 64
    client.send(lengthsent)
    client.send(message)
    print(client.rcv(3000).decode(encoding))

sendmsg("Hello")
sendmsg("Hello World!")
sendmsg(removeconn)

