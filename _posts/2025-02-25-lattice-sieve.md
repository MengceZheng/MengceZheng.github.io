---
layout: post
title: "格密码分析之格筛法简要概述"
date: 2025-02-25
---

## 引言

格密码分析利用格理论中困难问题（如最短向量问题SVP和最近向量问题CVP）的求解方法攻击密码方案，格筛法（lattice sieving）作为高效工具，在解决SVP方面表现突出。本文从起源、发展、顶峰、理论基础、实践实现和未来方向等六个方面，简要调研格筛法在密码分析中的应用。

## 历史发展

在2001年之前，格问题主要通过格基约化技术如Lenstra-Lenstra-Lovász算法（LLL算法）解决，专注于寻找已约化格基而非直接解决SVP。Ajtai在1996年引入基于格的加密构造，展示了平均情况下如短整数解（SIS）问题的困难程度，但具体筛法尚未突出。Kannan于1983年提出求解SVP的算法，达到$2^{O(n \log n)}$的时间复杂度，奠定了后来的改进基础。然而，随机化筛法直到2001年才由Ajtai等人正式提出。

2001年，Ajtai、Kumar和Sivakumar在第33届ACM理论计算研讨会（STOC）发表“用于最短格向量问题的筛法”（[A sieve algorithm for the shortest lattice vector problem](https://dl.acm.org/doi/abs/10.1145/380752.380857)）。该论文提出随机化筛法，时间复杂度为$2^{O(n)}$，改进了Kannan的$2^{O(n \log n)}$，通过采样短向量并迭代组合减少长度，实现了SVP求解的多项式时间近似。这项工作奠定了格筛法的基础。

2008年，Nguyen和Vidick的论文“最短向量问题的筛法是实用的”（[Sieve algorithms for the shortest vector problem are practical](https://www.degruyter.com/document/doi/10.1515/JMC.2008.009/html)）推动了格筛法的发展。他们评估了Ajtai等人提出的AKS算法的实用性，同时提出启发式变体，使格筛法能找到高达50维格中的格向量，挑战了之前认为不实用的观点。这一时期还出现了GaussSieve（[Faster exponential time algorithms for the shortest vector problem](https://epubs.siam.org/doi/abs/10.1137/1.9781611973075.119)）和HashSieve（[Sieving for shortest vectors in lattices using angular locality-sensitive hashing](https://link.springer.com/chapter/10.1007/978-3-662-47989-6_1)）。GaussSieve使用基于列表的方法，通过向量相互约化找到短向量；HashSieve利用局部敏感哈希（locality-sensitive hashing）提高效率。此后，更多论文进一步增强了筛法。例如，Mariano等人引入并行无锁HashSieve（[Parallel (probable) lock-free HashSieve: a practical sieving algorithm for the SVP](https://eprint.iacr.org/2015/041.pdf)），改善了实际性能。Ishiguro等人使用并行GaussSieve解决了128维SVP挑战（[Parallel Gauss sieve algorithm: solving the SVP challenge over a 128-dimensional ideal lattice](https://link.springer.com/chapter/10.1007/978-3-642-54631-0_24)），展示了可扩展性。

2016年，Becker、Ducas、Gama和Laarhoven的论文“最近邻搜索的新方向及其在格筛中的应用”（[New directions in nearest neighbor searching with applications to lattice sieving](https://epubs.siam.org/doi/abs/10.1137/1.9781611974331.ch2)）标志着格筛法的又一个顶峰，发表在第27届ACM-SIAM离散算法年会（SODA）。他们引入局部敏感过滤器（locality-sensitive filters），针对球面上的近邻搜索问题，显著提高了筛算法效率。论文显示：SVP求解算法的启发式时间复杂度从之前的$2^{0.298n + o(n)}$降低到$2^{0.292n + o(n)}$，在高维中表现出色。GaussSieve实验验证了这一加速，显示实际运行时间减少，证明了方法的实用性。之后，Laarhoven探索了进化技术在格筛中的应用（[Evolutionary techniques in lattice sieving algorithms](https://arxiv.org/abs/1907.04629)），将格筛与进化算法（如遗传算法）类比，提出可能的新优化策略，扩展了筛法的理论框架。

## 理论基础

格筛法的理论基础在于通过启发式近似处理高维空间。其核心思想是维护一个短向量列表，通过组合对或元组迭代减少其范数，利用欧几里得空间的三角不等式。时间复杂度通常为$2^{c \cdot n + o(n)}$，其中$c$是随时间改进的常数（如Ajtai等人的$0.415$到Becker等人的$0.292$）。启发式假设如格点均匀分布和约化独立性在随机格中是经验上有效的，但缺乏严格证明。例如，GaussSieve假设列表中向量的线性独立性，HashSieve使用角度局部敏感哈希高效查找近邻。这些启发式使实际实现成为可能，但相比枚举法，可证明性保证有限。

## 实践实现

格筛法的实践实现主要集中在优化GaussSieve、HashSieve及其变体，用于现实世界的密码分析。GaussSieve由Micciancio和Voulgaris提出，使用基于列表的方法，通过向量相互约化找到短向量。Yang等人在GPU上实现并行化，线性加速，解决了130维SVP挑战（[Gauss sieve algorithm on GPUs](https://link.springer.com/chapter/10.1007/978-3-319-52153-4_3)）。HashSieve由Laarhoven提出，替换暴力搜索为角度局部敏感哈希，保持内存为$2^{0.207n}$，时间复杂度降低。Mariano等人开发并行无锁HashSieve，增强多核系统可扩展性。这些实现对攻击基于格的密码方案或困难问题如NTRU和LWE至关重要，实证结果显示均优于理论界限。

## 未来方向

未来，格筛法可能受益于量子计算，如Chailloux和Loyer提出量子随机游走，时间复杂度降至$2^{0.2570n + o(n)}$（[Lattice sieving via quantum random walks](https://arxiv.org/abs/2105.05608)）。内存效率仍是挑战，Laarhoven探索元组式筛法减少空间复杂度（[Faster tuple lattice sieving using spherical locality-sensitive filters](https://arxiv.org/abs/1705.02828)），但高维可扩展性存争议。Albrecht和Rowell提出多机器扩展的格筛法（[Scaling lattice sieves across multiple machines](https://eprint.iacr.org/2024/747)），但算法实现需要指数级内存。此外，开放问题包括弥合可证明与启发式复杂度之间的差距，扩展到非欧几里得范数等。

> 本文撰写过程中借助AI技术。
