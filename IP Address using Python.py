import socket
hostname=socket.gethostname()
IPAdd=socket.gethostbyname(hostname)
print(IPAdd)