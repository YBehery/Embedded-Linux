import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8889))

while True:
    msg = input()
    client.send(msg.encode('UTF-8'))
    print(client.recv(1024).decode('UTF-8'))