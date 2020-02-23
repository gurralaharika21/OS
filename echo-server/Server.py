import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 3016))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print("Connection by" ,address)
    msg = clientsocket.recv(1024)
    print(msg)
    print(msg.decode("utf-8") , "received from client")
    clientsocket.send(bytes(msg))

clientsocket.close()










