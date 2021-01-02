import socket
import json
from typing import List

UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 15555

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


def processData(argb: List[int]):
    assert(len(argb) == 4)
    assert(all(map(lambda val: 0 <= val <= 255, argb)))
    print(argb)


while True:
    data, addr = serverSock.recvfrom(1024)
    argb: List[int] = json.loads(data)
    try:
        processData(argb)
    except Exception as e:
        print(e)
