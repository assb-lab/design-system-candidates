---
name: digital-agency-design
description: デジタル庁デザインシステム（DADS）を参考に、日本語の研究用Webアプリ・データ管理画面・入力フォームをアクセシブルに設計・実装する。React/Tailwind・HTML・CSS・Figma・データテーブル・ファイルアップロードで使う。学会PPTXへは情報設計の原則として応用する。
metadata:
  version: "0.1.0"
  origin: "assb-lab-original-adaptation"
---

# Digital Agency Design

デジタル庁デザインシステムβ版（DADS）を参考に、assb-labが独自作成したAgent Skill。**デジタル庁の公式スキルではなく、承認・提携も受けていない。** ロゴ、Figmaデザインデータ、公式コード、フォント、ドキュメント全文を含まない。

公式サイト: https://design.digital.go.jp/dads/  
公式リソース: https://design.digital.go.jp/dads/resources/  
確認したWeb版: v2.18.3（2026-11-18）。**Figma、npmパッケージとは別のバージョン体系なので、実装時に最新の対応表を確認する。**

## 主な用途

- 日本語の研究室・実験管理Webアプリ、測定条件フォーム、実験一覧、検索、フィルタ、データテーブル、ファイルアップロード、状態表示
- React/TypeScript/Tailwind、素のHTML/CSS/JavaScript、Figmaを使うWeb UI設計
- 運用管理画面、学内・公共向けサイト、アクセシビリティ改善
- 学会スライド・ポスター・PPTXには、余白・情報階層・可読性などの**設計原則のみ**応用（公式のスライドデザインではない）

科学図表（XPS、XRD、EIS、SEM等）のグラフ配色・軸・統計検証は `scientific-editorial` 等と組み合わせる。このスキルは科学グラフ専用規格ではない。

## デザイン原則

1. まず利用者、画面で達成したいタスク、ブランド規定、既存のコンポーネント・CSS・ロックファイルを調べる。
2. DADSをコピーした「政府風の画面」にするのではなく、DADSのルールを基に**導入先のローカルデザインシステム**を定義する。
3. キーカラー、タイポグラフィのスケール、余白、角丸等は利用先向けに調整してよい。ただしアクセシビリティの骨格は壊さない。
4. 公式にないトークン値・Reactコンポーネントprops・仕様を憶測で書かない。実装の前に対象コンポーネントの公式ページ・Storybookを参照する。
5. 大学公式資料は大学のブランド規則を優先。デジタル庁のロゴ・政府機関名を流用しない。

参照: [基本デザインとアクセシビリティ](references/foundations-and-accessibility.md)、[公式ローカルデザインシステム](https://design.digital.go.jp/dads/guidance/local-design-system/)。

## 必ず守るアクセシビリティ

- テキストと背景のコントラストは原則 **4.5:1以上**、重要な非テキスト・罫線等は **3:1以上**。
- 本文とUIは原則 **16 CSS px以上**。読み物の本文行高は **1.5倍以上**。
- 操作対象は **44 CSS px以上**を基準として確保。入力ラベル、エラー内容、必須・任意、フィードバックを明示する。
- 公式の**黒と黄色の二重フォーカスインジケーターを変更しない**。キーボードの操作性・強制カラーモードを維持する。
- リンクを色だけで区別しない。見た目とDOMの読み上げ順はできる限り一致させる。
- 既存のaria属性、フォーカス管理、状態通知をスタイル変更で削除しない。

公式コンポーネントの個別要件は、その都度[公式コンポーネント一覧](https://design.digital.go.jp/dads/components/)から確認する。

## コンポーネント選択

[研究Webアプリ向けの対応表](references/components-and-research-workflows.md)で、インプットテキスト、テーブル、検索、セレクト、モーダル、ファイルアップロード、進捗表示等を適切に選ぶ。複雑なコンポーネントを無条件に採用せず、ネイティブ要素で十分なら簡素化する。

## Node.js環境・実装

[implementation.md](references/implementation.md)を必ず読む。

**pnpmが利用可能なら、Node.jsの依存追加・実行にはpnpmを優先**する（`pnpm add` / `pnpm install` / `pnpm run` / `pnpm dlx`）。pnpmがなければnpmを使う。ただし既存の `packageManager` 指定や `package-lock.json`、`yarn.lock`、`bun.lock*` 等に別のマネージャーが指定されていれば、既存ルールを尊重して勝手に移行しない。

- 公式 `@digital-go-jp/design-tokens` を導入し、公式CSSの後に `assets/tokens.css` のエイリアスを読み込む。`assets/tokens.json` はエイリアスの一覧であり、公式パッケージを置き換えない。
- Tailwind環境では公式 `@digital-go-jp/tailwind-theme-plugin` を参照する。v3とv4で設定方法が違う。
- Reactサンプルの基準は**React 19 / Tailwind CSS 3**。異なるバージョンに導入する際は互換性・実装方法を確認する。
- `pnpm dlx skills add` または `npx skills add` はAgent Skillだけを導入し、UIライブラリや公式トークンは自動インストールされない。

## 制作フロー

1. 機能とユーザー行動、データ型、既存スタック、大学・組織ブランドを把握する。
2. 必要なDADSのコンポーネントと公式ドキュメントを絞って参照する。
3. ローカルトークン・フォーム・表・ファイル操作の状態設計を定義する。
4. 既存の依存管理を尊重して実装。アクセシビリティ実装を保持する。
5. 狭幅画面、文字ズーム、キーボード操作、エラー通知、強制カラー等を試す。
6. 自動検査（axe等）に加えて人手検査を行う。検査だけでWCAG適合済と断定しない。
7. 成果物にコード、依存パッケージ、利用した公式参照、変更・加工の有無を記録する。

## 出典・権利

[公式リソースと利用条件](references/sources-and-licenses.md)参照。公式サイト上の文章・Markdownの利用には出典表示と加工の明記が必要。FigmaデータはCC BY 4.0、コードスニペットはMIT、Material Symbols等の一部素材は別ライセンス。配布物をデジタル庁公式と誤認させない。
