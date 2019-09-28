import socket

server = socket.socket()
server.bind(('', 65431))
server.listen(1)

while True:
    connection, address = server.accept()
    connection.send('Message from server')
    connection.close()
