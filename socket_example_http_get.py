import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
s.send(b'GET / HTTP/1.0\n\n')
data = s.recv(4096)
print(repr(data))
