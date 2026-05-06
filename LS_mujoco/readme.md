# 双关节机械臂系统辨识实验

## 实验目的
通过正弦信号激励，辨识 MuJoCo 模型中电机 m1（驱动 joint1）的等效转动惯量 `J` 和粘性阻尼系数 `B`。

## 系统概述
- 仿真环境：MuJoCo
- 机械结构：基部固定（base_body），上装配 Part473_body（绕 Z 轴铰链 joint1），Part474_body 安装在 Part473 上（绕 X 轴铰链 joint2）。
- 驱动：电机 m1 作用于 joint1，力矩/位置控制；m2 作用于 joint2（本次实验保持锁定或不受力）。
- 传感器：记录 joint1 的位置（角度）和速度。

## LQR control

NOTE: I use `u = 0.3 * np.sin(2*np.pi*0.5*t) ` to identify this gimbal system, get param. Though use 3 state function to LQR control, the control is stable. But the corresponding time is too long.

So, I use chrip frenquency signal to identify this system, get these param, only has `a1 a2`, `b1 b2` is nearly 1e-3. Which causes LQR Ricatti Equation has not been successfully solved. I simple this system, change it inito 2 state function, but the param matrix `A B Q R` is choosed difficultly. If Q or R is big, this function is not solved. Even the two rank is controlled.

Maybe there are some IMPORTANT THINGS I HAVE NOT DISCOVERD. But for now, PID is better than LQR or other algorithm, if your system is not good by identified or computed.