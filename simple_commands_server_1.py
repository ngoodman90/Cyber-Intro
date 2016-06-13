import socket
import sys
import time
import random

#initiate socket
server_socket = socket.socket()

#bind server to port
server_socket.bind(('0.0.0.0', 1729))

#listen on port
server_socket.listen(1)


#accept new connection
(client_socket, client_address) = server_socket.accept()

#receive data
client_data = client_socket.recv(1024)

for i in range(100):
    if client_data == 'TIME':
        localtime = time.localtime(time.time())
        client_socket.send(localtime)

    elif client_data == 'NAME':
        client_socket.send('Hi, my name is Andy')

    elif client_data == 'RAND':
        rand_num = random.randrange(1, 11, 2)
        client_socket.send(rand_num)

    elif client_data == 'EXIT':
        client_socket.send('Server is shutting down')
        break

    else:
        client_socket.send('Invalid request! Try again')

# close client socket
client_socket.close()
#close server socket
server_socket.close()