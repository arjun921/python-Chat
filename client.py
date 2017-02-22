import socket
s=socket.socket()
host=socket.gethostname()
port=12121
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((host,port))
x=""
while x!="exit":
	x = s.recv(1024)
	print x 
# s.shutdown(socket.SHUT_RDWR)
s.close