import socket
import threading
import time
import sys

HOST = '127.0.0.1'
PORT = 20000


#will run as long as the client maintains its connection.
def client_listen():
    while True:
        msgs, serv = c.recvfrom(1024)
        print(msgs)


#will be executed as long as the client does not close the connection with the command "/bye"
def client_send():
    #The first information to be received by the customer is the username
    print('Nome de usuário: ')
    user = input()
    c.sendto(user.encode(), to)
    while True:
        msg = input()
        c.sendto(msg.encode(), to)
        if msg == '/bye':
            break
        if '/file' in msg:
            threading.Thread(
                target=sendFileTCP,
                args=(msg.replace('/file ', ''), ),
            ).start()
    time.sleep(5)
    c.close()
    return


def sendFileTCP(fileName):
    s = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )  # Create a socket object

    s.connect((socket.gethostname(), PORT))
    # s.send(("Enviando arquivo " + fileName + "...").encode())
    f = open(fileName, 'rb')
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    f.close()
    s.shutdown(socket.SHUT_WR)
    s.close()


c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to = (HOST, PORT)

#the client will listen to the server in parallel sending messages, to receive messages from other connected clients
listen = threading.Thread(target=client_listen)
listen.start()
send = threading.Thread(target=client_send)
send.start()
