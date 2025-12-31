---
layout: post
title: "格密码分析之格筛法简要概述"
---

---

## 引言

随着计算能力的飞速发展，特别是量子计算的潜在威胁日益临近，传统公钥密码体系（如RSA、ECC）的安全性面临严峻挑战。在后量子密码（Post-Quantum Cryptography, PQC）的研究浪潮中，格密码（Lattice-Based Cryptography, LBC）凭借其对量子攻击的推定抵抗性以及支持高级密码学功能（如全同态加密）的潜力，成为了最有前途的研究方向之一，并已在NIST PQC标准化进程中占据核心地位。

格密码的安全性通常基于格（Lattice）上的一些困难问题的计算复杂性，其中最著名的包括最短向量问题（Shortest Vector Problem, SVP）和最近向量问题（Closest Vector Problem, CVP）。格密码分析（Lattice Cryptanalysis）旨在评估和攻击这些基于格的密码系统，而理解和改进解决SVP和CVP等问题的算法，对于准确评估格密码方案的安全强度至关重要。

在众多解决格困难问题的算法中，格基约化算法（如LLL, BKZ）和枚举算法（Enumeration）长期占据主导地位。然而，近年来，格筛法（Lattice Sieving Methods）作为一类在理论上具有最佳渐进复杂度的算法，受到了越来越多的关注。格筛法通过在格中生成大量向量并迭代地“筛选”出更短的向量，为解决高维SVP问题提供了一种强大的启发式及概率性工具。本文将简要概述格筛法的基本原理、主流算法、在密码分析中的应用、面临的挑战以及未来的发展方向。

## 格理论基础

为了理解格筛法，我们首先需要了解一些基本的格理论概念。

### 格的定义

一个 $n$ 维欧氏空间 $\mathbb{R}^m$ 中的**格 (Lattice)** $L$ 是由一组线性无关的向量 $\mathbf{b}_1, \mathbf{b}_2, \dots, \mathbf{b}_n \in \mathbb{R}^m$ (其中 $n \le m$) 的所有整系数线性组合构成的离散子群：

$$
L = \left\{ \sum_{i=1}^n a_i \mathbf{b}_i \mid a_i \in \mathbb{Z} \right\}
$$

