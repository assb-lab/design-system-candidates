# Design System Candidates

学会発表、学術図表、技術資料、Webアプリなどで試せる **選択式のデザインスキル集** です。既存の [science-tokyo-design-skills](https://github.com/assb-lab/science-tokyo-design-skills) の代替候補として比較できるようにしています。

**本リポジトリに収録された6つは、公開デザインの考え方に着想を得て独自に作成したAgent Skillです。** 参照元の公式デザインシステム、既存スキルのコピー、ロゴ・フォント・コンポーネントは同梱していません。大学のブランドが求められる公式資料では大学規定を優先してください。

## 導入（Claude Code / Codex）

Node.js 22.20以上が必要です。このリポジトリは公開されています。**pnpmが使える場合は `pnpm dlx skills add` を優先**し、pnpmがない場合は `npx skills add` を使います。

```bash
# pnpmがある場合の推奨コマンド
pnpm dlx skills add assb-lab/design-system-candidates --list
pnpm dlx skills add assb-lab/design-system-candidates --skill digital-agency-design -g -a claude-code -a codex

# pnpmがない場合のnpx版（以下のコマンドも動作します）
# 収録スキルを一覧表示（インストールなし）
npx skills add assb-lab/design-system-candidates --list

# 研究発表・論文図表向けの1件を両エージェントへ
npx skills add assb-lab/design-system-candidates --skill scientific-editorial -g -a claude-code -a codex

# 6種類すべて追加（ユーザー全体）
npx skills add assb-lab/design-system-candidates --skill '*' -g -a claude-code -a codex

# 個別例
npx skills add assb-lab/design-system-candidates --skill metropolis-research -a codex

# 更新
npx skills update
```

`-g` を外すとプロジェクトに導入します。エージェントの指定は環境に応じて変更可能です。

**Node.jsの作業:** pnpmが利用可能なら `pnpm add` / `pnpm install` / `pnpm run` / `pnpm dlx` を優先します。ただし既存の `packageManager` 指定・ロックファイルが別のマネージャーを示す場合は、無断で移行せず、その指定を優先してください。

## 収録スキル

| 名前 | 概要・特徴 | 何に使えるか | 想定形式 | `--skill` 名 |
| --- | --- | --- | --- | --- |
| [Metropolis Research](skills/metropolis-research/SKILL.md) | 白に近い背景、左揃え、広い余白、短い結論タイトル、控えめなアクセントライン。研究図と数式を主役にする。 | 学会口頭発表・研究室セミナー・博士審査 | PPTX、HTML、ポスター、グラフ | `metropolis-research` |
| [Scientific Editorial](skills/scientific-editorial/SKILL.md) | 白地、簡潔なサンセリフ、規則的なパネル配置、図表に隣接した注記。美観より学術的な正確性を優先。 | 学術論文のマルチパネル図・学会ポスター・学会発表 | 論文図、ポスター、PPTX、HTML | `scientific-editorial` |
| [Carbon Research](skills/carbon-research/SKILL.md) | ニュートラルなグレーが主役。8px刻みのグリッドと明瞭な状態・操作区分、必要な箇所だけブルーで強調。 | 測定・解析WebアプリのUI・統計・技術ダッシュボード | Web UI、HTML、PPTX、グラフ | `carbon-research` |
| [Digital Agency Design](skills/digital-agency-design/SKILL.md) | デジタル庁の日本語UI・アクセシビリティ・ローカルデザインシステムを参考にした独自スキル | 研究用Webアプリ、フォーム、テーブル、ファイルアップロード | React、HTML/CSS、Figma、UI設計 | `digital-agency-design` |
| [Midnight Technical](skills/midnight-technical/SKILL.md) | 深い紺色、明るい文字、明瞭なスペクトル色。3Dモデルやシミュレーション画像が主役。 | 3D・AR・材料シミュレーションの紹介・バンド構造・電子状態・スペクトル発表 | PPTX、HTML、技術デモ、グラフ | `midnight-technical` |
| [Tufte Research](skills/tufte-research/SKILL.md) | 温かい紙の色、落ち着いたセリフ、本文の近くに配置した余白注釈、飾りを減らしたデータ可視化。 | 研究手法の解説HTMLと技術ノート・講演配布資料・長文の研究紹介 | HTML文書、配布資料、PPTX、図表 | `tufte-research` |

### 選び方

- **学会口頭発表:** `metropolis-research` — 1枚1メッセージ、図や式を主役にする。
- **学会ポスター・論文図・SEM/XRD/XPS/EIS:** `scientific-editorial` — データの正確さ・多パネル・注釈・スケールバーを優先。
- **実験データ解析Webアプリ:** `carbon-research` — コンポーネント・グリッド・表・データ可視化の統一。
- **日本語の入力・データ管理画面:** `digital-agency-design` — アクセシブルなフォーム・データテーブル・ファイルアップロード。科学グラフには `scientific-editorial` を併用。
- **3D・電子構造・技術デモ:** `midnight-technical` — 紺色背景、高コントラストなスペクトル線。
- **研究方法の解説記事・配布資料:** `tufte-research` — 余白注釈と本文＋図表の関係を整理。

## スキル内のファイル

最初の5つのテーマスキルは以下の構成です。

```text
skills/<skill-name>/
├── SKILL.md                  # 使いどころ、ルール、実装方針、チェックリスト
└── assets/
    ├── tokens.json           # PPTX/HTML/Web向けの共通デザイントークン
    ├── tokens.css            # CSSカスタムプロパティ
    ├── scientific.mplstyle   # matplotlibスタイル
    └── slide-template.html  # 16:9 HTMLサンプル（実データは未挿入）
```

新しいDigital Agency Designは、上流の公式トークンを再配布しないため構成が異なります。

```text
skills/digital-agency-design/
├── SKILL.md
├── references/
│   ├── foundations-and-accessibility.md
│   ├── components-and-research-workflows.md
│   ├── implementation.md
│   └── sources-and-licenses.md
└── assets/
    ├── tokens.json
    └── tokens.css
```

各スキルは **デザインを適用するための指示とアセット** を提供します。`npx skills add` はPPTX生成エンジン、Python、matplotlib、TypstやIBM CarbonのUIライブラリ自体を自動でインストールするコマンドではありません。

### 使用例

```text
このLi-Mg負極の学会発表をMetropolis ResearchのデザインでPPTXにして。
このXPS/UPS/EISのマルチパネル図をScientific Editorialで読みやすくして。
デジタル庁デザインシステムを参考に、測定データ管理Webアプリのフォームをアクセシブルにして。
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

本家の出力機能や前提条件は上流の最新ドキュメントを確認してください。**収録6スキルをインストールしても上記4件は自動的にはインストールされません。**

## その他の既存Agent Skills — 追加調査（2026-11-19）

以下は実際に公開されている `SKILL.md` を確認できたものです。**このリポジトリ内には複製せず、上流から直接 `npx skills add` してください。** CLIによる個々のインストール実行テストまでは行っていません。必要な実行環境・APIキーは別途準備します。

### A. デザインテーマ・Webデザイン

| スキル | 得意なこと・何に使えるか | 注意点 | インストール |
| --- | --- | --- | --- |
| [Theme Factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | **スライド／文書／HTML向けの10種類の配色＋書体テーマ**。Ocean Depths、Modern Minimalist、Midnight Galaxyなどを選べるほか、新規テーマも提案 | 配色・フォント中心。スライド生成エンジンは別 | `npx skills add anthropics/skills --skill theme-factory` |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 多数のデザインスタイル、パレット、書体、グラフ、アクセシビリティやUIパターンを検索。React/Next.js等の**研究用Webアプリ・解析UI**に好適 | Web/UI中心でPPTX用テンプレートではない | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max` |
| [Design System](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/design-system/SKILL.md) | Primitive → Semantic → Componentのトークン階層。CSS変数、コンポーネント定義、検証、スライドの規則にも対応 | 既存の大学公式トークンと競合しないよう役割分離が必要 | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill design-system` |
| [Frontend Design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 量産型ではないレイアウト・タイポグラフィ・色使い、研究WebページやWebアプリの見た目の改善 | 科学データの妥当性や数式組版には別途確認が必要 | `npx skills add anthropics/skills --skill frontend-design` |
| [Slides（HTML/Chart.js）](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/slides/SKILL.md) | HTMLスライド、Chart.jsのデータ可視化、戦略的なスライド構成 | マーケティング系の原則も含むため研究発表では主張の根拠を優先 | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill slides` |

### B. スライド制作・配布用プレゼン

| スキル | 得意なこと・何に使えるか | 注意点 | インストール |
| --- | --- | --- | --- |
| [Slidev（公式）](https://github.com/slidevjs/slidev/tree/main/skills/slidev) | Markdown＋Vueの**Webプレゼン**。数式、Mermaid、アニメーション、コード、インタラクティブな図。PDF/PPTX/SPAなどに出力 | Slidev本体のNode.js環境等が必要。PPTXは元データの編集性を別途確認 | `npx skills add slidevjs/slidev --skill slidev` |
| [Presentation Creator](https://github.com/mblode/agent-skills/tree/main/skills/presentation-creator) | 発表のストーリー、スライド分量、見出し、話者ノートの設計。Marp、Slidev、Reveal.js等の構成 | `.pptx`自体の作成・編集は別ツールへ渡す | `npx skills add mblode/agent-skills --skill presentation-creator` |
| [PPTX（Anthropic）](https://github.com/anthropics/skills/tree/main/skills/pptx) | PowerPointの新規作成・編集・レビュー、テンプレート・レイアウト・注釈・ノートの処理 | スキルのインストールだけでは生成ライブラリは導入されない | `npx skills add anthropics/skills --skill pptx` |
| [Slides（Marp/Apple-like）](https://github.com/mattwoodco/skills/tree/main/skills/slides) | Markdownから余白の広いミニマルな**Apple Keynote風**プレゼンを作る | Marp CLI等の追加導入が必要。上記HTML Slidesと`slides`名が重複するので併用時に注意 | `npx skills add mattwoodco/skills --skill slides` |

### C. 学会ポスター・図版・インフォグラフィック

| スキル | 得意なこと・何に使えるか | 注意点 | インストール |
| --- | --- | --- | --- |
| [PPTX Posters](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/pptx-posters) | **PowerPointで編集できる学会ポスター**。物理寸法、印刷規定、ソース追跡、アクセシビリティ、PPTX検証 | Python / python-pptx等が必要。ポスター専用 | `npx skills add K-Dense-AI/scientific-agent-skills --skill pptx-posters` |
| [LaTeX Posters](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/latex-posters) | beamerposter / tikzposter / baposterを使うマルチカラムの**数式中心の学会PDFポスター** | LaTeXと対象クラスが必要（baposterはクラスを別途提供） | `npx skills add K-Dense-AI/scientific-agent-skills --skill latex-posters` |
| [Canvas Design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | 研究紹介ポスター、展示パネル、配布用ビジュアルの**構図・タイポグラフィを重視した静的デザイン** | PNG/PDFなどの静的成果物が中心。科学図表の正確性は人が検証 | `npx skills add anthropics/skills --skill canvas-design` |
| [Infographics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/infographics) | 研究概要、比較、タイムライン、測定フローを**インフォグラフィック画像**として構成 | OpenRouter APIキー・ネットワーク・費用が必要。生成画像は事実と数値を必ず検証 | `npx skills add K-Dense-AI/scientific-agent-skills --skill infographics` |
| [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-schematics) | 実験フロー、装置概念図、プロセス、システム構造の図案と自動レビュー | OpenRouter APIキー等が必要。**ラスターPNG**出力でありベクター図版ではない | `npx skills add K-Dense-AI/scientific-agent-skills --skill scientific-schematics` |

### 組合せの例

- **学会PPTX:** `theme-factory` ＋ `scientific-slides`（上記既存リスト）＋ `pptx`。デザイン・発表構成・ファイル出力を分離。
- **学会ポスター:** `scientific-visualization`（上記既存リスト）＋ `pptx-posters` または `latex-posters`。科学図の検証とレイアウト制作を分離。
- **測定Webアプリ:** `ui-ux-pro-max` ＋ `design-system` ＋ `scientific-editorial`（このリポジトリ）。操作体験・トークン・図表の質を分担。
- **Webベースの研究発表:** `slidev` ＋ `theme-factory`。アニメーション／数式／デザインの統一を分担。

複数スキルで同名（例：`slides`）がある場合は、インストールする側の名前衝突に注意し、どちらかを選ぶかCLIの `--rename` を利用してください。外部スキルの利用権限・更新・依存ライブラリについては、各上流リポジトリの規定を優先します。

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
- [デジタル庁デザインシステムβ版](https://design.digital.go.jp/dads/) — 日本語UI、アクセシビリティ、ローカルデザインシステム。[公式利用条件](https://design.digital.go.jp/dads/introduction/notices/)も参照。
- [SeaSlides](https://github.com/touying-typ/seaslides) — Midnightなどのテーマ群。
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/) — 注釈と情報デザイン。
- [skills CLI](https://github.com/vercel-labs/skills) — Agent Skillの導入と更新。

本リポジトリの **独自に作成した** 指示文とアセットにはリポジトリのMITライセンスが適用されます。外部プロジェクトとは提携・認証関係にありません。
