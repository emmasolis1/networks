# Author: Emmanuel D. Solis.
from socket import *

server_name = 'localhost' # Address of the server, it could be like ucr.ac.cr in which case the DNS will tranform into an IP or either the IP directly.
server_port = 12000 # The specific socket to which we want to connect because a server could be running multiple sockets for diferent programs.
client_socket = socket(AF_INET, SOCK_DGRAM) # Creates the socket. AF_INET == IPv4
print('Escriba un mensaje de saludo para enviar al server:')
message = input()
client_socket.sendto(message.encode(), (server_name, server_port)) # Parse the data to bytes and send the request to the server socket.
new_message, server_address = client_socket.recvfrom(2048) # Receive from the server the new message (into new_message) and the info about the server (into server_addres, both IP and Port Number)
print('Mensaje recibido desde el server:', new_message.decode())
print("Information from the server is: ", server_address)

client_socket.close() # Terminates the execution.