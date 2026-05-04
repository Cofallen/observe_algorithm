import socket
import time
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dt = 0.01
t = 0.0

# system param
a1 = 1.5
a2 = -0.7
b1 = 0.5
b2 = 0.1

y_k1, y_k2 = 0.0, 0.0
u_k1, u_k2 = 0.0, 0.0

while True:
    u = np.sin(2*np.pi*0.5*t) + 0.5*np.sin(2*np.pi*10.0*t)

    y = a1 * y_k1 + a2 * y_k2 + b1 * u_k1 + b2 * u_k2
    y += 0.05 * np.random.randn()

    msg = f"{u},{y}\n"
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))

    y_k2 = y_k1
    y_k1 = y
    u_k2 = u_k1
    u_k1 = u

    t += dt
    time.sleep(dt)