import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 5090))
while True:
    data = input("Enter data to send to server: press q to quit:\n")
    c.send(data.encode("utf-8"))
    if data == 'q' or data == 'Q':
        c.close()
        break
    print(c.recv(512).decode())
