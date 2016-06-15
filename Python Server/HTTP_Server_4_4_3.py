import socket
import os

from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

#initiate socket
server_socket = socket.socket()

#bind server to port
HOST = '127.0.0.1'
PORT = 80
server_socket.bind((HOST, PORT))

#listen on port
server_socket.listen(1)
while True:
    #accept new connection
    (client_socket, client_address) = server_socket.accept()

    while True:

        print 'New Client\n'

        #receive data
        client_data = client_socket.recv(1024)

        #handle case where client closed connection
        if not client_data:
            break

        #check if request == GET
        request = HTTPRequest(client_data)


        if (request.command == "GET") and (request.request_version == "HTTP/1.1"):
            if os.path.isfile(request.path):
                with open(request.path, 'rb') as f:
                    bytesToSend = f.read(os.path.getsize(request.path))
                    client_socket.send(bytesToSend)
            else:
                client_socket.send('Error, no such file!' + request.path)
        break

    # close client socket
    client_socket.close()

#close server socket
server_socket.close()