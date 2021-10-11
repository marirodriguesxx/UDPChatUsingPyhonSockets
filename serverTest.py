import socket
import threading

HOST = ""
PORT = 20000

origem = (HOST, PORT)
clientes = []


def receiver():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(origem)  # binding the IP address and port number
    while True:
        msg, cliente = s.recvfrom(1024)
        if cliente not in clientes:
            clientes.append(cliente)
        for cli in clientes:
            if cli != cliente:
                print(cli, ": " + msg.decode())
                s.sendto(msg, cli)
        print("\n")


receive = threading.Thread(target=receiver)
receive.start()

# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# udp.bind(origem)

# def receiveAndBroadcast(msg, cliente):
#   if cliente not in clientes:
#     clientes.append(cliente)
#   for cli in clientes:
#     # if cli[1] != cliente[1]:
#     udp.sendto(msg.encode(), cli)

# Function for sending
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

# send.start()

# while True:
#   msg, cliente = udp.recvfrom(1024)
#   print(cliente, msg.decode())
#   t = threading.Thread(target=receiveAndBroadcast, args=(msg, cliente))
#   t.start()
#   print(threading.active_count())
