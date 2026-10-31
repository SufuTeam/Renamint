<p align="center"><img src="assets/renamint.png" width="112" alt="Renamint app icon"></p>
<h1 align="center">Renamint for Mac</h1>
<p align="center"><strong>Camera Wi-Fi transfers. Local AI naming. Your media, in order.</strong></p>
<p align="center"><a href="https://renamint.com/en/">Website</a> · <a href="https://renamint.com/en/docs">Guide</a> · <a href="https://renamint.com/en/cameras">Camera compatibility</a> · <a href="README.zh-CN.md">简体中文</a></p>

<!-- release-status:start -->
**Renamint 1.12.2 · Apple silicon · macOS 26 or later**

[Download the DMG](https://github.com/SufuTeam/Renamint/releases/download/v1.12.2/Renamint-1.12.2-arm64.dmg) · [Release notes and checksums](https://github.com/SufuTeam/Renamint/releases/tag/v1.12.2) · [All releases](https://github.com/SufuTeam/Renamint/releases)

Signed with Developer ID and notarized by Apple. The built-in AI model downloads separately (approximately 1.80 GB).
<!-- release-status:end -->

## About Renamint

Bring photos and videos from a compatible camera to your Mac over Wi-Fi, then turn camera filenames into names you can find again. Renamint combines camera browsing and downloads, local AI, reusable naming templates, and a workspace where you can preview changes before applying them.

Import files from your Mac too. Use dates, descriptions, original names, confirmed people, and sequence numbers; organize files in place or into a destination on the same disk. Review every suggestion, apply a batch, and undo when the original path and file identity still allow it.

## Key features

- **Camera Wi-Fi transfer:** discover and pair over Bluetooth, browse recorded media, preview supported photos and videos, and download selected originals directly to your Mac. No cloud relay.
- **A connected workflow:** completed camera downloads can enter the naming workspace without automatically starting AI analysis.
- **Transfer controls:** choose a destination, use date folders, inspect counts and byte progress, and retry incomplete downloads. Resume depends on the camera's response; existing same-name files are protected.
- **Local AI naming:** download the built-in model for on-device analysis, or connect your own Ollama, LM Studio, or compatible vision API. External services follow your permissions and may charge separately.
- **Reusable templates:** combine dates, titles, original names, confirmed people, and sequence numbers. Preserve extensions and review conflicts before applying.
- **Preview and undo:** compare proposed and original names, edit suggestions, and undo individual files or batches with identity and path checks.
- **Duplicate media:** compare full file contents, review renamed copies side by side, and move selected duplicates to the Trash only after confirmation. Keep at least one copy per group.
- **Release updates:** check official GitHub releases and read release notes in the app. Automatic checks can be turned off; downloads open in your browser and installation stays under your control.
- **Watched folders — Pro:** bring stable new or changed media into the workspace while Renamint runs.
- **Auto-apply — Pro:** opt in for each trusted folder after validating the template and AI settings. Automatic renames stay in that folder and remain visible in history.

[Explore the guide](https://renamint.com/en/docs) · [Read practical tutorials](https://renamint.com/en/blog)

## Camera compatibility

Status as of **October 31, 2026**. “Integrated” means an implementation exists, not that every listed camera has passed physical-device testing. Firmware and media formats affect availability.

| Camera | Status | Current scope |
| --- | --- | --- |
| DJI Osmo Action 6 | Hardware verified | Camera library, photo/video preview, and original-file Wi-Fi downloads verified, including a completed transfer batch. |
| DJI Osmo Action 2 / 3 / 4 / 5 Pro | Integrated · hardware testing pending | Osmo protocol integration and model recognition are present; Action 6 test results do not verify these models. |
| DJI Osmo Pocket 3 / 4 / 4 Pro · Osmo Nano | Integrated · hardware testing pending | Wireless media paths are implemented; library access, downloads, and previews still need testing on each model. |
| GoPro HERO9 / 10 / 11 / 12 / 13 Black · HERO11 Black Mini | Integrated · hardware testing pending | Pairing, Wi-Fi media lists, and original-file downloads are implemented with Open GoPro; no project-level GoPro hardware acceptance record yet. |

### Planned integrations

The following are **not current supported features** and have no confirmed release dates. Work starts with browsing and original-file transfer; panoramic playback, stitching, and live view need separate implementation and validation.

| Planned models | Scope to evaluate |
| --- | --- |
| DJI Osmo 360 | Complete the wireless media workflow and hardware validation. Recognition exists, but full support and raw panoramic processing remain unverified. |
| Insta360 X3 / X4 / X4 Air / X5 | Candidate integration: evaluate wireless browsing and original-file downloads first. Not integrated; raw panoramic stitching is not a current feature. |
| RICOH THETA X / Z1 | Candidate integration: evaluate media listing and downloads through public interfaces. Not integrated yet. |
| GoPro MAX 2 | Candidate integration: validate the model and media formats separately. Not enabled; panoramic playback or stitching is not promised. |
| DJI Mavic 3 · DJI Neo 2 | Research candidates: wireless transfer needs separate integration and hardware testing. The current version does not support DJI drone Wi-Fi connections. |

[Full compatibility notes](https://renamint.com/en/cameras) · [Wi-Fi transfer walkthrough](https://renamint.com/en/wifi-camera-transfer-mac)

## Free and Pro

| Feature | Free | Pro |
| --- | --- | --- |
| Camera Wi-Fi browsing and downloads, on compatible devices | ✓ | ✓ |
| Manual naming, templates, preview, and undo | ✓ | ✓ |
| AI analyses | 50 per month | Unlimited |
| Watched folders | — | ✓ |
| Auto-apply in trusted folders | — | ✓ |
| Active Macs per license | — | 2 |

**One-time lifetime Pro: US$19.90 early bird through 2026.** New orders are US$29.90 from **January 1, 2027, 00:00 Asia/Shanghai (UTC+8)**. External AI provider fees are separate.

[Pricing and purchase](https://renamint.com/en/pricing) · [Recover a key or manage devices](https://licenses.sufuapp.com/portal)

## Installation and first use

1. Download the DMG above, open it, and drag Renamint into Applications.
2. Open Renamint. Choose local rules or prepare your preferred AI method; the built-in model downloads separately.
3. Add local photos and videos, or open Camera import to connect a compatible camera.
4. Choose a naming template, review suggestions, and confirm changes.
5. If you purchased Pro, enter the emailed key in Settings → License.

Connecting a camera temporarily switches the Mac to its Wi-Fi hotspot, which may interrupt internet access. Normal disconnection attempts to restore the previous network. Keep the app running during transfers and folder monitoring.

## Updating Renamint

Download the latest DMG, quit Renamint, and replace the app in Applications. Existing library data, templates, preferences, and license are kept. Versions 1.12.0 and later can check for updates from Settings → About or the app menu; older versions can update using the download above.

## Compatibility and privacy

- **Apple silicon Mac, macOS 26 or later.** No Intel installer is currently provided.
- JPG, PNG, HEIC, MP4, MOV, and other supported media; RAW decoding depends on macOS. Some video formats can use optional FFmpeg tools. Office documents are not supported.
- Video analysis uses **1–8 sampled frames**, not every frame or audio transcription.
- Downloading a camera's original does not imply support for raw panoramic playback or stitching.
- Camera transfers and built-in AI keep media local. Remote AI receives data only according to the service settings and your permission.
- Pro activation requires internet; signed offline receipts last 30 days and renew online.

[Privacy details](https://renamint.com/en/privacy) · [License and device guide](https://renamint.com/en/license-and-new-mac)

## Feedback and help

Use **Help → Feedback** or **Settings → Support & diagnostics** in the app. Renamint opens a GitHub draft for you to review before publishing. You can also [report a problem or suggest a feature](https://github.com/SufuTeam/Renamint/issues/new/choose).

Include the app and macOS versions, steps to reproduce, and the camera model and firmware for transfer issues. Review screenshots before posting. Never post license keys, API keys, private media, or personal file paths. For a missing activation email, use the license portal with the checkout email instead of posting purchase details publicly.

## About this repository

This is the official distribution and feedback repository. It does not contain the proprietary app source. Third-party notices ship with the app. The modified AGPL Keygate server's complete corresponding source is available in [licensing](licensing/).

© 2026 Sufu. Renamint. Camera brands belong to their respective owners; this project is not their official application.
