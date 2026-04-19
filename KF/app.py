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

# ---------------- KF parameters ----------------
dt = 0.01

A = np.array([[1, dt],
              [0, 1]])

C = np.array([[1, 0]])

# process noise (tune this!)
Q = np.array([[1e-4, 0],
              [0, 1e-2]])

# measurement noise (tune this!)
R = np.array([[1e-2]])

# initial state
x_hat = np.array([[0],
                  [0]])  # [position, velocity]

# covariance
P = np.eye(2)

print("KF Receiver running...")

while True:
    data, _ = sock_rx.recvfrom(1024)
    z = float(data.decode().strip())  # measurement (position)

    # ---------------- Prediction ----------------
    x_hat = A @ x_hat
    P = A @ P @ A.T + Q

    # ---------------- Update ----------------
    y = np.array([[z]])  # measurement

    S = C @ P @ C.T + R
    K = P @ C.T @ np.linalg.inv(S)

    x_hat = x_hat + K @ (y - C @ x_hat)
    P = (np.eye(2) - K @ C) @ P

    # results
    x_est = x_hat[0, 0]
    v_est = x_hat[1, 0]

    # send to VOFA
    msg = f"{x_est},{v_est}\n"
    sock_tx.sendto(msg.encode(), (VOFA_IP, VOFA_PORT))

    time.sleep(dt)