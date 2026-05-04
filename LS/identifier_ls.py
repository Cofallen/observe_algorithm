import numpy as np
import socket
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock_rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rx.bind((UDP_IP, UDP_PORT))

dt = 0.01
theta = np.zeros((4, 1))
P = np.eye(4) * 1000  # P

y_k1, y_k2 = 0.0, 0.0
u_k1, u_k2 = 0.0, 0.0

while True:
    data, _ = sock_rx.recvfrom(1024)
    u, y = map(float, data.decode().strip().split(","))

    phi = np.array([[y_k1],
                    [y_k2],
                    [u_k1],
                    [u_k2]])
    
    K = P @ phi /  (1 + phi.T @ P @ phi)
    y_hat = phi.T @ theta
    e = y - y_hat

    theta = theta + K * e
    P = (np.eye(4) - K @ phi.T) @ P

    y_k2 = y_k1
    y_k1 = y
    u_k2 = u_k1
    u_k1 = u

    print(theta.flatten())
    time.sleep(dt)
