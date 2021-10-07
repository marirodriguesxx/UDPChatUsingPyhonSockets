import socket
import threading

HOST = ''
PORT =  20000

# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

origem = (HOST, PORT)

# udp.bind(origem)


# def receiveAndBroadcast(msg, cliente):
#   if cliente not in clientes:
#     clientes.append(cliente)
#   for cli in clientes:
#     # if cli[1] != cliente[1]:
#     udp.sendto(msg.encode(), cli)

clientes = []

def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(origem) #binding the IP address and port number
    while True:
        msg, cliente = s.recvfrom(1024)
        if cliente not in clientes:
          clientes.append(cliente)
        print(msg.decode())
        for cli in clientes:
          s.sendto(msg, cli)

#Function for sending
# def sender():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     text = "servidor msg:"
#     while True:
#         if "bye" in text or "exit" in text or "finish" in text:
#             exit()
#         else:
#             # text = input()
#             text = text
#             print(clientes)


# send = threading.Thread(target=sender)
receive = threading.Thread(target=receiver)
# send.start()
receive.start()

# while True:
#   msg, cliente = udp.recvfrom(1024)
#   print(cliente, msg.decode())
#   t = threading.Thread(target=receiveAndBroadcast, args=(msg, cliente))
#   t.start()
#   print(threading.active_count())
