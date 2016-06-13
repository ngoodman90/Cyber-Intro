import socket

#initializing socket
my_socket = socket.socket()

#connecting to remote server
my_socket.connect(('127.0.0.1', 1729))

#sending name to server
my_socket.send('Hello Echo Server')

#receiving data from server
data = my_socket.recv(1024)

#printing data
print 'The server responded with: ' + data

#closing socket
my_socket.close()
