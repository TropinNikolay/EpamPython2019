import socket
import threading


def receive(client):
    while True:
        try:
            message = client.recv(BUFSIZE).decode("utf8")
            print(message)
        except OSError:
            break


NEW = True
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect(('localhost', 5090))
BUFSIZE = 1024
threading.Thread(target=receive, args=(CLIENT,)).start()
print('Welcome to TCP chat!',
      'If you want to get full member list use -l',
      'If you want to send a message to a specific user, type his name, then -u, then your message',
      'If you want to quit type q', sep='\n')

while True:
    try:
        if NEW:
            DATA = input("Enter your name: ")
            NEW = False
            CLIENT.send(DATA.encode("utf-8"))
        else:
            DATA = input()
            CLIENT.send(DATA.encode("utf-8"))
            if DATA == 'q':
                CLIENT.close()
                break
    except KeyboardInterrupt:
        CLIENT.send(b'q')
        CLIENT.close()
        break
