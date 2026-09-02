<div align="center">

# ⚡ HARNEMON (ハーネモン) ⚡

**ポケモン風・ゼロ依存のAIコーディングエージェント専用自律ハーネスコンパニオン**

<p align="center">
  <em>「グローバル・ハーネモンはクラス（種/Species）であり、プロジェクト・ハーネモンはインスタンス（『サトシのピカチュウ』）です。」</em>
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> •
  <a href="README.ko.md"><b>한국어</b></a> •
  <a href="README.ja.md"><b>日本語</b></a> •
  <a href="README.zh-CN.md"><b>简体中文</b></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg?style=for-the-badge)](#-3つの不変条件)
[![Runtime: Pure POSIX Bash](https://img.shields.io/badge/Runtime-Pure_POSIX_Bash-orange.svg?style=for-the-badge)](#-3つの不変条件)
[![Architecture: 3 Pillars](https://img.shields.io/badge/Architecture-3_Pillars-purple.svg?style=for-the-badge)](#-3つの柱)
[![Evolution: Self-Evolving](https://img.shields.io/badge/Evolution-Hermetic_Learning-red.svg?style=for-the-badge)](#-自己進化--インキュベートエンジン)

<br/>

```text
       ┌──────────────────────────────────────────────────────────────┐
       │   🌐 GLOBAL HARNEMON (Class / 種の設計図)                    │
       │   ~/.harnemon/ (Nimbleet, Fortoise, Monkin, Yagni 設計図)    │
       └──────────────────────────────────────────────────────────────┘
                    │                                 ▲
     harnemon adopt │                                 │ harnemon register
                    ▼                                 │
       ┌──────────────────────────────────────────────────────────────┐
       │   🏠 PROJECT HARNEMON (Instance / 生きたパートナー)          │
       │   /my-project/.harnemons/ (譲り受けた・孵化したパートナー)  │
       └──────────────────────────────────────────────────────────────┘
```

</div>

---

## 🌟 コア哲学：クラス vs インスタンス ＆ インキュベーター

従来のAIハーネスは、何百行もの巨大なプロンプトをコピペするか、重いnpm/pipパッケージでプロジェクトを汚染していました。**Harnemon（ハーネモン）は、オブジェクト指向のクラス/インスタンスパラダイムとポケモンのメタファーによってこの問題を解決します。**

### 1. グローバル・ハーネモンはクラス（種 / Species）
- 開発者のグローバルベルト `~/.harnemon` に常駐します。
- **ピカチュウ、ゼニガメ、ヒトカゲ、フシギダネ** が種の遺伝的設計図であるように、単一のリポジトリに汚染されていない純粋な **3本の柱DNA（ルール、スキル、フック設計）** を保持します。

### 2. プロジェクト・ハーネモンはインスタンス（『サトシのピカチュウ』）
- 任意のリポジトリで `harnemon adopt` を実行すると、そのワークスペースに結びついた **唯一無二の生きたハーネモンインスタンス** が誕生します。
- **サトシのピカチュウ** が旅を通じて独自の戦闘技を習得するように、採用されたハーネモンは **そのリポジトリのドメイン規約、設計パターン、バグ履歴を自律的に吸収して自己進化（Self-Evolution）** します。
- **ゼロ依存（Zero-Dependency）**: `package.json` や `Cargo.toml` に **0バイト** も不要な依存を残しません。純粋なPOSIX Bashと標準Gitだけで完全に動作します。

### 3. ハーネモン・インキュベーター（真っ白なタマゴ 🥚）
- 既存のルールセットを使いたくない場合は、`harnemon incubate` で **完全に真っ白なタマゴ（Blank Egg）** から開始できます。
- 日常のコーディングとフィードバック（2回修正ルール）を通じて、タマゴが自律的に3本の柱（ルール・スキル・フック）を合成し、経験値（EXP）を蓄積します。
- 孵化の準備が整ったら `harnemon hatch <種名>` で正式な種として誕生させ、`harnemon register` で図鑑に登録できます。

---

## 📖 ハーネデックス (Harnedex) — 第1世代の伝説の4大アーキタイプ

| No. | 種 (Species) | タイプ (Type) | モデル元 | 特徴 ＆ 主要技 |
| :---: | :--- | :--- | :--- | :--- |
| **No.000** | **[ハーネモンのタマゴ](docs/harnemon-incubator.md)** | `Incubating 🌱` | `Harnemon Incubator` | **特性: まっさらなキャンバス**<br>0ルールの初期状態。開発者の習慣と2回修正フィードバックを吸収してカスタム種へと孵化。 |
| **No.001** | **[Nimbleet (ニムブリート)](docs/case-studies/01-jihan-harness.md)** | `Electric ⚡` | `2JIHAN/jihan-harness` | **特性: ライトニングルーター**<br>超高速50トークンスキルルーター。光速の応答性、ゼロ依存クリーン機動。 |
| **No.002** | **[Fortoise (フォートイス)](docs/case-studies/02-everything-claude-code.md)** | `Water 💧` | `affaan-m/everything-claude-code` | **特性: コンフィグガードシェル**<br>288個の技を持つ巨大要塞。AIがリント設定を勝手に弱める試みを物理的に完全ブロック。 |
| **No.003** | **[Monkin (モンキン)](docs/case-studies/03-obra-superpowers.md)** | `Fire 🔥` | `obra/superpowers` | **特性: 鉄則のるつぼ (The Iron Law)**<br>当て推量のコーディングを焼き払い、根本原因が証明されるまでコードの変更を厳禁。 |
| **No.004** | **[Yagni (ヤグニ)](docs/case-studies/04-dietrich-ponytail.md)** | `Grass 🍃` | `DietrichGebert/ponytail` | **特性: 怠惰のはしご (Ladder of Laziness)**<br>無駄を削ぎ落とす天才的怠け者。投機的コードを削減(`-N行`)し、標準ライブラリを最優先。 |

---

## 🏛️ 3つの柱 (The 3 Pillars)

```text
       ┌──────────────────────────────────────────────────┐
       │                ハーネモンの身体構造              │
       └──────────────────────────────────────────────────┘
             │                  │                  │
             ▼                  ▼                  ▼
      [ 柱 1: Rule ]     [ 柱 2: Skill ]    [ 柱 3: Hook ]
      • 常時特性 (Abilities) • 習得技 (Moves)   • 所持アイテム (Held Items)
      • 常時認知的制約   • オンデマンド専門力 • 物理ハードゲート
      • (~50トークンハブ) • (詳細マニュアル)   • (exit 0 / exit 1)
```

---

## ⚡ クイックスタート

```bash
# 1. グローバルツールのインストール（最新リリース）
mkdir -p ~/.harnemon
curl -fsSL https://github.com/2JIHAN/harnemon/releases/latest/download/harnemon.tar.gz | tar -xz -C ~/.harnemon
~/.harnemon/bin/harnemon setup

# 2. プロジェクトで採用またはタマゴを配置
cd /path/to/my-project
harnemon incubate          # タマゴから自律育成
harnemon adopt nimbleet    # 電撃ルーター Nimbleet を採用

# 3. 状態の確認
harnemon status
harnemon audit
```

---

## 👥 コントリビューター (Contributors)

Harnemon に貢献してくださった素晴らしい皆様に感謝いたします:

<a href="https://github.com/2JIHAN/harnemon/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=2JIHAN/harnemon" alt="Harnemon Contributors" />
</a>

バグ修正、新しいハーネモン種の提出、ドキュメント改善など、あらゆる貢献を歓迎します！詳細は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

---

## 📄 ライセンス

Harnemon は [MIT License](LICENSE) の下でオープンソースとして公開されています。
