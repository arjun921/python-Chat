import socket,sys
i = 0
x = ""

while True:
	if i%2==0:
		# print "Client Mode Started"
		#Reciever Code goes here
		Sock_Client=socket.socket()
		x=""
		port=int(sys.argv[2])
		if sys.argv[1]=="localhost":
			host=socket.gethostname()
		else:
			host=sys.argv[1]
		Sock_Client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		Sock_Client.connect((host,port))
		print "Typing..."
		while x!="over":
			x = Sock_Client.recv(1024)
			if x=="exit":
				break
			elif x!="over":
				print "Message Received:"+x 
		Sock_Client.close()
		#Reciever code ends here

		i=1
		if x=="exit":
			break
		else:
			x=""
	elif i%2!=0:
		# print "Server Started"
		#Sender Code goes here
		Sock_Server=socket.socket()
		Sock_Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		host=socket.gethostname()
		port=int(sys.argv[2])
		Sock_Server.bind((host,port))
		x = ""
		Sock_Server.listen(5)
		c,addr = Sock_Server.accept()
		print 'Got connection from',addr
		while x!="over":
			x = raw_input('Enter Message:')
			c.send(x)
			if x=="exit":
				break
		# c.shutdown(socket.SHUT_RDWR)
		Sock_Server.close()
		#Sender code ends here
		i=0
		if x=="exit":
			break
		else:
			x=""
