# Design System Candidates

学会発表、学術図表、技術資料、Webアプリなどで試せる **選択式のデザインスキル集** です。既存の [science-tokyo-design-skills](https://github.com/assb-lab/science-tokyo-design-skills) の代替候補として比較できるようにしています。

**本リポジトリに収録された5つは、公開デザインの考え方に着想を得て独自に作成したAgent Skillです。** 参照元の公式デザインシステム、既存スキルのコピー、ロゴ・フォント・コンポーネントは同梱していません。大学のブランドが求められる公式資料では大学規定を優先してください。

## 導入（Claude Code / Codex）

Node.js 22.20以上が必要です。このGitHubリポジトリは現在 **private** のため、GitHub認証が必要です。Git credential helper、`gh auth login` またはSSHの認証を設定してください。

```bash
# 収録スキルを一覧表示（インストールなし）
npx skills add assb-lab/design-system-candidates --list

# 研究発表・論文図表向けの1件を両エージェントへ
npx skills add assb-lab/design-system-candidates --skill scientific-editorial -g -a claude-code -a codex

# すべて追加（ユーザー全体）
npx skills add assb-lab/design-system-candidates --skill '*' -g -a claude-code -a codex

# 個別例
npx skills add assb-lab/design-system-candidates --skill metropolis-research -a codex

# 更新
npx skills update
```

`-g` を外すとプロジェクトに導入します。エージェントの指定は環境に応じて変更可能です。

## 収録スキル

| 名前 | 概要・特徴 | 何に使えるか | 想定形式 | `--skill` 名 |
| --- | --- | --- | --- | --- |
| [Metropolis Research](skills/metropolis-research/SKILL.md) | 白に近い背景、左揃え、広い余白、短い結論タイトル、控えめなアクセントライン。研究図と数式を主役にする。 | 学会口頭発表・研究室セミナー・博士審査 | PPTX、HTML、ポスター、グラフ | `metropolis-research` |
| [Scientific Editorial](skills/scientific-editorial/SKILL.md) | 白地、簡潔なサンセリフ、規則的なパネル配置、図表に隣接した注記。美観より学術的な正確性を優先。 | 学術論文のマルチパネル図・学会ポスター・学会発表 | 論文図、ポスター、PPTX、HTML | `scientific-editorial` |
| [Carbon Research](skills/carbon-research/SKILL.md) | ニュートラルなグレーが主役。8px刻みのグリッドと明瞭な状態・操作区分、必要な箇所だけブルーで強調。 | 測定・解析WebアプリのUI・統計・技術ダッシュボード | Web UI、HTML、PPTX、グラフ | `carbon-research` |
| [Midnight Technical](skills/midnight-technical/SKILL.md) | 深い紺色、明るい文字、明瞭なスペクトル色。3Dモデルやシミュレーション画像が主役。 | 3D・AR・材料シミュレーションの紹介・バンド構造・電子状態・スペクトル発表 | PPTX、HTML、技術デモ、グラフ | `midnight-technical` |
| [Tufte Research](skills/tufte-research/SKILL.md) | 温かい紙の色、落ち着いたセリフ、本文の近くに配置した余白注釈、飾りを減らしたデータ可視化。 | 研究手法の解説HTMLと技術ノート・講演配布資料・長文の研究紹介 | HTML文書、配布資料、PPTX、図表 | `tufte-research` |

### 選び方

- **学会口頭発表:** `metropolis-research` — 1枚1メッセージ、図や式を主役にする。
- **学会ポスター・論文図・SEM/XRD/XPS/EIS:** `scientific-editorial` — データの正確さ・多パネル・注釈・スケールバーを優先。
- **実験データ解析Webアプリ:** `carbon-research` — コンポーネント・グリッド・表・データ可視化の統一。
- **3D・電子構造・技術デモ:** `midnight-technical` — 紺色背景、高コントラストなスペクトル線。
- **研究方法の解説記事・配布資料:** `tufte-research` — 余白注釈と本文＋図表の関係を整理。

## スキル内のファイル

```text
skills/<skill-name>/
├── SKILL.md                  # 使いどころ、ルール、実装方針、チェックリスト
└── assets/
    ├── tokens.json           # PPTX/HTML/Web向けの共通デザイントークン
    ├── tokens.css            # CSSカスタムプロパティ
    ├── scientific.mplstyle   # matplotlibスタイル
    └── slide-template.html  # 16:9 HTMLサンプル（実データは未挿入）
```

各スキルは **デザインを適用するための指示とアセット** を提供します。`npx skills add` はPPTX生成エンジン、Python、matplotlib、TypstやIBM CarbonのUIライブラリ自体を自動でインストールするコマンドではありません。

### 使用例

```text
このLi-Mg負極の学会発表をMetropolis ResearchのデザインでPPTXにして。
このXPS/UPS/EISのマルチパネル図をScientific Editorialで読みやすくして。
OresmeProのデータ解析画面をCarbon Researchのグリッドとトークンで整理して。
3D結晶構造シミュレーションをMidnight TechnicalのHTMLスライドにして。
実験手順の説明文をTufte ResearchでHTML資料にして。
```

## 本家から直接入れられる既存のスキル（このリポジトリには複製しません）

テーマではなく、学術スライドや科学図表を **生成・検証するための既存のAgent Skill** も併用できます。これらは上流の更新、ライセンス、付属スクリプト、依存関係を保つため直接インストールしてください。

| スキル | 概要・できること | 元リポジトリ | インストール |
| --- | --- | --- | --- |
| SeaSlides | Typst/TouyingでAIプレゼン生成。Data Ink、Midnight等のテーマ集、PDF/PNG/PPTX関連ツール | [touying-typ/seaslides](https://github.com/touying-typ/seaslides) | `npx skills add touying-typ/seaslides --skill seaslides-typst-slides-skill` |
| Scientific Visualization | Matplotlib/Plotly等による正確・アクセシブルな科学図表と複数パネル、出版前の確認 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-visualization) | `npx skills add K-Dense-AI/scientific-agent-skills --skill scientific-visualization` |
| Scientific Slides | 学会、研究会、学位審査用のスライドストーリー・時間配分・ビジュアル検証 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-slides) | `npx skills add K-Dense-AI/scientific-agent-skills --skill scientific-slides` |
| Presentation Design | 編集的な視覚階層とデッキの構成。上流の `slides.md` を併せて参照 | [blisse-code/presentation-design-skill](https://github.com/blisse-code/presentation-design-skill) | `npx skills add blisse-code/presentation-design-skill` |

本家の出力機能や前提条件は上流の最新ドキュメントを確認してください。**収録5スキルをインストールしても上記4件は自動的にはインストールされません。**

## 品質・権利の原則

- データの値、外れ値、欠損、正規化、計測条件、誤差、単位、引用を見栄えのために変えない。
- 図の色は線種・マーカー・ラベルを併用。文字は通常WCAG AA相当のコントラストを目安にする。
- スライドでは会場の投影距離を意識し、論文投稿用の小さな図中文字をそのまま使わない。
- 学会主催者のテンプレート・大学公式テンプレート・論文投稿先の現行要件を優先する。
- 出力形式に応じて編集可能なソースを残す。Webのaltテキストや図表キャプションも準備する。

## デザインの参考元

- [Metropolis Beamer](https://github.com/matze/mtheme) — 余白・進捗線・ミニマルなスライド。上流テーマ本体はCC BY-SA 4.0。
- [Nature Research Figure Guide](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) — 論文の図版の整列・編集可能なラベル・画像とスケールバー。
- [IBM Carbon Design System](https://carbondesignsystem.com/) — トークン、IBM Plex、グリッド、グレー中心の構造。
- [SeaSlides](https://github.com/touying-typ/seaslides) — Midnightなどのテーマ群。
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/) — 注釈と情報デザイン。
- [skills CLI](https://github.com/vercel-labs/skills) — Agent Skillの導入と更新。

本リポジトリの **独自に作成した** 指示文とアセットにはリポジトリのMITライセンスが適用されます。外部プロジェクトとは提携・認証関係にありません。
