---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "<https://cdn.jsdelivr.net/gh/>" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "<https://raw.githubusercontent.com/>" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

## 👨‍💼 About Me

I am currently an Associate Professor at [Zhejiang Wanli University (ZWU)](https://www.zwu.edu.cn/) and work as the head of the Cyber Security major.
Before joining ZWU, I worked as a postdoctoral researcher at [School of Information Science and Technology](https://sist.ustc.edu.cn/main.htm) of [University of Science and Technology of China (USTC)](https://www.ustc.edu.cn/) from 2018.12 to 2020.12 under collaboration with Prof. [Nenghai Yu (俞能海)](https://faculty.ustc.edu.cn/yunenghai/zh_CN/index.htm) and Prof. [Honggang Hu (胡红钢)](https://faculty.ustc.edu.cn/huhonggang/zh_CN/index.htm).

From 2009.09 to 2018.11, I studied at USTC, where I received my bachelor's degree in 2013 and the doctoral degree in 2018, advised by Prof. Honggang Hu.
I conducted academic visits at [The University of Tokyo (UTokyo)](https://www.u-tokyo.ac.jp/en/) from 2016.10 to 2017.09 under collaboration with Prof. [Noboru Kunihiro](https://www.crisec.cs.tsukuba.ac.jp/kunihiro/english/). I conducted academic visits at [University of Caen Normandy (UniCaen)](https://www.unicaen.fr/) from 2024.11 to 2025.10 under collaboration with Prof. [Abderrahmane Nitaj](https://nitaj.users.lmno.cnrs.fr/).

My main research interests include cryptographic algorithms and their applications, including public-key cryptanalysis, side-channel analysis, quantum cryptographic protocols, etc.
I have published more than 30 papers [![Google Scholar Citations](https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FMengceZheng%2FMengceZheng.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations)](https://scholar.google.com/citations?user=WgoBZnkAAAAJ), in related journals and conferences such as SCIENCE CHINA Information Sciences, Theoretical Computer Science, Journal of Information Security and Applications, CHES, ACISP, etc.

Further information on my experience and work can be found in my attached [**CV**](/docs/CV.pdf).
If you are interested in similar research and seeking any form of academic cooperation, please feel free to email me at [mengce.zheng@gmail.com](mailto:mengce.zheng@gmail.com).

## 🔥 News

- *2025.09*: One paper entitled "New Lattice-Based Partial Key Exposure Attacks on Common Prime RSA" was accepted by *Journal of Cryptographic Engineering*.
- *2025.05*: Two papers entitled "A New Generalized Attack on RSA-like Cryptosystems" and "A Novel Partial Key Exposure Attack on Common Prime RSA" were accepted by *AFRICACRYPT 2025*.
- *2025.04*: One paper entitled "Improving RSA Cryptanalysis: Combining Continued Fractions and Coppersmith's Techniques" was accepted by *ACISP 2025*.
- *2025.01*: One paper entitled "MulLeak: Exploiting Multiply Instruction Leakage to Attack the Stack-optimized Kyber Implementation on Cortex-M4" was accepted by *CHES 2025*.🎉
- *2024.11*: One paper entitled "Generalized Cryptanalysis of Cubic Pell RSA" was accepted by *Inscrypt 2024*.
- *2024.11*: I have come to France to visit the University of Caen Normandy and work with Prof. Nitaj. 🏰

## 🧰 Projects

- Lattice-Based Cryptanalysis: It employs lattice structures to analyze cryptographic systems. The celebrated Coppersmith's method utilizes lattice reduction to find small roots of polynomial equations modulo an integer. This technique can compromise RSA cryptosystem, especially with short exponents or partial key exposure, by efficiently recovering messages or factorizing the RSA modulus. This highlights the need for careful parameter selection in cryptographic protocols to prevent such vulnerabilities.

- Post-Quantum Cryptography: It develops cryptographic methods secure against quantum computer attacks. Lattice-based cryptography, a key area within this field, relies on mathematical structures called lattices. Its security is based on the difficulty of solving certain lattice problems, making it resistant to both classical and quantum attacks. This approach is efficient, scalable, and forms the basis for various cryptographic protocols, including key exchanges and digital signatures.

- Quantum Network Protocols: It uses quantum mechanics to create secure communication channels. A key component is quantum key distribution (QKD), which allows two parties to generate a shared secret key for encrypting messages. QKD detects eavesdropping attempts due to quantum properties, offering security beyond classical methods. This is crucial in post-quantum cryptography, as it also protects information against future quantum computer threats.

- Side-Channel Analysis: It extracts sensitive information from cryptographic systems by monitoring unintended emissions like power consumption or timing variations. Machine learning (ML) and deep learning (DL) have recently enhanced such attacks by automatically identifying complex patterns in side-channel data, enabling more accurate and efficient recovery of secret keys. This advancement underscores the need for robust countermeasures in the cryptographic implementations.

## 📝 Publications

### 📃 Journal Articles

- Fan Huang, Xiaolin Duan, Chengcong Hu, **Mengce Zheng**, Honggang Hu. MulLeak: Exploiting Multiply Instruction Leakage to Attack the Stack-optimized Kyber Implementation on Cortex-M4. *IACR Transactions on Cryptographic Hardware and Embedded Systems* 2025(2), 23--68 (2025). \| \[[HTML](https://tches.iacr.org/index.php/TCHES/article/view/12041) [PDF](/docs/HDH+25.pdf)\]
- **Mengce Zheng**, Hao Kang. Lattice-based cryptanalysis of RSA-type cryptosystems: a bibliometric analysis. *Cybersecurity* 7: 74 (2024). \| \[[HTML](https://link.springer.com/article/10.1186/s42400-024-00289-7) [PDF](/docs/ZK24.pdf)\]
- **Mengce Zheng**. Revisiting RSA-polynomial problem and semiprime factorization. *Theoretical Computer Science* 1004: 114634 (2024). \| \[[HTML](https://www.sciencedirect.com/science/article/pii/S0304397524002494) [PDF](/docs/Zheng24b.pdf) [Code](https://github.com/MengceZheng/RSAPoly)\]
- **Mengce Zheng**. Revisiting Small Private Key Attacks on Common Prime RSA. *IEEE Access* 12: 5203--5211 (2024). \| \[[HTML](https://ieeexplore.ieee.org/document/10380560) [PDF](/docs/Zheng24a.pdf) [Code](https://github.com/MengceZheng/SPKA_CPRSA)\]
- **Mengce Zheng**. Generalized implicit-key attacks on RSA. *Journal of Information Security and Applications* 77: 103562 (2023). \| \[[HTML](https://www.sciencedirect.com/science/article/pii/S2214212623001461) [PDF](/docs/Zheng23.pdf)\]
- **Mengce Zheng**, Zhigang Chen, Yaohui Wu. Solving Generalized Bivariate Integer Equations and Its Application to Factoring With Known Bits. *IEEE Access* 11: 34674--34684 (2023). \| \[[HTML](https://ieeexplore.ieee.org/document/10092793) [PDF](/docs/ZCW23.pdf)\]
- **Mengce Zheng**. Revisiting the Polynomial-Time Equivalence of Computing the CRT-RSA Secret Key and Factoring. *Mathematics* 10(13): 2238 (2022). \| \[[HTML](https://www.mdpi.com/2227-7390/10/13/2238) [PDF](/docs/Zheng22.pdf)\]
- **Mengce Zheng**, Noboru Kunihiro, Yuanzhi Yao. Cryptanalysis of the RSA variant based on cubic Pell equation. *Theoretical Computer Science* 889: 135--144 (2021). \| \[[HTML](https://www.sciencedirect.com/science/article/abs/pii/S030439752100445X) [PDF](/docs/ZKY21.pdf) [Code](https://github.com/MengceZheng/cPRSA)\]
- **Mengce Zheng**, Kaiping Xue, Shangbin Li, Nenghai Yu. A practical quantum designated verifier signature scheme for E-voting applications. *Quantum Information Processing* 20(7): 1--22 (2021). \| \[[HTML](https://link.springer.com/article/10.1007/s11128-021-03162-5) [PDF](/docs/ZXLY21.pdf)\]
- Zhigang Chen, Gang Hu, **Mengce Zheng**, Xinxia Song, Liqun Chen. Bibliometrics of Machine Learning Research Using Homomorphic Encryption. *Mathematics* 9(21): 2792 (2021). \| \[[HTML](https://www.mdpi.com/2227-7390/9/21/2792) [PDF](/docs/CHZ+21.pdf)\]
- Qidong Jia, Kaiping Xue, Zhonghui Li, **Mengce Zheng**, David S. L. Wei, Nenghai Yu. An improved QKD protocol without public announcement basis using periodically derived basis. *Quantum Information Processing* 20(2): 69 (2021). \| \[[HTML](https://link.springer.com/article/10.1007/s11128-021-03000-8) [PDF](/docs/JXL+21.pdf)\]
- **Mengce Zheng**, Noboru Kunihiro, Honggang Hu. Lattice-based cryptanalysis of RSA with implicitly related keys. *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences* 103(8): 959--968 (2020). \| \[[HTML](https://search.ieice.org/bin/summary.php?id=e103-a_8_959) [PDF](/docs/ZKH20.pdf)\]
- Jiajia Zhang, **Mengce Zheng**, Jiehui Nan, Honggang Hu, Nenghai Yu. A Novel Evaluation Metric for Deep Learning-Based Side Channel Analysis and Its Extended Application to Imbalanced Data. *IACR Transactions on Cryptographic Hardware and Embedded Systems* 2020(3): 73--96 (2020). \| \[[HTML](https://tches.iacr.org/index.php/TCHES/article/view/8583) [PDF](/docs/ZZN+20.pdf)\]
- **Mengce Zheng**, Honggang Hu, Zilong Wang. Generalized cryptanalysis of RSA with small public exponent. *SCIENCE CHINA Information Sciences* 59(3): 32108:1--32108:10 (2016). \| \[[HTML](https://link.springer.com/article/10.1007/s11432-015-5325-7) [PDF](/docs/ZHW16.pdf) [Code](https://github.com/MengceZheng/GRSA)\]
- **Mengce Zheng**, Honggang Hu. Cryptanalysis of Prime Power RSA with two private exponents. *SCIENCE CHINA Information Sciences* 58(11): 1--8 (2015). \| \[[HTML](https://link.springer.com/article/10.1007/s11432-015-5409-4) [PDF](/docs/ZH15.pdf) [Code](https://github.com/MengceZheng/PPRSA)\]

### 📖 Conference Proceedings

- Michel Seck, Oumar Niang, Djiby Sow, Abderrahmane Nitaj, **Mengce Zheng**, Maher Boudabra. A New Generalized Attack on RSA-like Cryptosystems. In: *AFRICACRYPT* 2025. \| \[[ePrint](https://eprint.iacr.org/2025/380)\]
- **Mengce Zheng**, Abderrahmane Nitaj. A Novel Partial Key Exposure Attack on Common Prime RSA. In: *AFRICACRYPT* 2025. \| \[[ePrint](https://eprint.iacr.org/2025/1282) [Code](https://github.com/MengceZheng/CPRSA_PKEA)\]
- **Mengce Zheng**, Yansong Feng, Abderrahmane Nitaj, Yanbin Pan. Improving RSA Cryptanalysis: Combining Continued Fractions and Coppersmith's Techniques. In: *ACISP* 2025. \| \[[ePrint](https://eprint.iacr.org/2025/1281) [Code](https://github.com/MengceZheng/RSA_CFL)\]
- Hao Kang, **Mengce Zheng**. Generalized Cryptanalysis of Cubic Pell RSA. In: *Inscrypt* 2024. \| \[[ePrint](https://eprint.iacr.org/2024/2081) [Code](https://github.com/MengceZheng/GCPRSA)\]
- **Mengce Zheng**, Wei Yan. Improved Lattice-Based Attack on Mersenne Low Hamming Ratio Search Problem. In: *ACISP* 2024. \| \[[ePrint](https://eprint.iacr.org/2024/2080) [Code](https://github.com/MengceZheng/MLHRSP)\]
- **Mengce Zheng**. Partial Key Exposure Attack on Common Prime RSA. In: *Inscrypt* 2023. \| \[[ePrint](https://eprint.iacr.org/2024/061) [Code](https://github.com/MengceZheng/PKEA_CPRSA)\]
- Shukun An, Jianzhao Liu, Xiaolin Duan, **Mengce Zheng**, Honggang Hu. Strengthening Profiled Side Channel Attacks on AES via Multi-view Information Aggregation. In: *CIS* 2021.
- Yukun Cheng, **Mengce Zheng**, Fan Huang, Jiajia Zhang, Honggang Hu, Nenghai Yu. A Fast-Detection and Fault-Correction Algorithm against Persistent Fault Attack. In: *TrustCom* 2021. \| \[[arXiv](https://arxiv.org/abs/2106.07943)\]
- Zhimin Luo, **Mengce Zheng**, Ping Wang, Minhui Jin, Jiajia Zhang, Honggang Hu. Towards Strengthening Deep Learning-based Side Channel Attacks with Mixup. In: *TrustCom* 2021. \| \[[arXiv](https://arxiv.org/abs/2103.05833) [ePrint](https://eprint.iacr.org/2021/312)\]
- Wenlong Cao, Fan Huang, **Mengce Zheng**, Honggang Hu. Attacking FPGA-based Dual Complementary AES Implementation Using HD and SD Models. In: *CIS* 2020.
- Minhui Jin, **Mengce Zheng**, Honggang Hu, Nenghai Yu. An Enhanced Convolutional Neural Network in Side-Channel Attacks and Visualization. In: *WCSE* 2020. \| \[[arXiv](https://arxiv.org/abs/2009.08898)\]
- **Mengce Zheng**, Honggang Hu. Implicit Related-Key Factorization Problem on the RSA Cryptosystem. In: *CANS* 2019. \| \[[PDF](/docs/ZH19b.pdf)\]
- **Mengce Zheng**, Honggang Hu. Implicit-Key Attack on the RSA Cryptosystem. In: *SciSec* 2019. \| \[[PDF](/docs/ZH19a.pdf)\]
- Jiehui Nan, **Mengce Zheng**, Honggang Hu. Post-Quantum Pseudorandom Functions from Mersenne Primes. In: *FCS* 2019.
- Zilong Wang, Honggang Hu, **Mengce Zheng**, Jiehui Nan. Symmetric Lattice-Based PAKE from Approximate Smooth Projective Hash Function and Reconciliation Mechanism. In: *FCS* 2019.
- **Mengce Zheng**, Noboru Kunihiro, Honggang Hu. Cryptanalysis of RSA Variants with Modified Euler Quotient. In: *AFRICACRYPT* 2018. \| \[[PDF](/docs/ZKH18.pdf) [Code](https://github.com/MengceZheng/MEQRSA)\]
- **Mengce Zheng**, Noboru Kunihiro, Honggang Hu. Improved Factoring Attacks on Multi-prime RSA with Small Prime Difference. In: *ACISP* 2017. \| \[[ePrint](https://eprint.iacr.org/2015/1137) [PDF](/docs/ZKH17.pdf) [Code](https://github.com/MengceZheng/MPRSA)\]

## 💬 Presentations

- A Novel Partial Key Exposure Attack on Common Prime RSA, The 16th International Conference on the Theory and Applications of Security and Cryptography, Rabat, Morocco, 2025. \| \[[Slides](/docs/AFRICACRYPT25.pdf)\]
- Improving RSA Cryptanalysis: Combining Continued Fractions and Coppersmith's Techniques, The 30th Australasian Conference on Information Security and Privacy, Wollongong, Australia, 2025. \| \[[Slides](/docs/ACISP25.pdf)\]
- Lattice-Based Solving Strategy Using Coppersmith's Techniques and Its Applications, Crypto Seminar at the University of Caen Normandie, Caen, France, 2025. \| \[[Slides](/docs/UCaen25.pdf)\]
- Generalized Cryptanalysis of Cubic Pell RSA, The 20th International Conference on Information Security and Cryptology, Kunming, China, 2024. \| \[[Slides](/docs/INSCRYPT24.pdf)\]
- Improved Lattice-Based Attack on Mersenne Low Hamming Ratio Search Problem, The 29th Australasian Conference on Information Security and Privacy, Sydney, Australia, 2024. \| \[[Slides](/docs/ACISP24.pdf)\]
- Lattice-Based Cryptanalysis of RSA with Implicitly Related Keys (Chinese Version), Academic Seminar at Nanjing University of Posts and Telecommunications, Online, China, 2020. \| \[[Slides](/docs/NJUPT20.pdf)\]
- Implicit Related-Key Factorization Problem on the RSA Cryptosystem, The 18th International Conference on Cryptology and Network Security, Fuzhou, China, 2019. \| \[[Slides](/docs/CANS19.pdf)\]
- Implicit-Key Attack on the RSA Cryptosystem, The 2nd International Conference on Science of Cyber Security, Nanjing, China, 2019. \| \[[Slides](/docs/SciSec19.pdf)\]
- Cryptanalysis of RSA Variants with Modified Euler Quotient, The 10th International Conference on the Theory and Applications of Security and Cryptography, Marrakesh, Morocco, 2018. \| \[[Slides](/docs/AFRICACRYPT18.pdf)\]
- Improved Factoring Attacks on Multi-prime RSA with Small Prime Difference, The 22nd Australasian Conference on Information Security and Privacy, Auckland, New Zealand, 2017. \| \[[Slides](/docs/ACISP17.pdf)\]

## 📘 Notes

{% assign current_year = site.time | date: "%Y" %}
{% assign posts_by_year = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
  {% if year.name == current_year %}

🕛 {{ year.name }}

{% for post in year.items %}

- [{{ post.title }}]({{ post.url }})

{% endfor %}
  {% else %}

<!-- markdownlint-disable MD033 -->

<details markdown="1">
<summary>{{ year.name }}</summary>

{% for post in year.items %}

- [{{ post.title }}]({{ post.url }})

{% endfor %}
</details>

<!-- markdownlint-enable MD033 -->

  {% endif %}
{% endfor %}

## 🏆 Honors and Awards

- *2023*: CSC Local Cooperation Program for Visiting Scholar
- *2023*: Ningbo Youth Science and Technology Innovation Leading Talent Program  
- *2022*: Zhejiang Province University Leading Talent Training Program -- Young Talents
- *2021*: Ningbo Leading Talent Training Project -- The Third Level  
- *2016*: CSC Scholarship for Joint Doctoral Students
- *2015*: National Scholarship for Graduate Students

## 🎓 Educations and Visitings

- *2024 -- 2025*: Visiting Sholar, University of Caen, Caen, France
- *2013 -- 2018*: PH.D. & M.S., University of Science and Technology of China, Hefei, China
- *2016 -- 2017*: Visiting PH.D., The University of Tokyo, Tokyo, Japan
- *2009 -- 2013*: B.E., University of Science and Technology of China, Hefei, China

## 👨‍🏫 Teaching

- *Cryptography Theory and Technology*:  2024 Spring
- *Advanced Cryptography*:  2023 Spring, 2024 Spring, 2024 Fall
- *Blockchain Theory and Technology*:  2023 Spring, 2023 Fall
- *Cybersecurity Theory and Technology*:  2021 Spring, 2022 Spring
- *Data Structures and Algorithms*:  2021 Fall, 2022 Fall
