#########################################################Trabalho 2 - INF 452######################################################################################
## Autores: Mariana Rodrigues de Sant'Ana(Es98875) e Rafael Rocha(Es90668)                                                                                       ##
##                                                                                                                                                               ##
##                                                                                                                                                               ##
##                                                                                                                                                               ##
##                                                                                                                                                               ##
###################################################################################################################################################################

import socket
import threading

HOST = ''
PORT = 20000
clients = []
usernames = []
users_info = {}


def server_send(msg, sender):
    for info, user in list(users_info.items()):
        if info != sender:  #broadcast: send to everyone except the sender
            s.sendto(msg, info)


def list_conected_clients(msg_list, request):
    s.sendto(msg_list, request)


def receiveFileTCP(fileName):
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)  # Create a socket object
    s.bind((HOST, PORT))  # Bind to the port
    f = open("[copy]" + fileName, 'wb')
    s.listen(5)  # Now wait for client connection.
    while True:
        c, addr = s.accept()  # Establish connection with client.
        print('Got connection from', addr)
        print("Receiving...")
        l = c.recv(1024)
        while (l):
            print("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print("Done Receiving")
        c.send(('Thank you for connecting').encode())
        c.close()


def server_listen():
    while True:
        msg, client = s.recvfrom(1024)

        #If it's a new client connecting to the server, we add him and his information to the list and send the login notification to the others.
        if client not in clients:
            user = msg.decode() + ' entrou'
            print(user)
            server_send(user.encode(), client)
            usernames.append(msg)
            clients.append(client)
            users_info[client] = msg
        #if it was already connected, we just received the message and broadcasted to others on the network, including the information about who sent it.
        else:
            #While the server listens to the client, it sends the broadcast in parallel
            if msg.decode() == '/bye':
                msg_bye = users_info[client].decode() + ' saiu'
                print(msg_bye)
                server_send(msg_bye.encode(), client)
                usernames.remove(users_info[client])
                clients.remove(client)
                if not clients:
                    break
            #If the list of logged in users is requested, we transform the list of users so far and send it in string format only to the one who requested the list
            elif msg.decode() == '/list':
                msg_list = ','.join(str(x) for x in usernames)
                s.sendto(('Clientes conectados: ' + msg_list).encode(), client)
            elif '/file' in msg.decode():
                print(msg.decode())
                threading.Thread(
                    target=receiveFileTCP,
                    args=(msg.decode().replace('/file ', ''), ),
                ).start()

                msg_chat = users_info[client].decode(
                ) + ' enviou um arquivo: ' + msg.decode().replace(
                    '/file ', '')  #variable to identify sender
                server_send(msg_chat.encode(), client)
            else:
                msg_chat = users_info[client].decode(
                ) + ' disse: ' + msg.decode()  #variable to identify sender
                server_send(msg_chat.encode(), client)
    s.close()
    return


print('Aguardando conexão')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
s.bind(orig)

listen = threading.Thread(target=server_listen)
listen.start()
