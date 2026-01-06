---
layout: post
title: "SageMath + VSCode 配置"
---

---

本文为 SageMath 多版本内核配置指南 - WSL2 + VSCode 集成，在 WSL2 Ubuntu 已安装 SageMath 9.5 的情况下，说明如何在 VSCode 中配置使用虚拟环境中的 [SageMath 10.3](https://mengcezheng.github.io/sagemath/) 。

## 环境准备

### 系统环境

- **操作系统**: Windows 10 + WSL2 (Ubuntu 22.04)  
- **工具链**:  
  - VSCode 扩展: `Remote - WSL`, `Python`, `Jupyter`  
  - 包管理器: `miniconda3`, `miniforge3`

### 软件版本

| 名称             | 版本   | 安装位置              |
|------------------|--------|-----------------------|
| SageMath         | 9.5    | 系统全局 (`/usr/bin`) |
| SageMath         | 10.3   | miniforge 虚拟环境    |
| Jupyter Client   | ≥7.0   | 虚拟环境              |

---

## 旧版 SageMath 9.5 全局配置

### 内核信息

```bash
# 进入虚拟环境
mamba activate sage-dev

# 查看内核文件
jupyter kernelspec list

# 验证路径
ls /usr/share/jupyter/kernels/sagemath/kernel.json
```

### 文件内容

```json
// cat /usr/share/jupyter/kernels/sagemath/kernel.json
{
  "argv": ["/usr/bin/sage", "--python", "-m", "sage.repl.ipython_kernel", "-f", "{connection_file}"],
  "display_name": "SageMath",
  "language": "sage"
}
```

---

## 新版 SageMath 10.3 虚拟环境配置

### 步骤概览

1. **创建虚拟环境**: 详见 [SageMath 10.3](https://mengcezheng.github.io/sagemath/)

2. **内核注册**:  

   ```bash
   mamba activate sage-dev
   mkdir -p $CONDA_PREFIX/share/jupyter/kernels/sagemath10.3
   ```

3. **编写内核配置**:

   ```bash
   cat << EOF > $CONDA_PREFIX/share/jupyter/kernels/sagemath10.3/kernel.json
   {
     "argv": ["$CONDA_PREFIX/bin/python", "-m", "sage.repl.ipython_kernel", "-f", "{connection_file}"],
     "display_name": "SageMath 10.3",
     "language": "sage"
   }
   EOF
   ```

4. **注册到 Jupyter**:

   ```bash
   jupyter kernelspec install $CONDA_PREFIX/share/jupyter/kernels/sagemath10.3 --user --name "sagemath10.3"
   ```

---

## 内核冲突解决

### 关键操作

- 路径冲突: `mv /usr/share/jupyter/kernels/sagemath /usr/share/jupyter/kernels/sagemath9.5`
- 环境变量覆盖: 在 `kernel.json` 中显式指定虚拟环境的 Python 路径

---

## 内核命名优化

### 修改显示

1. **旧版内核**:

   ```bash
   sudo nano /usr/share/jupyter/kernels/sagemath9.5/kernel.json
   # 修改 "display_name": "SageMath 9.5"
   ```

2. **新版内核**:

   ```bash
   nano $CONDA_PREFIX/share/jupyter/kernels/sagemath10.3/kernel.json
   # 修改 "display_name": "SageMath 10.3"
   ```

### 最终效果

```bash
mamba activate sage-dev
jupyter kernelspec list
Available kernels:
  python3         /home/user/miniforge3/envs/sage-dev/share/jupyter/kernels/python3
  sagemath10.3    /home/user/miniforge3/envs/sage-dev/share/jupyter/kernels/sagemath10.3
  sagemath9.5     /usr/share/jupyter/kernels/sagemath9.5
```

---

## 验证与测试

### 测试代码

```python
# 版本验证
print(f"SageMath Version: {sage.version.version}")

# 功能验证
print(f"ceil(3.14) = {ceil(3.14)}")  # 应输出 4
print(f"factor(10) = {factor(10)}")  # 应输出 2 * 5
```

### 预期输出

| 内核名称       | `sage.version.version` | `ceil(3.14)` |
|----------------|------------------------|--------------|
| SageMath 9.5   | 9.5                    | 4            |
| SageMath 10.3  | 10.3                   | 4            |

---

> 通过本指南，可实现在单一 Jupyter 环境中管理多版本 SageMath 内核，并保持环境隔离性和命名简洁性。本文撰写过程中参考 [DeepSeek](https://www.deepseek.com/) 提供的建议与方案。
