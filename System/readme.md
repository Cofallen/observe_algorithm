# 状态空间模型 (State-Space Model)

描述动态系统的一种常用形式，包括连续和离散两种。

## 连续系统

$$ \begin{cases} \dot{\mathbf{x}}(t) = A(t) \mathbf{x}(t) + B(t) \mathbf{u}(t) + \mathbf{e}(t) \\ \mathbf{y}(t) = C \mathbf{x}(t) + D \mathbf{u}(t) + \mathbf{v}(t) \end{cases} $$

- $\mathbf{x}$：状态向量
- $\mathbf{u}$：输入向量
- $\mathbf{y}$：输出向量
- $\mathbf{e}, \mathbf{v}$：过程与测量噪声

## 离散系统

$$ \begin{cases} \mathbf{x}(k+1) = A \mathbf{x}(k) + B \mathbf{u}(k) \\ \mathbf{y}(k) = C \mathbf{x}(k) + D \mathbf{u}(k) \end{cases} $$

传递函数矩阵：

$$ G(z) = C (zI - A)^{-1} B + D $$

## 从 ARX 到状态空间

给定 ARX 模型：

$$ y(t) + a_1 y(t-1) + \cdots + a_n y(t-n) = b_1 u(t-1) + \cdots + b_n u(t-n) + e(t) $$

可定义状态为：

$$ x_1(t) = y(t-n), \quad x_2(t) = y(t-n+1), \dots, x_n(t) = y(t-1) $$

即可写出可控标准型状态空间表示。


# ARX 模型 (Auto-Regressive with eXogenous input)

一种线性离散时间模型，当前输出由过去的输出、过去的输入以及白噪声的线性组合构成。

## 模型方程

$$ y(t) = \sum_{i=1}^{n} a_i y(t-i) + \sum_{i=1}^{n} b_i u(t-i) + e(t) $$

更常见的写法：

$$ y(t) + a_1 y(t-1) + \cdots + a_n y(t-n) = b_1 u(t-1) + \cdots + b_n u(t-n) + e(t) $$

## 特点

- 噪声 $e(t)$ 直接加到输出上（方程误差结构）
- 参数估计可用最小二乘法
- 简单实用，但可能产生有偏估计（当噪声不为白噪声时）

## 等价表达

使用延迟算子 $q^{-1}$：

$$ A(q^{-1}) y(t) = B(q^{-1}) u(t) + e(t) $$

其中：

$$ A(q^{-1}) = 1 + a_1 q^{-1} + \cdots + a_n q^{-n} $$
$$ B(q^{-1}) = b_1 q^{-1} + \cdots + b_n q^{-n} $$

# 输出误差模型 (Output Error Model, O-E 或 D-E)

模型结构：系统的无噪声输出由输入经传递函数产生，然后加上输出端噪声。

## 模型定义

$$ y(t) = \frac{B(q^{-1})}{F(q^{-1})} u(t) + e(t) $$

其中：

$$ F(q^{-1}) = 1 + f_1 q^{-1} + \cdots + f_n q^{-n} $$
$$ B(q^{-1}) = b_1 q^{-1} + \cdots + b_n q^{-n} $$

## 与 ARX 的区别

- ARX：噪声直接加到输出方程中（方程误差）
- OE：先由输入生成“真实输出”，再加噪声（输出误差）

因此 OE 模型在信噪比较低时参数估计偏差较小，但优化问题是非线性的，通常需要迭代算法（如预测误差法）。

## 连续时间对应（表达为微分算子）

$$ y(t) = \frac{B(p)}{F(p)} u(t) + e(t), \quad F(p) = 1 + \sum_{i=1}^{n} q_i p^i $$