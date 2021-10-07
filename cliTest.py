import socket
import threading

HOST = '127.0.0.1'
PORT =  20000

# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)
# tcp.connect(destino)

def listenCliente():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
      msg = s.recvfrom(1024)
      print("\n"+msg[0].decode())
      if "exit" in msg[0].decode() or "bye" in msg[0].decode():
          print('tentou sair')


def sendMessage():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  text = "cliente:"
  while True:
    if "bye" in text or "exit" in text or "finish" in text:
        exit()
    else:
        text = input()
        text = text
        s.sendto(text.encode(), destino)


t = threading.Thread(target=listenCliente)
w = threading.Thread(target=sendMessage)
t.start()
w.start()
print(threading.active_count())


# udp.close()
# tcp.close()