#########################################################Trabalho 2 - INF 452######################################################################################
## Autores: Mariana Rodrigues de Sant'Ana(Es98875) e Rafael Rocha(Es98875)                                                                                       ##
## Tratar erro: um cliente não consegue pedir lista e logo em seguida sair                                                                                       ##
##                                                                                                                                                               ##
##                                                                                                                                                               ##
##                                                                                                                                                               ##
###################################################################################################################################################################

import socket
import threading

HOST = ''
PORT =  20000
clients = []
usernames = []
users_info = {}


def server_send(msg, sender):
  for info, user in list(users_info.items()):
    if info != sender:                                  #broadcast: send to everyone except the sender
        s.sendto(msg,info)

def list_conected_clients(msg_list, request):                         
  s.sendto(msg_list,request)

def server_listen():
  while True:
    msg, client = s.recvfrom(1024)
    
    #If it's a new client connecting to the server, we add him and his information to the list and send the login notification to the others.
    if client not in clients:                             
      user = msg.decode() + ' entrou'
      print(user)
      server_send(user.encode(),client)
      usernames.append(msg)
      clients.append(client)
      users_info[client] = msg
    #if it was already connected, we just received the message and broadcasted to others on the network, including the information about who sent it.
    else:
      #While the server listens to the client, it sends the broadcast in parallel
      if msg.decode() == '/bye':
        msg_bye = users_info[client].decode()+ ' saiu'
        print(msg_bye)
        server_send(msg_bye.encode(),client)
        usernames.remove(users_info[client])
        clients.remove(client)
        if not clients:
          break
      #If the list of logged in users is requested, we transform the list of users so far and send it in string format only to the one who requested the list
      elif msg.decode() == '/list':
        msg_list = ','.join(str(x) for x in usernames)
        s.sendto(('Clientes conectados: '+msg_list).encode(),client)
      else:
        msg_chat = users_info[client].decode()+ ' disse: '+msg.decode()            #variable to identify sender
        server_send(msg_chat.encode(),client)
  s.close()
  return

print('Aguardando conexão')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
orig = (HOST,PORT)
s.bind(orig) 

listen = threading.Thread(target=server_listen)
listen.start()
  
