import socket
import json
from typing import List

# LED strip configuration:
LED_COUNT = 16      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Server configuration:
UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 15555


class LED_Control:

    def __init__(self) -> None:
        # strip = Adafruit_NeoPixel(
        #     LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # strip.begin()
        pass

    def setCol(self, red: int, green: int, blue: int) -> None:
        # for i in range(self.strip.numPixels()):
        #     self.strip.setPixelColorRGB(i, red, green, blue)
        #     self.strip.show()
        print("Setting color to", red, green, blue)


class Server:

    def __init__(self, led_ctrl: LED_Control) -> None:
        self.led_ctrl = led_ctrl
        self.running = False
        self.prev_data: bytes = None

    def processData(self, rgb: List[int]) -> None:
        assert(len(rgb) == 3)
        assert(all(map(lambda val: 0 <= val <= 255, rgb)))
        self.led_ctrl.setCol(*rgb)

    def run(self) -> None:
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


led_ctrl = LED_Control()
server = Server(led_ctrl)
server.run()
