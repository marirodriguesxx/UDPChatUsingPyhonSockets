import socket
import threading

HOST = '127.0.0.1'
PORT =  20000

def conectado(con, cliente):
  print('Conectado por', cliente)

  while True:
    msg = con.recv(1024).decode()
    if msg == 'bye':
      break
    print(cliente, msg)
  print('Finalizando conexao do cliente', cliente)
  con.close()
  return

# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# print(socket.gethostbyname(socket.gethostname()))

origem = (HOST, PORT)

# tcp.bind(origem)
udp.bind(origem)
# tcp.listen(1)

clientes = []

while True:
  print('esperando ...')
  msg, cliente = udp.recvfrom(1024)
  if cliente not in clientes:
    clientes.append(cliente)
  # print(cliente, msg.decode())
  # udp.sendto(msg, ('255.255.255.255', 9999))
  for cli in clientes:
    print(cli[1])
    udp.sendto("alou", ('<broadcast>', cli[1]))
  # udp.sendto('ack'.encode(), cliente)

udp.close()
# tcp.close()
