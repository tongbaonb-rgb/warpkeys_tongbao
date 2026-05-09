# ⚡TONGBAO's WARP Key Gen

[![License](https://shields.io)](LICENSE)
[![GitHub stars](https://shields.io)](https://github.com)
[![GitHub issues](https://shields.io)](https://github.com)

> **WARP Key Gen** 是一个用于快速生成 Cloudflare WARP+ (WARP Plus) 许可密钥（License Key）的自动化工具。旨在帮助用户轻松获取高速、无限制的 WARP 流量。

## 🚀 功能特点

- **快速生成**：毫秒级生成全新的 WARP 许可密钥。
- **无需等待**：无需繁琐的邀请和注册流程。
- **高自由度**：支持自定义生成密钥的次数或循环批量生成。
- **轻量化**：基于简单脚本开发，无复杂依赖。

## 🛠️ 安装与使用

### 1. 前提条件
- 安装了 [Python 3.x](https://python.org) (如果你的工具是用 Python 写的) 或 [Node.js](https://nodejs.org)。

### 2. 获取工具
```bash
git clone https://github.com
cd warp-key-gen
```

### 3. 安装依赖
```bash
# 如果是 Python 项目
pip install -r requirements.txt

# 如果是 Node.js 项目
npm install
```

### 4. 运行
```bash
# 如果是 Python 项目
python main.py

# 如果是 Node.js 项目
node index.js
```

## ⚙️ 使用说明
运行脚本后，它会自动在终端输出生成的 WARP+ Key。
你可以通过修改 `config.json` 或修改代码中的循环参数来决定生成 Key 的数量。

*提示：获得的 Key 流量通常为 12PB，但在某些特殊情况下，可以通过再次生成 Key 来覆盖旧 Key。*

## 💡 使用示例
```bash
$ python main.py
[+] Generating...
[+] Key: 5c8b9d0a-1234-5678-abcd-1234567890ef
[+] Enjoy!
```

## 🛡️ 免责声明
- 本工具仅用于学习交流，请勿用于商业用途。
- 请遵守 Cloudflare 的服务条款。
- 因使用本工具造成的任何问题，作者概不负责。

## 🤝 贡献
欢迎提交 Issue 和 Pull Request！

## 📄 许可证
[MIT](LICENSE) © [Your Name]
