import socket

# initiate socket
server_socket = socket.socket()

# bind server to port
HOST = '127.0.0.1'
PORT = 80
server_socket.bind((HOST, PORT))

# listen on port
server_socket.listen(1)
while True:
    # accept new connection
    (client_socket, client_address) = server_socket.accept()

    while True:

        print 'New Client\n'

        # receive data
        client_data = client_socket.recv(1024)

        # handle case where client closed connection
        if not client_data:
            break

    # close client socket
    client_socket.close()

# close server socket
server_socket.close()