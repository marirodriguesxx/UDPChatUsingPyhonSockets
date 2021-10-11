import socket
import threading

HOST = '127.0.0.1'
PORT = 20000

# tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (HOST, PORT)
# tcp.connect(destino)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def listenCliente():
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg, addr = s.recvfrom(1024)
        print("recebido: " + msg.decode())


def sendMessage():
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        text = input()
        s.sendto(text.encode(), destino)


t = threading.Thread(target=listenCliente)
w = threading.Thread(target=sendMessage)
t.start()
w.start()
print(threading.active_count())

# udp.close()
# tcp.close()