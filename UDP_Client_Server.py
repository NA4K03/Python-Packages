import socket
import threading


class UDPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        # create a UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        message = input("Client -> ")  # take input

        while message.lower().strip() != 'bye':
            # send a message to the server
            udp_socket.sendto(message.encode(), (self.host, self.port))

            # receive the server's response
            data, _ = udp_socket.recvfrom(1024)

            print('Server: ' + data.decode())  # show in terminal
            message = input("Client -> ")  # again take input

        # Send "bye" to the server to inform that client is exiting
        udp_socket.sendto('bye'.encode(), (self.host, self.port))

        # close the socket
        udp_socket.close()


class UDPServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        # create a UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # bind the socket to a specific address and port
        udp_socket.bind((self.host, self.port))

        print("UDP server is listening on {}:{}".format(self.host, self.port))
        print("Type 'bye' to exit the program")
        while True:
            # receive data from a client
            data, address = udp_socket.recvfrom(1024)

            print("Received data from {}: {}".format(address, data.decode()))

            # echo the data back
            udp_socket.sendto(data, address)

            # check if the received data is "bye" to exit the program
            if data.decode().lower().strip() == 'bye':
                print("Closing connection from client: {}".format(address))
                break

        udp_socket.close()  # close the socket once the loop is exited


if __name__ == '__main__':


    # Start UDP server
    udp_server = UDPServer('localhost', 5001)
    udp_server_thread = threading.Thread(target=udp_server.run)
    udp_server_thread.start()

    # Start UDP client
    udp_client = UDPClient('localhost', 5001)
    udp_client.run()