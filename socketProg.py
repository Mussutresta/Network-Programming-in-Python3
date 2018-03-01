import socket

# initialize a socket! here AF_INET is simply the kind of connection that you want the socket to have
#SOCK_STREAM allows you to have a TCP connection. You may have a DGRAM for UDP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

# To communicate with a server, let us say a remote server

server ="google.com"

#Next, specify what port we want to communicate on, 80 for http

port=80

#You can also communicate using server's IP address

server_ip= socket.gethostbyname(server)

print(server_ip)

#make request

request= "GET / HTTP/1.1\n" + server+ "\n"

#Now connect the server and the prot

s.connect((server, port))

#In Python3, the data is in Byte string format that is the incorrect format, so we need to encode. This 
#isn't a problem in Python2.7

s.send(request.encode())

#1024 and 4096 etc is the buffer, that is how much data do we need to store at a time
result=s.recv(4096)

#print(result)

#The result will have the srever, port, server ip address, the request that we made which starts with a 'b':denoting byte code 

#else you could buffer and not print everythin al at once. 

while(len(result)>0):
	print(result)
	result=s.recv(1024)









