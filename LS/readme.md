# 最小二乘法用于系统辨识 (Least Squares for System Identification)

最小二乘法（LS）是线性系统辨识中最基础的参数估计方法，尤其适用于 **ARX 模型**（方程误差结构）。本文件介绍其基本形式、矩阵解法、递推实现以及在辨识中的应用步骤。

## 1. 辨识模型结构

考虑 ARX 模型：

$$ y(k) + a_1 y(k-1) + \cdots + a_n y(k-n) = b_1 u(k-1) + \cdots + b_n u(k-n) + e(k) $$

其中 $e(k)$ 为白噪声（方程误差）。也可写为：

$$ y(k) = \boldsymbol{\varphi}^T(k) \boldsymbol{\theta} + e(k) $$

- 回归向量 $\boldsymbol{\varphi}(k) = [-y(k-1), \dots, -y(k-n), u(k-1), \dots, u(k-n)]^T$
- 参数向量 $\boldsymbol{\theta} = [a_1, \dots, a_n, b_1, \dots, b_n]^T$

## 2. 批处理最小二乘

采集 $N$ 组数据（$N > 2n$），构造：

$$ \mathbf{Y} = \Phi \boldsymbol{\theta} + \mathbf{E} $$

其中：

$$ \mathbf{Y} = \begin{bmatrix} y(1) \\ y(2) \\ \vdots \\ y(N) \end{bmatrix}, \quad 
\Phi = \begin{bmatrix} \boldsymbol{\varphi}^T(1) \\ \boldsymbol{\varphi}^T(2) \\ \vdots \\ \boldsymbol{\varphi}^T(N) \end{bmatrix} $$

**最小二乘解**：

$$ \hat{\boldsymbol{\theta}} = (\Phi^T \Phi)^{-1} \Phi^T \mathbf{Y} $$

### 适用条件

- $\Phi^T \Phi$ 非奇异（输入信号持续激励）
- 噪声 $e(k)$ 为零均值、与输入不相关（无偏条件）

## 3. 递推最小二乘 (RLS)

适用于在线辨识，避免矩阵求逆：

**初始化**：

$$ \hat{\boldsymbol{\theta}}(0) = \mathbf{0}, \quad P(0) = \alpha I \quad (\alpha \text{大数，如 } 10^4) $$

**每一步 $k$ 更新**：

1. 计算预测误差
   $$ \varepsilon(k) = y(k) - \boldsymbol{\varphi}^T(k) \hat{\boldsymbol{\theta}}(k-1) $$

2. 计算增益向量
   $$ L(k) = \frac{P(k-1) \boldsymbol{\varphi}(k)}{ \lambda + \boldsymbol{\varphi}^T(k) P(k-1) \boldsymbol{\varphi}(k) } $$

3. 更新参数估计
   $$ \hat{\boldsymbol{\theta}}(k) = \hat{\boldsymbol{\theta}}(k-1) + L(k) \varepsilon(k) $$

4. 更新协方差矩阵
   $$ P(k) = \frac{1}{\lambda} \left[ I - L(k) \boldsymbol{\varphi}^T(k) \right] P(k-1) $$

其中 $\lambda$ 为遗忘因子（$0.95 \le \lambda \le 1$）。$\lambda = 1$ 时无遗忘（定常系统）；$\lambda < 1$ 用于时变系统。

## 4. 辨识步骤总结

1. 采集输入 $u(k)$ 和输出 $y(k)$ 数据（激励信号如 PRBS、正弦扫频等）
2. 选择模型阶次 $n$（可通过 AIC、交叉验证或已知物理结构）
3. 构造 $\Phi$ 和 $\mathbf{Y}$（批处理）或直接运行 RLS
4. 计算参数估计 $\hat{\boldsymbol{\theta}}$
5. 验证模型：比较模型输出与实际输出，检查残差是否为白噪声

## RUN

```bash
python sender.py  # one shell
python identifier_ls.py     # another shell
```
