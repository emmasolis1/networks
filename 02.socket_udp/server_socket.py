# Author: Emmanuel D. Solis.
from socket import *

server_port = 13000 # Must be the same as where the client will connect.
server_socket = socket(AF_INET, SOCK_DGRAM) # Creates the socket.
server_socket.bind(('', server_port)) # The program assign the server port number for this socket.

print("Server is online to receive request")
while True: # Will listen forever.
  message, client_address = server_socket.recvfrom(2048) # Receive the message from the client.
  print("Connection established succesfully")
  # modified_message = message.decode().upper() # Decodifies the message and transform it into upper case.
  modified_message = "Hola, soy el servidor."
  server_socket.sendto(modified_message.encode(), client_address) # Once transform we send it back to the client.