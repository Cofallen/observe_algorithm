import socket
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

class VOFA:
    def __init__(self):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_command(self, *data):
        msg = ",".join([f"{d:.5f}" for d in data]) + "\n"
        self.sock.sendto(msg.encode(), (self.UDP_IP, self.UDP_PORT))