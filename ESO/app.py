import numpy as np
import socket
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock_rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rx.bind((UDP_IP, UDP_PORT))

VOFA_IP = "127.0.0.1"
VOFA_PORT = 5006
sock_tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


dt = 0.01

w0 = 6.28        # ts=0.01, w0>2*3.14/0.01=62.8 * (1/5 - 1/10)
beta1 = 3 * w0
beta2 = 3 * w0**2
beta3 = w0**3    # high freq, w0

x1_hat = 0.0
x2_hat = 0.0
x3_hat = 0.0

while True:
    data, _ = sock_rx.recvfrom(1024)
    x = float(data.decode().strip())

    e = x - x1_hat

    x1_hat += dt * (x2_hat + beta1 * e)
    x2_hat += dt * (x3_hat + beta2 * e)
    x3_hat += dt * beta3 * e

    v_eso = x2_hat

    msg = f"{x},{v_eso}\n"
    sock_tx.sendto(msg.encode(), (VOFA_IP, VOFA_PORT))

    time.sleep(dt)