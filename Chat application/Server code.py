import socket

server = socket.socket()

server.bind(("127.0.0.1", 9999))

server.listen(1)

print("Waiting for connection...")

client, address = server.accept()

print("Connected to", address)

while True:

    message = client.recv(1024).decode()

    print("Client:", message)

    reply = input("You: ")

    client.send(reply.encode())