##Trabalho 2 - INF 452
# Autores: Mariana Rodrigues (Es98875) e Rafael Rocha(Es90668) 

import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 20000

def send_File(fileName):    
    # creating a socket implementing TCP for sending files
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    tcp.connect((socket.gethostname(), PORT))
    f = open(fileName, 'rb')
    read_file = f.read(1024)
    while (read_file):
        tcp.send(read_file)
        read_file = f.read(1024)
    f.close()
    tcp.shutdown(socket.SHUT_WR)
    tcp.close()

def receive_File(fileName):
        try:
            # creating a socket implementing TCP for sending and receiving files
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            tcp.bind((HOST, PORT))  
            f = open("[copy]" + fileName, 'wb')
            tcp.listen(5)  # Now wait for client connection.
            while True:
                #accepting client connection request
                c, address = tcp.accept()  
                cliente_file = c.recv(1024)
                while (cliente_file):
                    f.write(cliente_file)
                    cliente_file = c.recv(1024)
                f.close()
                print("Done Receiving")
                c.close()
        except:
            tcp.close()

#will run as long as the client maintains its connection.
def client_listen():
    while True:
        msgs, serv = c.recvfrom(1024)
        print(msgs.decode('utf8'))

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
            send_file = threading.Thread(target=send_File, args=(msg.replace('/file ', ''), ),)
            send_file.start()
        if '/get' in msg:
            threading.Thread(target=receive_File, args=(msg.replace('/get ', ''), ),).start()
    time.sleep(5)
    c.close()
    return


# creating a socket implementing UDP for sending and receiving normal messages
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to = (HOST, PORT) 

#the client will listen to the server in parallel sending messages, to receive messages from other connected clients
listen = threading.Thread(target=client_listen)
listen.start()
send = threading.Thread(target=client_send)
send.start()
