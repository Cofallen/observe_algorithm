# 算法开源汇总

本仓库包含控制理论与系统辨识领域的多种算法实现与仿真示例。所有公式使用 LaTeX，代码基于 Python。

> Welcome PR to add control methods!!

## 算法列表（共 7 种）

| 序号 | 算法名称                         | 简要说明                                   | 详细文档               |
|------|----------------------------------|--------------------------------------------|------------------------|
| 1    | 扩张状态观测器 (ESO)             | 估计总扰动，用于自抗扰控制                 | [ESO/readme.md](ESO/readme.md) |
| 2    | 卡尔曼滤波器 (KF)                | 线性高斯系统的最优状态估计                 | [KF/readme.md](KF/readme.md) |
| 3    | 最小二乘法 (LS)                  | 批处理/递推最小二乘，ARX 模型辨识          | [LS/readme.md](LS/readme.md) |
| 4    | MuJoCo Gimbal辨识 + LQR          | 基于最小二乘的参数辨识，LQR 控制           | [LS_mujoco/readme.md](LS_mujoco/readme.md) |
| 5    | Luenberger 观测器                | 线性系统的状态观测器                       | [luenberger/readme.md](luenberger/readme.md) |
| 6    | 滑模控制 / 超螺旋观测器 (SMC)    | 二阶滑模观测器，减弱抖振                   | [SMC/readme.md](SMC/readme.md) |
| 7    | 系统模型库 (System)              | 状态空间方程、ARX、输出误差模型的定义      | [System/readme.md](System/readme.md) |

## 使用说明

1. 进入任一算法文件夹，查看其中的 `readme.md` 了解原理与用法。
2. 运行 `app.py` 或 `main.py` 启动示例。
3. MuJoCo 相关代码需要额外安装 `mujoco` 和 `glfw`，请参考 `LS_mujoco/readme.md`。

## 许可证

MIT License
