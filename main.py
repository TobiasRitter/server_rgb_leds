import socket
import json

UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 15555

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    rgb = json.loads(data)
    print(rgb)
