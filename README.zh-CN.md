<p align="center"><img src="assets/renamint.png" width="112" alt="Renamint App 图标"></p>
<h1 align="center">Renamint for Mac</h1>
<p align="center"><strong>相机 Wi-Fi 传输、本地 AI 命名，让素材井井有条。</strong></p>
<p align="center"><a href="https://renamint.com/">官网</a> · <a href="https://renamint.com/docs">使用文档</a> · <a href="https://renamint.com/cameras">设备兼容表</a> · <a href="README.md">English</a></p>

<!-- release-status:start -->
**Renamint · 最新正式版 · Apple 芯片 Mac · macOS 26 或更新版本**

[下载 DMG 安装包](https://github.com/SufuTeam/Renamint/releases/latest/download/Renamint-arm64.dmg) · [版本说明与校验值](https://github.com/SufuTeam/Renamint/releases/latest) · [所有版本](https://github.com/SufuTeam/Renamint/releases)

已完成 Developer ID 签名与 Apple 公证。内置 AI 模型另行下载，资源约 1.80 GB。
<!-- release-status:end -->

## 关于 Renamint

通过 Wi-Fi 把兼容相机里的照片和视频直接传到 Mac，再把默认文件名变成容易查找的名称。Renamint 将相机浏览、预览与下载、本地 AI、命名模板和文件工作区放在同一套流程里。

也可以直接导入 Mac 上的素材。用日期、内容标题、原名、已确认人物和序号组合命名规则；保留原位置，或整理到同一磁盘的目标文件夹。先预览、修改建议，再批量应用；在文件身份与原路径允许时撤销。

## 主要功能

- **相机 Wi-Fi 传输**：蓝牙发现与配对，Wi-Fi 浏览相册、预览支持的照片视频、选择下载原文件。素材不经云端中转。
- **下载接着整理**：完成的下载可导入命名工作区，不会在导入时直接启动 AI 分析。
- **传输控制**：选择保存目录、按日期分文件夹、查看数量与字节进度、重试未完成下载。续传取决于相机响应，同名文件受到保护。
- **本地 AI 命名**：内置模型在本机分析，也可连接自己的 Ollama、LM Studio 或兼容视觉 API；外部服务按授权发送数据并可能单独收费。
- **可复用模板**：组合日期、标题、原名、人物与序号，保留扩展名，在应用前检查冲突。
- **预览与撤销**：比较新旧名称、编辑建议，按文件或批次撤销，并检查文件身份和路径。
- **文件去重**：按完整内容识别相同照片视频，改过名字的副本也能找到。对比后选择保留，确认后移入废纸篓，每组至少保留一份。
- **版本更新**：在 App 中检查 GitHub 正式版本并查看更新日志；自动检查可以关闭，下载交给浏览器处理，安装由你完成。
- **文件夹监控 — Pro**：App 运行期间，让稳定的新增或修改素材进入工作区。
- **可信文件夹自动应用 — Pro**：验证模板与 AI 设置后逐个文件夹开启，原地改名，操作历史可查。

[阅读使用文档](https://renamint.com/docs) · [查看实用教程](https://renamint.com/blog)

## 设备兼容性

截至 **2026-10-31**。「已接入」表示有实现，不等于列表内每台设备都经过实机验证。固件与媒体格式会影响可用功能。

| 相机 | 状态 | 当前范围 |
| --- | --- | --- |
| DJI Osmo Action 6 | 已实机验证 | 已验证相册、照片/视频预览及 Wi-Fi 原片下载；已有完整批次传输记录。 |
| DJI Osmo Action 2 / 3 / 4 / 5 Pro | 已接入 · 待逐机验证 | 已接入 Osmo 协议与型号识别；不能把 Action 6 的实测结果推广到这些型号。 |
| DJI Osmo Pocket 3 / 4 / 4 Pro · Osmo Nano | 已接入 · 待逐机验证 | 无线素材接入路径已实现，各机型的目录、下载与预览仍待硬件验收。 |
| GoPro HERO9 / 10 / 11 / 12 / 13 Black · HERO11 Black Mini | 已接入 · 待实机验证 | 按 Open GoPro 实现配对、Wi-Fi 目录和原片下载；当前没有项目内 GoPro 实机验收记录。 |

### 预加机型与适配计划

以下机型**尚未作为可用功能发布，没有确定上线日期**。先评估相册与原片传输；全景播放、拼接和实时取景需要单独实现与验证。

| 预加机型 | 适配方向 |
| --- | --- |
| DJI Osmo 360 | 完善无线素材流程与逐机验证。已有识别入口，尚不算完整支持；原始全景处理另行评估。 |
| Insta360 X3 / X4 / X4 Air / X5 | 候选适配：优先评估无线相册和原片下载；尚未接入，原始全景拼接不包含在当前能力中。 |
| RICOH THETA X / Z1 | 候选适配：基于公开接口评估素材列表和下载，尚未接入。 |
| GoPro MAX 2 | 候选适配：单独核对机型与媒体格式；当前未启用，不承诺全景播放或拼接。 |
| DJI Mavic 3 · DJI Neo 2 | 预研候选：无线传输需要独立适配和硬件验证。当前版本不支持 DJI 无人机无线连接。 |

[完整兼容说明](https://renamint.com/cameras) · [Wi-Fi 传输教程](https://renamint.com/wifi-camera-transfer-mac)

## 免费版与 Pro

| 功能 | Free | Pro |
| --- | --- | --- |
| 兼容设备的相机 Wi-Fi 浏览与下载 | ✓ | ✓ |
| 手动命名、模板、预览与撤销 | ✓ | ✓ |
| AI 分析 | 每月 50 次 | 不限次 |
| 文件夹监控 | — | ✓ |
| 可信文件夹自动应用 | — | ✓ |
| 每份许可证同时激活 | — | 2 台 Mac |

**早鸟终身价 US$19.90，持续到 2026 年底。** 北京时间 **2027 年 1 月 1 日 00:00** 起，新订单恢复 **US$29.90**。一次购买，不是订阅；外部 AI 服务费用另计。

[价格与购买](https://renamint.com/pricing) · [找回激活码／管理设备](https://licenses.sufuapp.com/portal)

## 安装与开始使用

1. 下载 DMG，打开后将 Renamint 拖入 Applications。
2. 打开 App，选择本地规则或准备需要的 AI 分析方式；内置模型另行下载。
3. 添加 Mac 上的照片视频，或进入「相机导入」连接兼容相机。
4. 选择模板、检查建议，再确认应用。
5. 已购买 Pro 时，在「设置 → 许可证」输入邮件中的激活码。

连接相机会暂时切换到相机热点，上网连接可能中断；正常断开时尝试恢复原网络。传输与文件夹监控期间需要保持 App 运行。

## 更新 Renamint

下载最新 DMG，退出 Renamint，将新版拖入 Applications 替换原 App。现有素材库、模板、偏好与许可证保留。1.12.0 及以后版本可以从「设置 → 版本信息」或 App 菜单检查更新；更早版本请使用上方下载链接手动更新。

## 系统、格式与隐私

- **Apple 芯片 Mac、macOS 26 或更新版本**；目前没有 Intel 安装包。
- 支持 JPG、PNG、HEIC、MP4、MOV 等素材；RAW 取决于 macOS 解码，部分视频可使用可选 FFmpeg 工具。不处理 Office 文档。
- 视频分析采样 **1–8 帧**，不逐帧观看，也不转写音频。
- 可以下载原片，不等于能播放或拼接原始全景格式。
- 相机传输与内置 AI 在本地处理；远程 AI 的数据发送取决于服务设置与授权。
- Pro 首次激活需要联网；离线签名凭据有效 30 天，联网验证后续期。

[隐私说明](https://renamint.com/privacy) · [激活与换机指南](https://renamint.com/license-and-new-mac)

## 反馈与帮助

在 App 的「帮助 → 反馈与建议」或「设置 → 支持与诊断」填写问题。App 会打开 GitHub 草稿，由你检查后发布；也可直接[报告问题或提出建议](https://github.com/SufuTeam/Renamint/issues/new/choose)。

请提供 App 与 macOS 版本、复现步骤；传输问题请补充相机型号和固件。提交前检查截图，不要公开激活码、API 密钥、私人素材或个人路径。未收到激活邮件时，使用结账邮箱登录许可证门户，不要在公开 Issue 中发送订单隐私。

## 关于此仓库

此仓库用于官方安装包分发和反馈，不包含专有 App 源码。第三方许可随 App 附带；修改后的 AGPL Keygate 后台完整对应源码见 [licensing](licensing/)。

© 2026 Sufu. Renamint。相机商标属于各自权利人，本项目不是相机品牌的官方应用。
