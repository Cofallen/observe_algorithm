# 扩张状态观测器 (Extended State Observer, ESO)

ESO 将系统总扰动（内部不确定性和外部扰动）扩张为一个新状态，进行在线估计。

## 系统描述

考虑单输入单输出系统：

$$
\dot{y} = f(t) + u(t) + d(t)
$$

其中 $d(t)$ 为总扰动。

定义状态：

$$ 
x_1 = y, \quad x_2 = d(t) 
$$

则扩张状态方程为：

$$ 
\begin{cases} \dot{x}_1 = x_2 + u \\ \dot{x}_2 = h(t) \end{cases} 
$$

## 线性 ESO 形式

$$ 
\begin{cases} \dot{\hat{x}}_1 = \hat{x}_2 + u + \beta_1 (y - \hat{x}_1) \\ \dot{\hat{x}}_2 = \beta_2 (y - \hat{x}_1) \end{cases} 
$$

参数选择（带宽法）：

$$ 
\beta_1 = 2\omega_o, \quad \beta_2 = \omega_o^2 
$$

其中 $\omega_o$ 为观测器带宽。

## 离散化实现（前向欧拉）

$$ 
e(k) = y(k) - \hat{x}_1(k) 
$$

$$ 
\hat{x}_1(k+1) = \hat{x}_1(k) + T_s \left( \hat{x}_2(k) + u(k) + \beta_1 e(k) \right) 
$$

$$ 
\hat{x}_2(k+1) = \hat{x}_2(k) + T_s \beta_2 e(k) 
$$

## 参数说明

- $T_s$：采样周期
- $\beta_1, \beta_2$：观测器增益
- $\omega_o$：带宽（通常 $\omega_o = 70$ 或更高）

## RUN

```bash
python signal.py  # one shell
python app.py     # another shell
```

THen Start VOFA+, choose UDP , set Firewater mode and set port `5006` to read data.