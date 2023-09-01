import socket
import threading

srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server socket opened')
threadcount=0
srvsocket.bind(('localhost', 8889))

srvsocket.listen(5)

def NewClientSocketHandler(client, ip):
    print(f'new client connected: {ip}')
    while True:
        recmsg=client.recv(1024).decode('UTF-8')
        print(f"{ip} sent : {recmsg}")
        msg="Confirmed:"+recmsg
        client.send(msg.encode('UTF-8'))
        

while True:
    print('Waiting for the incoming connections')
    client, ip = srvsocket.accept()
    threadcount+=1
    print(f"thread count ={threadcount}")
    threading._start_new_thread( NewClientSocketHandler, (client, ip))