这组向量 $\{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ 被称为格 $L$ 的一组**格基 (Basis)**。格的维度 (Dimension) 或秩 (Rank) 指的是其基向量的数量 $n$。如果 $n=m$，则称该格为满秩格。

### 格基与行列式

同一个格可以有多组不同的基。例如，对于一个二维格，向量 $\{\mathbf{b}_1, \mathbf{b}_2\}$ 和 $\{\mathbf{b}_1, \mathbf{b}_1 + \mathbf{b}_2\}$ 可以生成同一个格。

格的一个重要不变量是其**行列式 (Determinant)** 或**体积 (Volume)**，记作 $\det(L)$ 或 $\text{vol}(L)$。它表示由格基向量构成的基本平行多面体的 $n$ 维体积。对于一个由基矩阵 $B = [\mathbf{b}_1, \dots, \mathbf{b}_n]$ （列向量为基向量）生成的格，其行列式定义为：

$$
\det(L) = \sqrt{\det(B B^\mathsf{T})}
$$

如果格是满秩的 ($n=m$)，则 $\det(L) = \vert\det(B)\vert$。行列式的值与格基的选择无关。

### 最短向量问题与最近向量问题

格密码的安全性与以下两个核心困难问题密切相关：

1. **最短向量问题 (Shortest Vector Problem - SVP):** 给定一个格 $L$，找到一个非零格向量 $\mathbf{v} \in L \setminus \{\mathbf{0}\}$，使得其欧几里得范数 $\Vert\mathbf{v}\Vert$ 最小。这个最小范数通常记为 $\lambda_1(L)$。SVP被认为是NP难问题（在随机规约下）。
2. **最近向量问题 (Closest Vector Problem - CVP):** 给定一个格 $L$ 和一个目标向量 $\mathbf{t} \in \mathbb{R}^m$，找到一个格向量 $\mathbf{v} \in L$，使得其与目标向量 $\mathbf{t}$ 之间的距离 $\Vert\mathbf{v} - \mathbf{t}\Vert$ 最小。CVP也被认为是NP难问题，且通常认为比SVP更难。

在密码分析中，我们通常需要解决这些问题的近似版本（$\gamma$-SVP 或 $\gamma$-CVP），即找到一个长度不超过最短（或最近）向量长度 $\gamma$ 倍的向量。

## 格筛法基本原理

格筛法的核心思想是通过生成大量格向量，并利用格的加法（或减法）封闭性，迭代地构造出越来越短的向量，最终“筛选”出接近最短的向量。

### 核心思想：迭代缩减

想象一下，我们有一个包含许多格向量的列表 $S$。如果我们能找到列表中的两个向量 $\mathbf{v}_1, \mathbf{v}_2 \in S$，使得它们的差 $\mathbf{v}_1 - \mathbf{v}_2$ （或和 $\mathbf{v}_1 + \mathbf{v_2}$）比原来的向量更短，我们就可以用这个更短的向量来替换原来的向量（或将其加入列表）。由于格的性质，$\mathbf{v}_1 - \mathbf{v}_2$ 仍然是一个格向量。通过不断重复这个过程，我们期望列表中的向量会越来越短，最终收敛到最短（或接近最短）的向量。

这个过程的关键在于如何高效地找到这些“可缩减”的向量对。如果两个向量 $\mathbf{v}_1, \mathbf{v}_2$ 长度相近且夹角较小（小于 $60^\circ$ 或 $120^\circ$，取决于我们考虑差还是和），它们的差或和通常会更短。因此，筛法的本质可以看作是在高维空间中寻找“近邻”或“特定角度”的格向量对。

### AKS筛法的思想

最早的格筛法由 Ajtai, Kumar 和 Sivakumar (AKS) 于2001年提出。其基本思想是：

1. **采样:** 在一个以原点为中心的小球内随机采样大量点。
2. **扰动:** 对每个采样点进行微小扰动，并找到一个与之相关的格向量，使得扰动后的点与格向量的差保持为格向量。
3. **筛选:** 将这些扰动后的点分组（例如，使用哈希或几何划分），使得“靠近”的点分到一组。
4. **缩减:** 在同一组内，任意两个点对应的格向量之差，很可能是一个更短的格向量。通过不断迭代这个分组和相减的过程，可以逐步降低向量的长度。

AKS筛法证明了SVP可以在 $2^{O(n)}$ 的时间和空间内解决，但这更多是理论上的突破，其实际效率并不高。

### 现代筛法的两种思路

现代启发式筛法大致可以分为两类：

1. **AKS-like / NV Sieve:** 如Nguyen-Vidick (NV) 筛法，它遵循AKS的思路，从一个大的向量列表开始，在每一轮迭代中，通过两两组合产生一个全新的、更短的向量列表，并丢弃旧列表。这种方法比较“浪费”，因为它可能会丢弃一些已经找到的短向量。
2. **MV-like / GaussSieve:** 如Micciancio-Voulgaris (MV) 筛法（特别是GaussSieve），它从一个空列表开始，不断采样新的格向量，并尝试用列表中的向量去缩减新向量。一旦新向量无法再被缩减，就将其加入列表。更重要的是，它还允许新向量去缩减列表中的旧向量，使得列表中的向量可以持续被优化。这种方法更常用，因为它维护并不断优化一个包含当前已知最短向量的列表。

## 主流格筛法详解

### Nguyen-Vidick (NV) 筛法

NV筛法 (2008) 是AKS筛法的启发式版本，旨在提高实用性。

* **核心思想与步骤:**
  1. **初始化:** 生成一个包含大量（通常较长）格向量的列表 $S$。设定一个目标长度 $R$。
  2. **筛选:** 选择一个“筛因子” $\gamma < 1$。将 $S$ 中的向量分为两部分：长度小于 $\gamma R$ 的直接保留；长度大于 $\gamma R$ 的作为“中心点” $C$ 或尝试与 $C$ 中的向量相减。
  3. **缩减:** 对于 $S$ 中每个长度大于 $\gamma R$ 的向量 $\mathbf{v}$，寻找 $C$ 中是否存在一个中心点 $\mathbf{c}$ 使得 $\Vert\mathbf{v} - \mathbf{c}\Vert \le \gamma R$。如果存在，则将 $\mathbf{v} - \mathbf{c}$ 加入新列表；否则，将 $\mathbf{v}$ 加入 $C$。
  4. **迭代:** 用新生成的列表替换 $S$，并减小 $R$ ($R \leftarrow \gamma R$)，重复筛选和缩减步骤，直到 $R$ 足够小。
* **复杂度与变种:** 其启发式时间复杂度约为 $2^{0.415n}$，空间复杂度约为 $2^{0.2075n}$。一些变种（如两级筛法）试图优化性能，但其“丢弃旧列表”的特性使其在实践中不如MV筛法流行。

### Micciancio-Voulgaris (MV) 筛法 (GaussSieve / ListSieve)

MV筛法 (2010) 提出了两种重要的变体：ListSieve（可证明）和GaussSieve（启发式，更高效）。

* **核心思想与步骤 (GaussSieve):**
  1. **初始化:** 维护一个列表 $L$（初始为空或包含基向量）和一个栈 $S$。
  2. **采样:** 从格中采样一个新向量 $\mathbf{v}$（通常使用Klein采样器）。
  3. **缩减 $\mathbf{v}$:** 迭代地尝试用 $L$ 中的向量 $\mathbf{w}$ 去缩减 $\mathbf{v}$。如果找到一个 $\mathbf{w}$ 使得 $\Vert\mathbf{v} \pm \mathbf{w}\Vert < \Vert\mathbf{v}\Vert$，则用 $\mathbf{v} \pm \mathbf{w}$ 替换 $\mathbf{v}$ 并重新开始缩减过程。
  4. **缩减 $L$:** 用稳定后的 $\mathbf{v}$ 去尝试缩减 $L$ 中的所有向量。如果某个 $\mathbf{w} \in L$ 被缩减，则将其从 $L$ 中移除并压入栈 $S$。
  5. **加入 $L$:** 将稳定后的 $\mathbf{v}$ 加入 $L$。
  6. **处理栈:** 如果栈 $S$ 不为空，则弹出一个向量并将其作为新的 $\mathbf{v}$ 返回步骤3。
  7. **迭代:** 不断重复采样和缩减过程。
* **复杂度与改进:** GaussSieve的启发式时间复杂度约为 $2^{0.48n}$，空间复杂度约为 $2^{0.18n}$。其性能可以通过多种方式提升：
  * **局部敏感哈希 (LSH):** Laarhoven等人将LSH用于加速寻找可缩减向量对（近邻搜索），发展出HashSieve等算法，将时间复杂度降至 $2^{0.3366n}$ 左右。
  * **渐进式筛法 (Progressive Sieving):** Ducas等人提出的一种策略，从低维子格开始筛分，逐步增加维度，可以显著提高收敛速度和内存效率。
  * **理想格筛法 (IdealSieve):** 针对具有代数结构的理想格，利用旋转对称性，可以进一步提高效率。

### Becker-Ducas-Gama-Laarhoven (BDGL) 筛法 (LDSieve)

BDGL筛法 (2016)，又称LDSieve，是目前渐进复杂度最低的启发式筛法。

* **核心思想与步骤:** 它将寻找“近邻”格向量的问题转化为编码理论中的**高效列表译码问题**。
  1. **构造球面码:** 选择一个大小为 $M$ 的球面码 $F$（球面上的点集），这个码需要具备高效的列表译码能力。
  2. **分桶:** 对于列表 $L$ 中的每个（单位化）格向量 $\mathbf{v}$，找到 $F$ 中所有落在以 $\mathbf{v}$ 为中心的某个球冠内的码字 $f$。将 $\mathbf{v}$ 放入所有这些 $f$ 对应的“桶”中。
  3. **检查对:** 对于每个桶，检查桶内所有向量对，看它们是否构成“可缩减对”（夹角小于 $60^\circ$）。
     通过精心选择球面码 $F$ 的大小 $M$ 和球冠的大小，可以平衡计算量和找到所有可缩减对的概率。
* **复杂度与实际考量:** BDGL筛法的理想启发式时间和空间复杂度均为 $(3/2)^{n/2} \approx 2^{0.292n}$。然而，在实际实现中，通常使用**乘积码**来近似理想球面码，这会引入额外的计算、内存和概率开销。最近的研究表明，考虑内存访问模式（如流式访问）的BGJ筛法（BDGL的前身或近亲）可能在实际可达维度上比基于随机访问的BDGL更高效。

## 格筛法在密码分析中的应用

格筛法是现代格密码分析的核心工具之一，主要用于解决SVP问题，而SVP求解器是许多格攻击的关键组成部分。

* **在BKZ算法中的角色:** BKZ（Block-Korkine-Zolotarev）是一种强大的格基约化算法。它通过迭代地在低维投影子格上调用SVP求解器来逐步缩短格基向量。格筛法（特别是GaussSieve及其变种）常被用作BKZ中的SVP求解器，尤其是在高维或需要高质量规约时。
* **对NTRU的分析:** NTRU是一种基于多项式环上格的密码系统。对其进行攻击通常涉及在一个与公钥相关的格中寻找短向量。格筛法（集成在BKZ中）已被成功用于分析NTRU的安全性，并打破了一些NTRU挑战（如维度181的挑战）。
* **对LWE方案的分析:** 基于LWE（Learning With Errors）问题的密码方案，如NIST PQC标准中的CRYSTALS-Kyber（密钥封装）和CRYSTALS-Dilithium（数字签名），是当前的主流。对这些方案的攻击主要有**原始攻击 (Primal Attack)** 和**对偶攻击 (Dual Attack)**。这两种攻击最终都依赖于SVP求解器。格筛法的性能直接影响了这些攻击的估计成本，从而决定了Kyber和Dilithium等方案的安全级别。对筛法（如BDGL）成本的更精确估计（包括内存访问开销）已导致对这些方案的安全估计略有下调。
  * **原始攻击:** 通常需要在特定构造的格中找到一个与“错误”或秘密相关的短向量。
  * **对偶攻击:** 则需要在对偶格中找到短向量，用于区分LWE样本和随机样本。
* **对安全参数选择的影响:** 格筛法性能的不断提升和对其成本的更深入理解，迫使密码方案设计者选择更大的安全参数，以确保其方案能够抵抗已知的最佳攻击。筛法复杂度的估计是NIST PQC标准化过程中评估候选方案安全性的关键依据。

## 挑战、局限与未来展望

尽管格筛法取得了显著进展，但仍面临诸多挑战，同时也有广阔的研究前景。

### 主要挑战

1. **内存墙 (Memory Wall):** 最大的挑战是指数级的空间复杂度 ($2^{\Theta(n)}$)。存储和处理 $2^{\Theta(n)}$ 数量级的格向量需要巨大的内存，这严重限制了筛法在高维（例如，加密相关的几百到上千维）的应用。
2. **计算成本:** 即使时间复杂度是 $2^{cn}$ (其中 $c$ 相对较小)，对于高维格，总计算量仍然是天文数字。
3. **实际开销:** 像BDGL这样的渐进最优算法，在实际应用中可能因其复杂的结构（如乘积码译码）和随机内存访问模式而产生巨大的常数因子和实现开销，可能不如理论上稍差但实现更友好的算法（如BGJ或基于LSH的GaussSieve）。
4. **启发式性质:** 大多数高效的筛法都是启发式的，缺乏严格的性能保证。
5. **分布式实现:** 将筛法扩展到大规模并行计算集群上时，数据同步、通信带宽和负载均衡成为新的挑战。

### 量子筛法

理论上，量子计算机可以使用Grover算法或量子随机行走来加速筛法中的搜索过程，从而可能降低时间复杂度。然而，目前对量子筛法的详细资源估计表明，由于需要大量的量子比特（Qubits）、昂贵的量子随机访问内存（QRAM）以及巨大的量子纠错开销，对于当前密码学相关的维度，量子筛法似乎无法提供相对于经典筛法的实际优势。实现量子优势需要量子硬件和算法的重大突破。

### 未来研究方向

1. **内存优化:**
   * 研究**元组筛法 (Tuple Sieving)**，即一次组合超过两个向量来缩减。
   * 开发**流式筛法 (Streaming Sieves)**，优化内存访问模式，减少随机访问。
   * 探索**低精度筛法**，使用更少的比特表示向量坐标以减少内存和带宽。
   * 设计更高效的**分布式筛法**内存管理策略。
2. **算法融合与改进:**
   * **渐进式筛法**的进一步优化和应用。
   * 将筛法与**BKZ**、**枚举**等其他格算法更紧密地结合。
   * 发展新的**近邻搜索 (NNS)** 技术。
3. **硬件加速:**
   * 利用**GPU**进行并行计算，特别关注内存带宽问题。
   * 设计专用的**FPGA**或**ASIC**硬件来加速核心筛法操作。
4. **量子算法探索:**
   * 寻找更适合现有或近期量子硬件的量子格算法。
   * 降低量子筛法对QRAM的依赖。
5. **理论理解:**
   * 加深对筛法行为（如列表大小演化、碰撞概率）的理论理解。
   * 弥合启发式性能与可证明界限之间的差距。

## 总结

格筛法作为解决格上最短向量问题的最前沿技术之一，在格密码分析中扮演着不可或缺的角色。从AKS的理论突破，到NV、MV（特别是GaussSieve）的实用化，再到利用LSH和BDGL等技术追求极致渐进复杂度的努力，格筛法经历了长足的发展。它们不仅是评估NTRU、LWE等主流格密码方案安全性的标尺，也是推动格密码参数选择和方案演进的重要驱动力。

尽管面临着指数级内存消耗和高维计算成本等严峻挑战，但随着算法理论的创新、计算硬件的发展以及（或许长远的）量子计算的进步，格筛法及其相关技术仍将是格密码分析领域最活跃、最重要的研究方向之一。对格筛法的持续研究将有助于我们更准确地把握后量子密码的安全性边界，确保未来信息系统的安全。

## 参考资源（部分）

以下是本次调研过程中参考的部分网络资源和关键论文：

* [Lattice Sieving](https://en.wikipedia.org/wiki/Lattice_sieving)
* [Lattice-based cryptography](https://en.wikipedia.org/wiki/Lattice-based_cryptography)
* [Post-Quantum Cryptography: Lattice-Based Cryptography](https://pmc.ncbi.nlm.nih.gov/articles/PMC8433076/)
* [Progressive Lattice Sieving](https://www.researchgate.net/publication/324135046_Progressive_Lattice_Sieving)
* [Exploring the Foundations of Lattice-Based Cryptography](https://www.sectigo.com/resource-library/what-is-lattice-based-cryptography)
* [An Introduction to Lattices, Lattice Reduction, and Lattice-Based Cryptography](https://www.ias.edu/sites/default/files/PCMISlidesX1.pdf)
* [Sieving Algorithms for Lattice Problems](https://www.cs.uoregon.edu/Reports/UG-201606-Jagielski.pdf)
* [格上筛法研究现状与发展趋势 (Research Status and Development Trend of Lattice Sieving)](http://www.jcr.cacrnet.org.cn/CN/10.13868/j.cnki.jcr.000474)
* [Lattice Sieving and Combinatorial Algorithms](http://cseweb.ucsd.edu/~daniele/LatticeLinks/Sieve.html)
* [Efficient Implementations of Sieving and Enumeration Algorithms for Lattice-Based Cryptography](https://www.mdpi.com/2227-7390/9/14/1618)
* [The Complexity of the Shortest Vector Problem](https://eccc.weizmann.ac.il/report/2022/170/)
