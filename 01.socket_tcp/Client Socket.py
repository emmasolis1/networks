import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print ('Conectando con %s puerto %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'Hola Mundo!'.encode()
    print ('Enviando "%s"' % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ('Recibido "%s"' % data)

finally:
    print ('Cerrando socket')
    sock.close()