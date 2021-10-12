##Trabalho 2 - INF 452
# Autores: Mariana Rodrigues de Sant'Ana(Es98875) e Rafael Rocha(Es90668)                                                                                       ##

import socket
import threading

HOST = ''
PORT = 20000
clients = []
usernames = []
users_info = {}


def list_conected_clients(msg_list, request):
    s.sendto(msg_list, request)

def send_File(fileName):    
    # creating a socket implementing TCP for sending files
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    tcp.connect(('', PORT))
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
                print("Done Receiving File")
                c.close()
        except:
            tcp.close()
        

def server_send(msg, sender):
    for info, user in list(users_info.items()):
        if info != sender:  #broadcast: send to everyone except the sender
            s.sendto(msg, info)

def server_listen():
    while True:
        msg, client = s.recvfrom(1024)

        #If it's a new client connecting to the server, we add him and his information to the list and send the login notification to the others.
        if client not in clients:
            user = msg.decode() + ' entrou'
            server_send(user.encode(),client)
            usernames.append(msg)
            clients.append(client)
            users_info[client] = msg
        #if it was already connected, we just received the message and broadcasted to others on the network, including the information about who sent it.
        else:
            #While the server listens to the client, it sends the broadcast in parallel
            if msg.decode() == '/bye':
                msg_bye = users_info[client].decode() + ' saiu'
                server_send(msg_bye.encode(),client)
                usernames.remove(users_info[client])
                clients.remove(client)
                if not clients: #if there are no more "online" clients, the server is closed
                    break
            #If the list of logged in users is requested, we transform the list of users so far and send it in string format only to the one who requested the list
            elif msg.decode() == '/list':
                msg_list = ','.join(str(x) for x in usernames)
                s.sendto(('Clientes conectados: ' + msg_list).encode(), client)
            elif '/file' in msg.decode():
                #notifying other customers a notice that a file has been sent
                msg_file = users_info[client].decode() + ' enviou um arquivo: ' + msg.decode().replace('/file ', '')  #variable to identify who sent the file
                send_file_notification = threading.Thread(target=server_send, args= (msg_file.encode(),client))
                send_file_notification.start()
                #starting to receive files
                file = threading.Thread(target=receive_File, args=(msg.decode().replace('/file ', ''), ),)
                file.start()
            elif '/get' in msg.decode():
                print('Pegando arquivo')
                #starting to send the files
                # file = threading.Thread(target=send_File, args=(msg.decode().replace('/file ', ''), ),)
                # file.start()
            else:
                msg_chat = users_info[client].decode() + ' disse: ' + msg.decode()  #variable to identify who sent the message
                server_send(msg_chat.encode(),client)
    s.close()
    return


print('Aguardando conexão')
# creating a socket implementing UDP for receiving normal messages and broadcast
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
s.bind(orig)
 

listen = threading.Thread(target=server_listen)
listen.start()
