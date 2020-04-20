import optparse
import os
import socket
import time


def parser_args():
    usage = """
    usage of server.py is documented here
    """
    parser = optparse.OptionParser(usage)
    parser.add_option('--port', help="port given for server", type=int)
    parser.add_option('--ip', help="ip given for the server", default="localhost")
    options, _ = parser.parse_args()
    return options


def client(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))
    s.close()


def main():
    options = parser_args()
    print(options.port)
    print(options.ip)
    client(options.ip, options.port)
    pass


if __name__ == "__main__":
    main()
