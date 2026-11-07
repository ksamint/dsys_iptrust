# 岁知社 Style Kit（可复用）

真实、热爱、利他、有趣；第一梯队实战智慧；拒绝平庸；长期主义。

**东方诗意克制 + 西方现代主义精确。** 金色、米白、深炭灰，大量留白；几何形态与有机笔触相映。

- [完整 Style Kit 与通用 Prompt](IPTRUST/IPTrust_DESIGN.md)
- [参考图预览索引](IPTRUST/assets/style-kit/REFERENCES.md) · [原始 Logo 素材](IPTRUST/assets/brand-images/logo-set/)
- 独立 SVG：[深炭黑](IPTRUST/assets/logos/suizhishe-black.svg) · [金色](IPTRUST/assets/logos/suizhishe-gold.svg) · [白色](IPTRUST/assets/logos/suizhishe-white.svg)
- [设计 token](IPTRUST/tokens/iptrust.tokens.json) · [默认主题](data/theme.json)
- [资产清单 / SHA-256](data/style-kit-assets.json) · [Agent 入口](agent.json)

## 来源与版本

2026-11-07 按品牌持有人提供的 Style Kit、26 张参考图及 Logo 文件更新。参考图与原始文件保留原始字节；3 款可用 SVG 从现有矢量路径导出，来源与变更见资产清单。

本版取代仓库此前藏青与铂灰的默认方案。目录中的品牌身份对应 [岁知社 IPTrust](https://apuch.art/brand?brand=iptrust)，仓库地址保持 `ksamint/dsys_iptrust`。本次更新发布在该 GitHub 仓库；网站/API 不会自动同步。

历史目录快照见 [data/source.json](data/source.json)；初始导入与旧版规范保留在 Git 历史中。原始金色 SVG 为空、蓝色 SVG 内嵌位图，已保留并在清单中标注；使用上面的独立 SVG。

## Agent 快速使用

读取 `agent.json` 指向的指南、token 与资产清单。选择 `usage: logo` 的可用文件作品牌署名，选择 `usage: reference` 的文件作视觉参考。原始文件公开下载地址：

```text
https://raw.githubusercontent.com/ksamint/dsys_iptrust/main/<仓库内路径>
```

本地校验：`python3 scripts/validate-style-kit.py`。
