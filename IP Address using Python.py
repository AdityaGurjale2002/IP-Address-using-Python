import socket
hostname=socket.gethostname()
IPAdd=socket.gethostbyname(hostname)
print("Computer Name is: " + hostname)
print("Your IP Address is: " + IPAdd)
