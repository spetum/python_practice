import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.connect(("www.nate.com", 80))
s.connect(("google.com", 80))


#s.send(b'HEAD / HTTP/1.0\n\n')
#s.send(b'GET / HTTP/1.0\n\n')
#s.send(b'HEAD / HTTP/1.0\n\n')
s.send(b'GET / HTTP/1.1')
data = s.recv(1024) # 1024로 GET하니깐 반응이 없음.
print(repr(data))
