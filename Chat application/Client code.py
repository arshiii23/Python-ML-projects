import socket

client = socket.socket()

client.connect(("127.0.0.1", 9999))

print("Connected to server")

while True:

    message = input("You: ")

    client.send(message.encode())

    reply = client.recv(1024).decode()

    print("Server:", reply)