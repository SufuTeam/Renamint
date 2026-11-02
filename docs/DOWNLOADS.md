# 官网自动下载

官网使用 GitHub 原生的最新地址，不需要每次发版后重新部署官网：

`https://github.com/SufuTeam/Renamint/releases/latest/download/Renamint-arm64.dmg`

发布新的正式版本前，完成 Developer ID 签名、Apple 公证、票据和安装验证。在 Release 草稿中上传 `Renamint-<版本>-arm64.dmg` 与包含该文件摘要的 `SHA256SUMS.txt`，公开并设为 Latest。

`Sync latest website download` 工作流在正式发布或修改发布时自动执行：核对安装包与校验文件，为同一份字节添加固定文件名 `Renamint-arm64.dmg` 及独立摘要，再更新 `download-manifest.json`。首页读取这个公开文件显示版本号；下载直接使用 GitHub 最新附件，不依赖访客的 GitHub API 配额，不会把本机未发布的开发包当成正式版。

工作流不构建 App，也不上传私有源码、签名材料或用户数据。它不会把草稿或预发布版本设为 Latest；会拒绝缺失、未完成或摘要不匹配的安装包。原始带版本号的安装包和 `SHA256SUMS.txt` 保留不变。新版进入 Latest 后，需要等工作流成功，固定下载附件才准备完成。

在 GitHub Actions 查看工作流是否成功。若缺少附件或校验失败，修复对应 Release 后手动运行 **Run workflow**。每次以当前 Latest 为准，重复运行不会覆盖不一致的附件；版本文件只在实际变化时提交。若今后启用 immutable releases，必须在公开前把固定文件名附件与摘要一并放入草稿，否则发布后不能补传。

网站版本信息可能受到 GitHub 静态文件短暂缓存影响；下载始终由 GitHub 的 Latest 指向决定。更改页面文案、截图或演示仍通过 Sites 正常发布。
