# sender.py
import socket
import time
import math
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

t = 0.0
dt = 0.01

while True:
    # Generate position x
    x = math.sin(2 * math.pi * 0.5 * t) + 0.1 * np.random.randn()  # 0.5 Hz sine with noise

    # send x
    msg = f"{x}\n"
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))

    t += dt
    time.sleep(dt)