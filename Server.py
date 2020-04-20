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


def serverpart(sock, addr):
    """
    This is the methond which serves one clinent. Reads 1024 bytes and echos to the server
    """
    while True:
        print('Client connection received from  %s !' % (addr,))
        data = sock.recv(1024)
        if not data:
            """
            TODO: sock.close or not does not makes a difference.
            But there is some limit. I remembe when I was refractoring the TTS accpeter. I ended up in crashing
            server. Check once and clarify
            """
            sock.close()
            break
        print(data)
        try:
            sock.sendall(data)  # this is a blocking call
            print('Data sent', data)
        except socket.error:
            sock.close()
            return
    print("One request completed")


def serve(listen_socket):
    """
    This method will be looping for all the client which request for the server
    TODO: Test what will happen if two client connects at the same time
         Add some sleep in server and test
    """
    while True:
        sock, addr = listen_socket.accept()
        serverpart(sock, addr)


def server_start(ip, port):
    """
    This will create the socket with below options and bind provided ip and port
    TODO: What is listen
    socket.AF_INET
    socket.SOCK_STREAM
    socket.SOL_SOCKET
    socket.SO_REUSEADDR
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port or 0))
    sock.listen(5)

    serve(sock)


def main():
    options = parser_args()
    print(options.port)
    print(options.ip)
    server_start(options.ip, options.port)
    pass


if __name__ == "__main__":
    main()
