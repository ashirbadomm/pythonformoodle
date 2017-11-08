import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6000)
print ('connecting to ' , server_address)
sock.connect(server_address)
try:
    message = 'This is the message.  It will be repeated.'
    print ('sending', message)
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received',data)

finally:
    print('closing socket')
    sock.close()
