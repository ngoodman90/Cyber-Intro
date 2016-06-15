import socket
import time

import sys



while True:

    # initializing socket
    my_socket = socket.socket()

    #connecting to remote server
    my_socket.connect(('127.0.0.1', 1729))



    #receiving data from user
    input_data = raw_input('Enter TIME, NAME or RAND:')

    if (input_data != 'NAME' and input_data != 'TIME' and input_data != 'RAND'):
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

    time.sleep(2)
    #closing socket
    my_socket.close()
