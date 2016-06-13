import socket

import sys

#initializing socket
my_socket = socket.socket()

#connecting to remote server
my_socket.connect(('127.0.0.1', 1729))

for i in range(100):
    #receiving data from user
    input_data = raw_input('Enter TIME, NAME or RAND:')

    if len(input_data) != 4:
        print 'Error! Illegal input, try again'
        continue
    else:
        # sending data to server
        my_socket.send(input_data)


    #receiving data from server
    data = my_socket.recv(1024)
    if data != "":
        print 'The server responded with: ' + data
    else:
        print 'No response from server'


#closing socket
my_socket.close()
