import socket
import threading
import time
import sys

HOST = '127.0.0.1'
PORT =  20000

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
  orig = c.getsockname()                                           #"returns the current address to which the socket c is bound,"
  while True:
    msg = input()
    c.sendto(msg.encode(),to)
    if msg == '/bye':
      break
  time.sleep(5)
  c.close()
  return
  

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
to = (HOST, PORT)

#the client will listen to the server in parallel sending messages, to receive messages from other connected clients
listen =  threading.Thread(target=client_listen)
listen.start()
send = threading.Thread(target=client_send)
send.start()

