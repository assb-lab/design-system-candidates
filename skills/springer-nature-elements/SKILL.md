---
name: springer-nature-elements
description: Springer Nature Elementsの公開デザインシステムを参照し、Nature/Springer NatureテーマのWeb UIや科学技術コンテンツ、研究紹介HTMLを構築する。npmパッケージ、Dart Sass、デザイントークン、コンポーネントを活用し、学会PPTXへは情報設計のみ応用する。
metadata:
  version: "0.1.0"
  origin: "assb-lab-original-elements-guidance"
---

# Springer Nature Elements — research web design

Springer Nature公式[Elements Design System](https://eds.springernature.com/get-started/)の**参照・導入を支援する非公式Agent Skill**。Springer Nature/Natureが制作・承認したスキルではなく、公式フォント・ロゴ・コンポーネントのコードは同梱していない。

## 向いている用途

- Nature Portfolioの情報設計を参考にした研究室Webサイト、技術ブログ、研究データの解説ページ
- NatureテーマとSpringer Natureテーマの**Webデザイン**を、公式コンポーネント／デザイントークンから構築
- 学会HTMLスライド、PPTX、ポスターで見出し階層・余白・カード・図表との関係を整理するための**構図の参考**
- 研究用Webアプリのアクセシビリティ、記事一覧、検索、カード、ヘッダーやフォームの改善

**対象外:** これだけでNature誌の図版投稿規定を満たすとは考えない。論文Figuresには別の `nature-figure-style` を使う。

## 公式の構成

- ElementsはSpringer NatureとNatureのブランドテーマ、Sassスタイル、コンポーネント、ユーティリティを持つ。
- 公式は `@springernature/elements` とDart Sassによる導入を案内している。利用するテーマのCore/Enhanced等のスタイルを適切に取り込む。
- NatureテーマとSpringer Natureテーマを**同じ画面で無条件に混合しない**。
- コンポーネントのHTMLはHandlebarsテンプレート、スキーマ・サンプルデータ等が参照可能。React専用UIキットとして誤認しない。
- 構成・パス・利用条件・インストール可能なnpmバージョンは変わり得るので、現在のパッケージを確認する。

## トークン／書体

- ブランドトークンを暗記で再現せず、公式[Design Tokens](https://eds.springernature.com/design-tokens/)と[Nature Colour](https://eds.springernature.com/foundations/nature/colour/)を参照する。
- Natureの公式Web見出し・本文にはHarding、サービスによってGraphikが使われる。**これらはライセンスが必要な場合があるため、フォントファイルを収集・再配布・埋め込みしない。**
- このスキルのオリジナルHTMLサンプルは**独自のニュートラルな研究記事スタイル**で、Nature公式サイトのレプリカではない。
- テキストはWCAG 2.1 AAを目安に4.5:1以上を確保し、色のみに頼って意味やリンクを伝えない。アクセント色の使いすぎや濃淡の手作りを避ける。
- 公式テーマのトークンが確認できない場合は、勝手に公式HEX値やSCSS変数名を作らない。

## Node.js / Sass の利用

[implementation.md](references/implementation.md)を読む。

- Node.jsの作業でpnpmが使える新規プロジェクトなら **pnpmを優先**（`pnpm add` / `pnpm add -D` / `pnpm run` / `pnpm dlx`）。pnpmがない場合はnpm。
- 既存のpackageManagerとロックファイルを尊重し、pnpmへ勝手に移行しない。
- 公式導入例は `pnpm add @springernature/elements` と `pnpm add -D sass` に読み替えてよいが、**インストールできる版・パス・Sassバージョンを先に確認**。
- 現行の公式get-startedに記載される例は `themes/nature/scss/core.scss`、`enhanced.scss` など。npm公開版や採用中のビルド環境に合わせてパスを調整する。
- `pnpm dlx skills add ...` または `npx skills add ...` はこのスキルのインストールであり、公式npmコンポーネントは別途導入する。

## HTML/PPTX等への適用

[web-and-slides.md](references/web-and-slides.md)を参照。

- Web UI: 実際に公式コンポーネントを組み込む場合、公式SCSSやJSが提供する状態・アクセシビリティ仕様を確認。
- HTMLスライド: `assets/editorial-starter.html` は参考レイアウト。16:9に直してもブランドの公式テンプレートと断定しない。
- PPTX: 編集可能なネイティブの図形・テキストで余白、タイポグラフィ階層、図表の配置を再現。ロゴやHarding書体を無断で再現しない。
- 科学図表: Natureの論文Figuresに必要な軸・スケール・文字サイズ・DPIは `nature-figure-style` を別途参照する。

## 最終チェック

1. ブランド名とロゴの適切な利用権を確認。
2. 正式なElementsテーマと単なる独自参考デザインを明確に区別。
3. 公式のコンポーネント仕様とパッケージの現行のファイル構造を検証。
4. 文字コントラスト、キーボード、見出し階層、フォームラベル、レスポンシブ、読み上げ順、引用出典を検査。
5. 学会発表では会場の投影距離に適した文字・線・図の大きさにする。

権利・参考: [sources-and-licensing.md](references/sources-and-licensing.md)
