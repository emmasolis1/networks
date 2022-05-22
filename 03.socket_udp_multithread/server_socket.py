# Author: Emmanuel D. Solis y Gilbert Marquez.
from socket import *
import threading
import time
SERVER_ADDRESS = ('localhost', 12000)

def main():
  wait_connections()

# Forever waiting for new connections.
def wait_connections():
  server_socket = socket(AF_INET, SOCK_DGRAM) # Creates the socket.
  server_socket.bind(SERVER_ADDRESS)
  print("Server is online to receive request")
  while True:
    # Socket principal espera.
    message, client_address = server_socket.recvfrom(2048) # Receive the message from the client.
    # Cuando se da la conexion se crea un nuevo hilo para atender el cliente.
    client_connection = threading.Thread(target=handle_connection, args=(message, client_address, server_socket))
    client_connection.daemon = True
    # El hilo debe tener una subrutina para atender ese cliente.
    client_connection.start()

# Method for each thread to handle his own client.
def handle_connection(message, client_address, server_sock):
  print("A new thread has successfully accepted the connection from ", client_address)
  data = message.decode()
  data = data.upper()
  time.sleep(5.0)
  server_sock.sendto(data.encode(), client_address)

# Initializing the code.
if __name__ == "__main__":
  main()