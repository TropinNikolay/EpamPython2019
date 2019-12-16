import socket
import threading


def accept_incoming_connections():
    while True:
        client_socket, client_address = SERVER.accept()
        print("Received the connection from:", client_address)
        threading.Thread(target=handle_client, args=(client_socket,)).start()


def handle_client(client_socket):
    try:
        name = client_socket.recv(BUFSIZE).decode()
        clients[client_socket] = name
        print("Data received:", name)
        while True:
            data = client_socket.recv(BUFSIZE).decode()
            if data == "q":
                print("Client quits: ")
                client_socket.close()
                del clients[client_socket]
                break
            elif data == '-l':
                users = ''
                for client in clients.values():
                    users += str(client) + '\n'
                client_socket.send(users.encode())
            elif data.find('-u') != -1:
                index = data.find('-u')
                name = data[:index - 1]
                message = data[index + 3:]
                for address, client_name in clients.items():
                    if client_name == name:
                        address.send(message.encode())
            else:
                broadcast(data.encode(), client_socket)

    except OSError:
        client_socket.close()
        try:
            del clients[client_socket]
        except KeyError:
            print("Client quits: ")


def broadcast(data, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(data)
            except OSError:
                pass


clients = {}

HOST = 'localhost'
PORT = 5090
BUFSIZE = 1024

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))

if __name__ == '__main__':
    SERVER.listen(100)
    print("Server is running on port 5090")
    print("Waiting for connection...")
    ACCEPT_THREAD = threading.Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
