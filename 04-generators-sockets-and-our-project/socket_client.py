import socket

try:
    sock = socket.socket()
    sock.connect(('', 65431))
    print(sock.recv(1024))
except socket.error as err:
    print(str(err))
finally:
    sock.close()
