import socket
import threading


class TCPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        client_socket.connect((self.host, self.port))  # connect to the server
        message = input("Client -> ")  # take input

        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            print('Received from server: ' + data)  # show in terminal

            message = input("Client -> ")  # again take input

        client_socket.send('bye'.encode())
        client_socket.close()  # close the connection


class TCPServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        server_socket = socket.socket()  # get instance
        server_socket.bind((self.host, self.port))  # bind host address and port together
        print("Type bye on both server and client side to exit the program")

        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            data = input('server -> ')
            if data.lower().strip() == 'bye':
                conn.send('bye'.encode())
                break
            conn.send(data.encode())

            if data.lower().strip() == 'bye':
                break

        conn.close()  # close the connection

if __name__ == '__main__':
    # Start TCP server
    tcp_server = TCPServer('localhost', 5000)
    tcp_server_thread = threading.Thread(target=tcp_server.run)
    tcp_server_thread.start()

    # Start TCP client
    tcp_client = TCPClient('localhost', 5000)
    tcp_client.run()
