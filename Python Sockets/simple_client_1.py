import socket

#initializing socket
my_socket = socket.socket()

#connecting to remote server
my_socket.connect(('54.213.229.251', 8820))

#sending name to server
my_socket.send('Andy')

#receiving data from server
data = my_socket.recv(1024)

#printing data
print 'The server responded with: ' + data

#closing socket
my_socket.close()
