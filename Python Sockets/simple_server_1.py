import socket

#initiate socket
server_socket = socket.socket()

#bind server to port
server_socket.bind(('0.0.0.0', 1729))

#listen on port
server_socket.listen(1)

#accept new connection
(client_socket, client_address) = server_socket.accept()

#receive data
client_name = client_socket.recv(1024)

#send back same data
client_socket.send('Hello ' + client_name)

#close client socket
client_socket.close()

#close server socket
server_socket.close()