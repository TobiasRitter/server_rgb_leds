import socket
import json
from typing import List

UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 15555


class Server:

    def __init__(self):
        self.running = False
        self.prev_data: bytes = None

    def processData(self, argb: List[int]):
        assert(len(argb) == 4)
        assert(all(map(lambda val: 0 <= val <= 255, argb)))
        print(argb)

    def run(self):
        self.running = True
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

        while self.running:
            data, _ = serverSock.recvfrom(1024)
            argb: List[int] = json.loads(data)
            try:
                if self.prev_data == None or data != self.prev_data:
                    self.prev_data = data
                    self.processData(argb)
            except Exception as e:
                print(e)


server = Server()
server.run()
