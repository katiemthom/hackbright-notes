import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# class socket, method socket
# now a socket class is created 
# with a specific type of socket
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,)
# next let's tell the socket what 
# to interface with
server_socket.bind(('localhost', 1200)) 
# any port number less than 1024 is reserved
# this creates a socket listening on port 1200
# on the localhost interface
server_socket.listen(5)
# listen takes an arg:
# the number of connections it can buffer 


running = True
while running: 
	# when a connection comes in we want to accept it 
	connection, address = server_socket.accept()
	# accept returns a list 
	# connection is a connection object 
	data = connection.recv(1024)
	# specify the number of bytes you want 
	# to receive at a time 
	# you can read the data in, break apart the headers, 
	# figure out what the browser is asking for, 
	# and reply to it
	# now we have data
	# and we need to send a response back to the browser
	# using http so the browser can understand 
	resp = "HTTP/1.0 200 OK\n" # response code 200 = OK, 302 = redirect
	resp += "Content-type: text/html\n"
	resp += "\n"
	resp += "Hello fish.\nYou are <b>slimy</b>."
	connection.sendall(resp)
	# connection is a handle, like file
	# you can send or sendall
	# you can also open a file and add the contents to the resp
	connection.close()
	running = False 
