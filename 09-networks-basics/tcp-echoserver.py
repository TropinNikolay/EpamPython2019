import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 5090))
s.listen(5)
print("Server is running on port 5090:")
while True:
    clientsocket, clientaddress = s.accept()
    print("Received the connection from:", clientaddress)
    while True:
        data = clientsocket.recv(512).decode()
        if data == "q":
            clientsocket.close()
            print("Client quits: ")
            break
        else:
            print("Data received:", data)
            newdata = "You Send: " + data
            clientsocket.send(newdata.encode())
