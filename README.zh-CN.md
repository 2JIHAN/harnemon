<div align="center">

# ⚡ HARNEMON (宝可梦式智能体 Harness) ⚡

**面向 AI 编码智能体的宝可梦风格、零依赖自进化 Harness 伴侣**

<p align="center">
  <em>“全局 Harnemon 是一个类（物种/Species），而项目 Harnemon 是一个实例（‘小智的皮卡丘’）。”</em>
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> •
  <a href="README.ko.md"><b>한국어</b></a> •
  <a href="README.ja.md"><b>日本語</b></a> •
  <a href="README.zh-CN.md"><b>简体中文</b></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg?style=for-the-badge)](#-三大不变量)
[![Runtime: Pure POSIX Bash](https://img.shields.io/badge/Runtime-Pure_POSIX_Bash-orange.svg?style=for-the-badge)](#-三大不变量)
[![Architecture: 3 Pillars](https://img.shields.io/badge/Architecture-3_Pillars-purple.svg?style=for-the-badge)](#-三大支柱)
[![Evolution: Self-Evolving](https://img.shields.io/badge/Evolution-Hermetic_Learning-red.svg?style=for-the-badge)](#-自进化--孵化引擎)

<br/>

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 全局 HARNEMON (Class / 物种基因蓝图)                    │
       │   ~/.harnemon/ (Nimbleet, Fortoise, Monkin, Yagni 蓝图)      │
       └──────────────────────────────────────────────────────────────┘
                    │                                 ▲
     harnemon adopt │                                 │ harnemon register
                    ▼                                 │
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 项目 HARNEMON (Instance / 活体伙伴)                     │
       │   /my-project/.harnemons/ (领养或孵化出的伙伴)               │
       └──────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 核心哲学：类 vs 实例 & 孵化器

传统的 AI Harness 要么把数百行臃肿的 Prompt 复制粘贴到每个仓库，要么引入沉重的 npm/pip 依赖。**Harnemon 通过面向对象的 Class/Instance 范式与宝可梦隐喻彻底解决了这一问题。**

### 1. 全局 Harnemon 是类（物种 / Species）
- 常驻在开发者的全局腰带 `~/.harnemon` 中。
- 正如 **皮卡丘、杰尼龟、小火龙、妙蛙种子** 代表物种蓝图一样，全局 Harnemon 保持纯净的 **三大支柱 DNA（规则、技能、钩子架构）**，不受任何单一代码库污染。

### 2. 项目 Harnemon 是实例（“小智的皮卡丘”）
- 在任何代码库中运行 `harnemon adopt`，即可实例化绑定到该工作区的 **独特、鲜活的 Harnemon 实例**。
- 正如 **小智的皮卡丘** 在冒险中掌握独特的战斗技能一样，被领养的 Harnemon 会 **自律吸收该项目的领域规范、架构特性和 Bug 修复历史，实现自进化（Self-Evolution）**。
- **零依赖设计（Zero-Dependency）**：在 `package.json` 或 `Cargo.toml` 中留下 **0 字节** 垃圾依赖。仅靠原生 POSIX Bash 和标准 Git 即可完美运行。

### 3. Harnemon 孵化器（空白蛋 🥚）
- 不想使用预置规则？运行 `harnemon incubate` 从 **一颗完全空白的蛋** 开始。
- 随着结对编程和提供反馈（2次修正法则），蛋会自动提炼三大支柱规则与技能并积累经验值（EXP）。
- 孵化成熟后，运行 `harnemon hatch <名称>` 诞生专属物种，并用 `harnemon register` 注册进全局图鉴！

---

## 📖 Harnedex (宝可梦图鉴) — 第1代四大传奇原型

| 编号 | 物种 (Species) | 属性 (Type) | 现实来源原型 | 核心特性与招式 |
| :---: | :--- | :--- | :--- | :--- |
| **No.000** | **[Harnemon 蛋](docs/harnemon-incubator.md)** | `Incubating 🌱` | `Harnemon 孵化器` | **特性: 空白画布 (Blank Canvas)**<br>0 规则起点。吸收开发者习惯和 2 次修正反馈，孵化为定制物种。 |
| **No.001** | **[Nimbleet (闪电鼠)](docs/case-studies/01-jihan-harness.md)** | `Electric ⚡` | `2JIHAN/jihan-harness` | **特性: 闪电路由器**<br>极速 50-token 技能调度中枢。闪电般的响应，零依赖极致轻量。 |
| **No.002** | **[Fortoise (铠甲龟)](docs/case-studies/02-everything-claude-code.md)** | `Water 💧` | `affaan-m/everything-claude-code` | **特性: 配置守卫甲壳**<br>拥有 288 项技能的庞大堡垒。物理拦截任何 AI 擅自放宽 linter/formatter 规则的企图。 |
| **No.003** | **[Monkin (铁律猴)](docs/case-studies/03-obra-superpowers.md)** | `Fire 🔥` | `obra/superpowers` | **特性: 铁律熔炉 (The Iron Law)**<br>燃烧猜想；在证明根本原因之前，绝对禁止修改代码。 |
| **No.004** | **[Yagni (懒惰草)](docs/case-studies/04-dietrich-ponytail.md)** | `Grass 🍃` | `DietrichGebert/ponytail` | **特性: 懒惰之梯 (Ladder of Laziness)**<br>修剪冗余的天才懒汉。大刀阔斧削减投机代码 (`-N行`)，标准库优先。 |

---

## 🏛️ 三大支柱 (The 3 Pillars)

```text
       ┌──────────────────────────────────────────────────┐
       │                 Harnemon 身体构造                │
       └──────────────────────────────────────────────────┘
             │                  │                  │
             ▼                  ▼                  ▼
      [ 支柱 1: Rule ]   [ 支柱 2: Skill ]  [ 支柱 3: Hook ]
      • 常驻特性 (Abilities) • 掌握招式 (Moves) • 携带道具 (Held Items)
      • 常驻认知约束     • 按需专业技能     • 物理硬拦截
      • (~50-token 中枢) • (详细操作指南)   • (exit 0 / exit 1)
```

---

## ⚡ 快速开始 (Quickstart)

```bash
# 1. 安装全局工具
git clone https://github.com/2JIHAN/harnemon.git ~/.harnemon
ln -sf ~/.harnemon/bin/harnemon ~/.local/bin/harnemon

# 2. 在项目中领养或放置空白蛋
cd /path/to/my-project
harnemon incubate          # 放置空白蛋开启自律孵化
harnemon adopt nimbleet    # 领养闪电路由器 Nimbleet

# 3. 检查伙伴状态与健康
harnemon status
harnemon audit
```

---

## 📄 开源协议

Harnemon 基于 [MIT 许可证](LICENSE) 开源。
