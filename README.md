# MengceZheng.github.io

[![GitHub Pages](https://img.shields.io/github/deployments/MengceZheng/MengceZheng.github.io/github-pages?label=Deploy+Status)](https://mengcezheng.github.io)
[![Scholar Sync](https://github.com/MengceZheng/MengceZheng.github.io/actions/workflows/google_scholar_crawler.yaml/badge.svg)](https://github.com/MengceZheng/MengceZheng.github.io/actions)
[![LICENSE](https://img.shields.io/badge/license-CC_BY--NC--SA_4.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Personal academic portal of **Mengce Zheng** - Research in Cryptography and Information Security.

## ✨ Core Features

- **Academic Resources**

  - Publications Archive
  - Preprints & Slides
  - Citation Metrics Auto-Sync
  - Technical Reports & Notes

- **Profile Links**
  - [![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=WgoBZnkAAAAJ)
  - [![DBLP](https://img.shields.io/badge/DBLP-005571?logo=dblp)](https://dblp.uni-trier.de/pid/169/8949.html)
  - [![ORCID](https://img.shields.io/badge/ORCID-A6CE39?logo=orcid)](https://orcid.org/0000-0003-0777-4175)
  - [![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?logo=researchgate)](https://www.researchgate.net/profile/Mengce-Zheng)

- **Key Publications**
  - [![IEEE Xplore](https://img.shields.io/badge/IEEE_Xplore-00629B?logo=ieee)](https://ieeexplore.ieee.org/author/37086429906)
  - [![Springer](https://img.shields.io/badge/Springer-303284?logo=springer)](https://link.springer.com/search?query=Mengce+Zheng)
  - [![Scopus](https://img.shields.io/badge/Scopus-green?logo=scopus)](https://www.scopus.com/authid/detail.uri?authorId=56948190500)
  - [![IACR-ePrint](https://img.shields.io/badge/ePrint-IACR-red?logo=iacr)](https://eprint.iacr.org/search?q=&title=&authors=Mengce+Zheng)
  - [![arXiv](https://img.shields.io/badge/arXiv-B31B1B?logo=arxiv)](https://arxiv.org/search/?query=Mengce+Zheng&searchtype=author&abstracts=show)

## 🔄 Citation Metrics 自动同步

引用数据由 GitHub Actions 工作流 [`.github/workflows/google_scholar_crawler.yaml`](.github/workflows/google_scholar_crawler.yaml) 每日错峰自动抓取，并推送到 `google-scholar-stats` 分支，供站点 badge 展示。

### 配置 `SERPAPI_KEY`（推荐）

GitHub Actions 的固定出口 IP 会被 Google Scholar 限流，因此爬虫默认通过 [SerpAPI](https://serpapi.com) 的 `google_scholar_author` 接口抓取，稳定且免费额度足够每日一次调度。

1. 在 [serpapi.com](https://serpapi.com) 注册，于 Dashboard 复制 API Key。
2. 在仓库 **Settings → Secrets and variables → Actions → New repository secret** 添加：
   - Name: `SERPAPI_KEY`
   - Value: 你的 SerpAPI Key
3. 触发方式：
   - 自动：每日 7–8 点随机分钟（`cron: '7,23,41,59 7-8 * * *'`）
   - 手动：Actions → `Get Citation Data` → `Run workflow`

未配置 `SERPAPI_KEY` 时会回退到 `scholarly` 直连（CI 上易失败），失败再回退上次缓存或兜底默认值，workflow 不会因此报错中断。

### 其他可选 Secrets

| Secret | 作用 |
| --- | --- |
| `GOOGLE_SCHOLAR_ID` | 作者 Scholar ID（默认可在 `main.py` 中硬编码或在此覆盖） |
| `GS_PROXY` | 自定义代理（如 `https://user:pass@host:port`），仅在 `SERPAPI_KEY` 缺失时用于 `scholarly` 直连 |

## 📜 License

- Content: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- Code: [MIT License](LICENSE)
