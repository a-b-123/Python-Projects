#beginner implementation of basic socket programming in python following client-server model
#learned how to do this from a great tutorial by Tech With Tim on YouTube. 

##SERVER##

import socket
import threading #allows us to create multiple threads within the program for execution
import time

port = 9432
address = socket.gethostbyname(socket.gethostname())
tup = (address, port) #tuple used to bind the server socket to the address of the machine
header = 64 #dictates the length of the message we want to receive

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = using IPv4, #SOCK_STREAM = using TCP
srvr.bind(tup)

encoding = 'UTF-8'
removeconn = "disconnect"

def client(conn, tup):
    print(f"New Connection from: {tup}")
    while 1:
        rcv = conn.recv(header).decode(encoding) #decoding the message recevied in byte format into a UTF-8 string
        if rcv:
            rcv = int(rcv) #convert the string to an int
            actualmsg = conn.recv(rcv).decode(encoding) #tells us how many bytes we will receive
            if actualmsg == removeconn:
                break
            print(f"{tup} {actualmsg}")
            conn.send("Acknowledged".encode(encoding)) #message from server back to client

    conn.close()

def listen():
    srvr.listen()
    print(f"Server {address} now listening")
    while 1:
        conn, tup = srvr.accept() #server will wait for a new connection to the server. The address and port are saved to send info back
        newthread = threading.Thread(target=client, args=(conn,tup)) #passes new connection to client function to handle it
        newthread.start()
        print(f"[connections] {threading.active_count() - 1}")

print("Server starting..")
listen()        