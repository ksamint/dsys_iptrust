# 岁知社 Style Kit（可复用）

版本：2026-11-07。来源：品牌持有人本次提供的规范与参考素材。本版更新仓库默认视觉方向，取代此前藏青与铂灰的默认方案；历史版本仍可通过 Git 查询。品牌身份沿用 [IPTrust 品牌目录](https://apuch.art/brand?brand=iptrust)，本仓库的更新不会自动回写该网站/API。

## 品牌核心

- 品牌名：岁知社。
- 调性：真实、热爱、利他、有趣；第一梯队实战智慧；拒绝平庸；长期主义。
- 视觉目标：东方诗意克制 + 西方现代主义精确。

## 色彩系统

| 角色 | 色值 |
| --- | --- |
| 主金色 | `#8B7355` / `#8D723F` / `#99834E` |
| 背景米白 | `#F7F5F0` / `#FAF8F3` |
| 深炭灰 | `#2D2E30` / `#1A1A1A` |
| 留白纯白 | `#FFFFFF` |

复用默认值：金 `#8B7355`、背景 `#F7F5F0`、正文 `#2D2E30`。其余值作为同一系统中的替代色，按单件物料选择。正文优先使用深炭灰；金色用于图形、标志与重点。保留文字与底色的清晰对比。

## 字体风格

- 中文：雅致、克制、类书法或类宋体，字距宽松。
- 英文：优雅衬线体或干净现代无衬线，诗意分行。
- 长正文保持可读性，标题与正文分工清楚。Logo 使用原始图形，不用字体重排替代。
- 未指定唯一字体或授权字体文件；选择项目已有且有使用权的字体。token 中字体栈是技术回退建议，不是新增官方字体指定。

## 视觉语言

- 博物馆级极简，大量留白。
- 几何形态：圆、三角、水平线、拱门。
- 柔和渐变与锐利边缘并存。
- 手绘笔触点缀：有机、粗细变化。
- 东方诗意克制 + 西方现代主义精确。
- 单幅优先使用一至两个主要几何形态，围绕一个明确主题组织。文字、形态与笔触各有空间。

## Logo 素材

持有人给出的素材方向：抽象符号图标、竹墨笔触图标、金色笔触图标。原始 Logo 文件完整保存在 [logo-set](assets/brand-images/logo-set/)；参考图与正式 Logo 通过资产清单的 `usage` 区分。

Agent 和设计工具优先使用以下透明背景矢量：

| 版本 | 文件 | 使用建议 |
| --- | --- | --- |
| 深炭黑 | [suizhishe-black.svg](assets/logos/suizhishe-black.svg) | 米白、白色等浅底 |
| 金色 | [suizhishe-gold.svg](assets/logos/suizhishe-gold.svg) | 需要金色标志时，保持清晰对比 |
| 白色 | [suizhishe-white.svg](assets/logos/suizhishe-white.svg) | 深色背景 |

以上三款由已有黑色 SVG 的矢量路径导出，保持原始造型，去掉底板，分别采用 `#1A1A1A`、`#8B7355`、`#FFFFFF`。这三款是同一标志的色彩版本，并非三个独立图标设计。

原件注意事项：`logo-set/金色/logo_logo.svg` 没有可见图形，已归档但不供使用；`logo-set/蓝色/logo_logo.svg` 含内嵌 PNG，不属于纯矢量。使用上表可用文件。完整来源、文件状态与 SHA-256 见 [资产清单](../data/style-kit-assets.json)。

## 参考图

- [10 张风格参考与 10 张中英文海报](assets/style-kit/references/export/)：保留原始文件名及原始字节。
- [品牌包中的 1–6.png](assets/style-kit/references/brandkit/)：视觉及表达参考。
- [完整预览索引](assets/style-kit/REFERENCES.md)：逐图链接与预览。

参考图用于观察构图、色彩、笔触、文字节奏与留白；实际品牌署名使用独立 Logo 文件。

## 通用 Prompt 模板

以下为持有人提供的原文，将 `[ratio]` 替换为实际比例：

> A museum-quality 岁知社 brand visual in [ratio]. Pristine warm cream background (#F7F5F0). Minimalist composition with generous negative space. One or two refined geometric forms (circle, triangle, horizontal line, arch) in deep charcoal and golden-brown (#8B7355). Subtle hand-drawn brushstroke accent with organic varying thickness. Clean, contemplative, sophisticated. Influenced by Agnes Martin, Hiroshi Sugimoto, Song Dynasty ink painting. No clutter, no decorative noise. World-class poetic restraint.

生成后使用官方 Logo 文件完成品牌署名。中文文案按最终批准稿排版和校对；品牌价值“第一梯队实战智慧”属于品牌表达，不自动构成第三方排名或认证事实。

## Agent 使用入口

1. 读取本文件，再读取 [token](tokens/iptrust.tokens.json) 与 [资产清单](../data/style-kit-assets.json)。
2. 按用途选择 `usage: logo` 的独立 SVG 或 `usage: reference` 的参考图；`source-archive` 为原始归档。
3. 公共原始文件地址：`https://raw.githubusercontent.com/ksamint/dsys_iptrust/main/<仓库内路径>`。中文及空格路径按 URL 标准编码。
4. 保持 Logo 比例、路径与选定色彩；避免将风格参考中的几何形态当成新的正式 Logo。

机器入口：[agent.json](../agent.json)。固定版本复现时，将下载地址中的 `main` 替换为已验收 commit SHA。
