import socket
import threading

HOST = ''
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

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (HOST, PORT)

tcp.bind(origem)
tcp.listen(1)

while True:
  conexao, cliente = tcp.accept()
  t = threading.Thread(target=conectado, args=(conexao, cliente))
  t.start()

tcp.close()
