import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6000)
print ('starting up on',server_address)
sock.bind(server_address)
sock.listen(5)
while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ('connection from', client_address)
        while True:
            data = connection.recv(1024)
            print ('received',data)
            if data:
                print ('sending data back to the client')
                connection.sendall(data)
            else:
                print ('no more data from', client_address)
                break
            
    finally:
        connection.close()
        
