import socket
Sock_Server=socket.socket()
host=socket.gethostname()
port=12121
Sock_Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Sock_Server.bind((host,port))
x = ""
Sock_Server.listen(5)
c,addr = Sock_Server.accept()
print 'Got connection from',addr
while x!="exit":
	x = raw_input('Enter Message:')
	c.send(x)
# c.shutdown(socket.SHUT_RDWR)
Sock_Server.close()