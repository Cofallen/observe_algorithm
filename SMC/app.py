import numpy as np
import socket
import time
import math

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock_rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rx.bind((UDP_IP, UDP_PORT))

VOFA_IP = "127.0.0.1"
VOFA_PORT = 5006
sock_tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# -------- parameters --------
dt = 0.01

# SMC states
x_hat = 0.0
v_hat = 0.0

# gains (VERY important to tune)
k1 = 5.0
k2 = 20.0

def sign(x):
    if x > 0:
        return 1.0
    elif x < 0:
        return -1.0
    else:
        return 0.0

print("SMC observer running...")

while True:
    data, _ = sock_rx.recvfrom(1024)
    x = float(data.decode().strip())

    # ---------------- SMC observer ----------------
    e = x - x_hat

    x_hat += dt * (v_hat + k1 * math.sqrt(abs(e)) * sign(e))
    v_hat += dt * (k2 * sign(e))

    # output
    msg = f"{x},{v_hat}\n"
    sock_tx.sendto(msg.encode(), (VOFA_IP, VOFA_PORT))

    time.sleep(dt)