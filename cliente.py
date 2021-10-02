import socket

HOST = '127.0.0.1'
PORT =  20000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)

while True:
  msg = input()
  tcp.send(msg.encode())
  if msg == 'bye':
    break

tcp.close()
