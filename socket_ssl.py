import socket
import sys


# Define a SocketClient class
class SocketClient:

    # Initialize the class
    def __init__(self):
        # Create a new socket object
        self.s = socket.socket()

    # Define a method to create a new socket
    def create_socket(self):
        try:
            # Create a new TCP/IP socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as err:
            print("socket creation failed with error %s" % (err))

    # Define a method to resolve the host IP address
    def resolve_host(self, host):
        try:
            # Get the IP address of the host
            host_ip = socket.gethostbyname(host)
        except socket.gaierror:
            print("there was an error resolving the host")
            sys.exit()

        # Return the IP address
        return host_ip

    # Define a method to connect to a remote server
    def connect_to_server(self, host_ip, port):
        try:
            # Connect to the server at the specified IP address and port
            self.s.connect((host_ip, port))
        except:
            print("Unable to connect to the server")

    # Define a method to bind the socket to a local port
    def bind_socket(self, port):
        try:
            # Bind the socket to the specified port
            self.s.bind(('', port))
            print("socket binded to %s" % (port))
        except socket.error as err:
            print("socket binding failed with error %s" % (err))

    # Define a method to listen for incoming connections
    def listen_to_socket(self):
        # Start listening for incoming connections
        self.s.listen(5)
        print("socket is listening")

        while True:
            # Accept a new connection
            c, addr = self.s.accept()
            print('Got connection from', addr)

            # Send a message to the client
            c.send('Thank you for connecting'.encode())

            # Close the connection
            c.close()

            # Exit the loop
            break

    # Define a method to connect to a local server
    def connect_to_local_server(self, port):
        # Connect to the local server at the specified port
        self.s.connect(('127.0.0.1', port))

        # Receive a message from the server and print it
        print(self.s.recv(1024).decode())

        # Close the connection
        self.s.close()

    # Define a method to run the socket client
    def run(self):
        # Create a new socket
        self.create_socket()

        # Resolve the IP address of the remote server
        host_ip = self.resolve_host('www.google.com')

        # Connect to the remote server at port 80
        self.connect_to_server(host_ip, 80)
        print("the socket has successfully connected to google")

        # Close the socket
        self.s.close()

        # Create a new socket
        self.create_socket()

        # Bind the socket to port 12345
        self.bind_socket(12345)

        # Listen for incoming connections
        self.listen_to_socket()

        # Create a new socket
        self.create_socket()

        # Connect to the local server at port 12345
        self.connect_to_local_server(12345)


# If the script is being run as the main program
if __name__ == '__main__':
    # Create a new instance of the SocketClient class
    client = SocketClient()
    client.run()