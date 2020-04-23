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
            import time
            time.sleep(100)  #This is done to simulate the multiple clinet connection to one server
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
    TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM.
    TCP (SOCK_STREAM) is a connection-based protocol. The connection is established and the two parties have a conversation until the connection is terminated by one of the parties or by a network error.
    UDP (SOCK_DGRAM) is a datagram-based protocol. You send one datagram and get one reply and then the connection terminates.
    socket.SOL_SOCKET

    socket.SO_REUSEADDR
    SO_REUSEADDR allows your server to bind to an address which is in a
    TIME_WAIT state.
    This socket option tells the kernel that even if this port is busy (in the TIME_WAIT state), go ahead and reuse it anyway. If it is busy, but with another state, you will still get an address already in use error. It is useful if your server has been shut down, and then restarted right away while sockets are still active on its port.
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
