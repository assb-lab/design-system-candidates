# Springer Nature Elements — 導入ガイド

## 公式パッケージと実装の位置づけ

公式: https://eds.springernature.com/get-started/

ElementsはSassを含むWeb向けコンポーネント設計で、Springer Nature/Natureのテーマを選択できる。公式サイトの例ではHandlebarsテンプレート、SCSS、JavaScriptを使用し、**React向けの完成コンポーネントライブラリとは異なる**。

公式ページは最低 Node.js 18.14.0、npm 7、Dart Sass を案内しているが、利用者のプロジェクトとnpmパッケージの現行版を確認する。

## pnpm優先

新規Node.jsプロジェクトでpnpmが利用できれば次を優先：

```bash
pnpm add @springernature/elements
pnpm add -D sass
```

pnpmがなければ `npm install @springernature/elements`、`npm install --save-dev sass`。ただし既存の `packageManager` 設定や `package-lock.json` / `yarn.lock` / `bun.lock*` が別のマネージャーを示す場合は**それを維持**する。

### 公式のSCSS構成例

以下は[公式get-started](https://eds.springernature.com/get-started/)に載っているテーマの**パス**を示す参考。プロジェクト内のSassインポート位置やnode_modulesの解決方法はビルドツールに合わせて調整し、パッケージに実際に存在するか確認してから使う。

```text
@springernature/elements/
  themes/nature/scss/core.scss
  themes/nature/scss/enhanced.scss
  themes/springernature/scss/core.scss
  themes/springernature/scss/enhanced.scss
  components/.../scss/...scss
```

- Natureを使うWeb UIならNatureテーマ、Springer Nature向けならSpringer Natureテーマを選ぶ。両者を無条件に混在させない。
- Core/Enhancedのどちらが必要か、依存するコンポーネントとCSSの順序を公式で確認。
- コンポーネントのテンプレートはHandlebarsが使われる。Reactコンポーネントと同じAPIがあると想定しない。
- `pnpm dlx skills add assb-lab/design-system-candidates --skill springer-nature-elements` は**Agent Skillのみ**を入れる。公式npmパッケージを自動導入しない。

## React/Next.jsで使うとき

公式サンプルをそのままReact JSXとして貼るのではなく、HTML出力とアニメーション・キーボード操作・JavaScript初期化の依存関係を把握したうえで適切にラップする。既存のアクセシブルなUIライブラリがある場合は、Elementsの情報設計・色・タイプスケールのみ採用する選択肢もある。

## 事前検査

- 公式デザイン／独自参考スタイルの違いをREADME等に記載する。
- 無断で公式Harding/GraphikフォントやSpringer Nature/Natureロゴを配布しない。
- 公式のSass/JSが古い環境向けの場合、現行のバージョンに合わせたパッチを行い、差分とライセンス条件を記録する。
- ブラウザ実機とキーボード、支援技術、狭幅、ズームで確認する。
