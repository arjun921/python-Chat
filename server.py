import socket
s=socket.socket()
host=socket.gethostname()
port=12347
s.bind((host,port))
x = ""
s.listen(5)
y=True
while y:
	c,addr = s.accept()
	print 'Got connection from',addr
	while x!="exit":
		x = raw_input('Enter Message:')
		c.send(x)
	c.close()
	y=False