import ipaddress

class IPManipulator:

    def __init__(self, ip_address):
        # Create an IP address object from the input string
        self.ip_address = ipaddress.ip_address(ip_address)

    def is_ipv4(self):
        # Check if the IP address is an IPv4 address
        return self.ip_address.version == 4

    def is_ipv6(self):
        # Check if the IP address is an IPv6 address
        return self.ip_address.version == 6

    def is_private(self):
        # Check if the IP address is in a private address range
        return self.ip_address.is_private

    def is_loopback(self):
        # Check if the IP address is the loopback address
        return self.ip_address.is_loopback

    def is_link_local(self):
        # Check if the IP address is a link-local address
        return self.ip_address.is_link_local

    def is_multicast(self):
        # Check if the IP address is a multicast address
        return self.ip_address.is_multicast

    def get_hex(self):
        # Get the hexadecimal representation of the IP address
        return hex(int(self.ip_address))[2:]

    def get_bin(self):
        # Get the binary representation of the IP address
        return bin(int(self.ip_address))[2:]

if __name__ == "__main__":
    # Test the IPManipulator class
    ip = IPManipulator("192.168.1.1")

    print(ip.is_ipv4())  # True
    print(ip.is_ipv6())  # False
    print(ip.is_private())  # True
    print(ip.is_loopback())  # False
    print(ip.is_link_local())  # False
    print(ip.is_multicast())  # False

    print(ip.get_hex())  # c0a80101
    print(ip.get_bin())  # 11000000101010000000000100000001
