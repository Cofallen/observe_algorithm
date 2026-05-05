import numpy as np
from scipy import linalg

# 系统参数
a1 = 1.38650793
a2 = -0.38650716
b1 = -0.58701908
b2 = 0.59800539

# 状态空间矩阵
A = np.array([
    [a1, a2, b1],
    [1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0]
])

B = np.array([
    [b2],
    [0.0],
    [1.0]
])

C = np.array([[1.0, 0.0, 0.0]])
D = np.array([[0.0]])

# LQR 权重矩阵（可以调）
Q = np.diag([10, 1, 1])
R = np.array([[1]])

# 求解离散 Riccati 方程
P = linalg.solve_discrete_are(A, B, Q, R)

# 计算 LQR 增益
K = np.linalg.inv(B.T @ P @ B + R) @ (B.T @ P @ A)

print("K =", K)