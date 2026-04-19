# receiver.py
import socket
import time

# UDP receive (from sender)
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock_rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rx.bind((UDP_IP, UDP_PORT))

# UDP send (to VOFA+)
VOFA_IP = "127.0.0.1"
VOFA_PORT = 5006

sock_tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# -------- parameters --------
dt = 0.01

# discrete derivative
x_prev = 0.0

# Luenberger observer states
x_hat = 0.0
v_hat = 0.0

# observer gains (tune this!)
L1 = 20.0
L2 = 200.0

print("Receiver running...")

while True:
    data, _ = sock_rx.recvfrom(1024)
    x = float(data.decode().strip())

    # --------------------------
    # Method 1: Discrete derivative
    # --------------------------
    v_discrete = (x - x_prev) / dt
    x_prev = x

    # --------------------------
    # Method 2: Luenberger observer
    # --------------------------
    error = x - x_hat

    x_hat += dt * v_hat + L1 * error * dt
    v_hat += L2 * error * dt

    v_luenberger = v_hat

    # --------------------------
    # Send to VOFA+
    # --------------------------
    msg = f"{x},{v_discrete},{v_luenberger}\n"
    sock_tx.sendto(msg.encode(), (VOFA_IP, VOFA_PORT))

    time.sleep(dt)