---
layout: post
title: "中国抗量子密码发展现状简述"
date: 2025-02-15
---
---

**作者**: [Mengce Zheng](https://mengcezheng.github.io/)

**日期**: 2025年2月15日

---

## 引言

随着量子计算技术的突破，传统密码算法的安全性面临严峻挑战，抗量子密码（Post-Quantum Cryptography, PQC）成为保障未来信息安全的战略重点。近年来，中国在PQC技术研究、迁移规划和产品应用方面取得了显著进展，为数字经济时代的信息安全提供了坚实保障。本报告将简要概述中国在这些领域的已有成果，基于公开信息和研究分析。

## 抗量子密码算法竞赛

中国在PQC算法开发上展现了积极的领导力。2018年，中国密码学会（CACR）组织了一场全国性竞赛，旨在选拔最有前途的量子抗性密码算法。该竞赛仅面向中国开发者，吸引了36份提案，经过一年的分析，评选出三个一等奖算法：Aigis-sig（基于CRYSTALS-DILITHIUM的数字签名）、Aigis-enc（基于CRYSTALS-KYBER的密钥封装）和LAC.PKE（基于格的密钥封装）。这些算法与国际标准如NIST的选择有一定一致性，显示了中国在全球PQC研究中的参与度。

更近的进展发生在2025年2月，商业密码标准研究所（ICCS）在中国密码标准化技术委员会的安排下，启动了一项全球倡议，征集下一代公钥密码算法（NGCC-PK）、密码哈希算法（NGCC-CH）和分组密码算法（NGCC-BC）的提案，旨在应对量子计算威胁。ICCS鼓励国际参与，算法将根据安全、性能和其他特性进行评估，最终入选者将被考虑标准化。公开意见征集期至2025年3月15日结束，目前标准化进程正在推进。

## 抗量子密码迁移规划

中国正在积极规划向PQC的迁移，以确保信息系统在量子时代的安全。2024年10月，中国专家在瑞典斯德哥尔摩举行的ISO/IEC JTC1/SC6（系统间远程通信和信息交换）会议上提交了一份量子安全电信安全协议的草案，并获得一致通过。该提案由中国Iwncomm（WAPI联盟成员）提出，旨在为全球通信网络向PQC迁移提供指导，特别关注“记录现在，解密以后”的攻击风险。提案中提到，中国于2022年12月成立了一个工作组，研究相关法律、政策和产业进展，促进国内共识。

虽然具体的迁移时间表尚未公开，但可以参考国际趋势。例如，美国国家安全局（NSA）呼吁在2035年前完成迁移，白宫制定了2025-2035年的战略，预计成本为71亿美元。中国作为全球领导者，可能会遵循类似的时间框架，但目前缺乏明确官方时间表。持续的标准化努力和国际合作表明，中国正在为结构化过渡做准备，与全球标准保持一致。

## 抗量子密码产品应用

中国企业开始探索将PQC集成到实际产品中，以增强信息安全。例如，华为在其信任中心页面中表示，计划在2024年前引入量子安全算法，确保长期安全。他们正在评估六类PQC算法，包括基于哈希、多变量、格、超奇异椭圆曲线、编码和杂项算法，并考虑三种实施选项：立即采用PQC、延迟至2024年标准化完成，或采用混合方案，将Diffie-Hellman与量子安全机制结合，用于TLS和IPsec等协议。然而，具体的产品应用案例尚未广泛公开。

其他公司如QuantumCTek，主要专注于量子密钥分发（QKD）和量子安全通信网络产品，而非PQC。2017年的行业报告曾提到，阿里巴巴曾发布量子密码通信产品，但更多是QKD相关，而非PQC。总体而言，中国PQC产品生态尚在发展中，具体应用案例有限，但国家竞赛和标准化倡议显示了一个日益壮大的技术生态系统，支持数字经济和国家安全。

## 小结

中国在PQC领域取得了显著进展，从2018年的CACR竞赛到2025年的ICCS全球倡议，显示了在算法研究和标准化方面的领导力。迁移规划通过国际合作和国内工作组推进，尽管时间表尚未明确。产品应用方面，华为等企业计划集成PQC，但具体案例有限。随着量子计算的推进，中国在PQC的投资和努力将为信息安全提供关键保障。

> 本文撰写过程中参考网络资源如下：[全国密码算法设计竞赛进入第二轮公钥算法](https://sfjs.cacrnet.org.cn/site/term/list_77_1.html)，[关于全国密码算法设计竞赛算法评选结果的公示](https://www.cacrnet.org.cn/site/content/854.html)，[关于开展新一代商用密码算法征集活动的公告](https://www.niccs.org.cn/tzgg/202502/t20250205_378196.html)，[中国将牵头制定抗量子攻击的通信网络安全协议设计指南](http://www.news.cn/20241028/5d10f8bc8f9241f6b5cd0fee2cbb8708/c.html)，[华为信任中心-后量子密码](https://www.huawei.com/cn/trust-center/post-quantum-cryptography)，[国盾量子](https://www.quantum-info.com/)等。
