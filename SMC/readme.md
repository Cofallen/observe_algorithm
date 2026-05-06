# 超螺旋滑模观测器 (Super-Twisting Sliding Mode Observer)

二阶滑模观测器，用于在存在扰动时实现对状态变量的连续估计，同时减弱传统滑模的抖振现象。

## 算法形式

对于系统 $\dot{x} = v + u$（其中 $v$ 为未知项），观测器结构：

$$ \dot{\hat{x}} = u + k_1 |s|^{1/2} \text{sign}(s) $$

$$ \dot{u} = k_2 \text{sign}(s) $$

其中滑模面 $s = x - \hat{x}$。

## 离散实现（近似）

$$ s_k = x_k - \hat{x}_k $$

$$ \hat{x}_{k+1} = \hat{x}_k + T_s \left( u_k + k_1 |s_k|^{1/2} \text{sign}(s_k) \right) $$

$$ u_{k+1} = u_k + T_s \cdot k_2 \text{sign}(s_k) $$

## 参数设计与 Lyapunov 稳定

参数 $k_1, k_2$ 需满足：

$$ k_1 > 0, \quad k_2 > \text{扰动上界} $$

以保证有限时间收敛。

## 对比方法

- Luenberger 观测器（线性）
- 标准滑模观测器（SMO）
- ESO（扩展状态观测器）

## RUN

```bash
python send.py  # one shell
python app.py     # another shell
```

THen Start VOFA+, choose UDP , set Firewater mode and set port `5006` to read data.