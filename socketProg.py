import socket

# initialize a socket! here AF_INET is simply the kind of connection that you want the socket to have
#SOCK_STREAM allows you to have a TCP connection. You may have a DGRAM for UDP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

# To communicate with a server, let us say a remote server

server ="pythonpragramming.net"

#Next, specify what port we want to communicate on, 80 for http

port=80

#You can also communicate using server's IP address

server_ip= socket.gethostbyname(server)

