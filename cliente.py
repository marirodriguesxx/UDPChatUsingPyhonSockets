import socket

HOST = '127.0.0.1'
PORT =  20000

# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)
PORTA = input("digite a porta: ")
udp.bind(("", int(PORTA)))
# tcp.connect(destino)

msg = input()
while msg != 'bye':
  # msg = input()
  udp.sendto(msg.encode(), destino)
  # tcp.accept()
  data, addr = udp.recvfrom(1024)
  print(data)
  # tcp.send(msg.encode())
  msg = input()

udp.close()
# tcp.close()
