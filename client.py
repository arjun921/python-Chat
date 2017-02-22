import socket
s=socket.socket()
host=socket.gethostname()
port=12347
s.connect((host,port))
x=""
while x!="exit":
	x = s.recv(1024)
	print x 
s.close