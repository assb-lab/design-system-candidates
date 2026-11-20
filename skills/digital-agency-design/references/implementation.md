# Node.js / CSS / Tailwind / React / HTML 実装

## pnpm優先ルール

既存の `package.json` の `packageManager` とロックファイルを先に調べる。既存のnpm/Yarn/Bun指定を無断で上書きしない。指定がなければ `command -v pnpm` で利用可能か確認し、**pnpmがあるなら優先**する。

| 操作 | pnpmが利用可能な場合 | pnpmがない場合 |
| --- | --- | --- |
| Agent Skill導入 | `pnpm dlx skills add assb-lab/design-system-candidates --skill digital-agency-design` | `npx skills add assb-lab/design-system-candidates --skill digital-agency-design` |
| DADSトークン | `pnpm add @digital-go-jp/design-tokens` | `npm install @digital-go-jp/design-tokens` |
| Tailwindプラグイン | `pnpm add @digital-go-jp/tailwind-theme-plugin` | `npm install @digital-go-jp/tailwind-theme-plugin` |
| テスト/ビルド | `pnpm run test` / `pnpm run build` | `npm run test` / `npm run build` |

`npx` に相当する一時実行は `pnpm dlx`。`pnpm skills` とは書かない。

## CSSデザイントークン

公式: https://github.com/digital-go-jp/design-tokens

CSS向けの `tokens.css`（全トークン）と `tokens-simple.css`（簡易版）を提供している。例えば新規pnpmプロジェクトでは：

```bash
pnpm add @digital-go-jp/design-tokens
```

バンドラーを使う場合は、プロジェクトへコピーしたこのスキルの `tokens.css` よりも先に、公式トークンを読み込む：

```ts
import "@digital-go-jp/design-tokens/dist/tokens.css";
import "./design/digital-agency/tokens.css";
```

`./design/digital-agency/tokens.css` はこのスキルの `assets/tokens.css` を配置した**例示パス**。別の場所にコピーする場合は修正する。CSS変数は公式配布パッケージから取得する。素のHTMLでは `node_modules` の裸のパスをブラウザーへ渡さず、適切にビルド・配信する。

## Tailwind CSS

公式: https://github.com/digital-go-jp/tailwind-theme-plugin

```bash
pnpm add @digital-go-jp/tailwind-theme-plugin
```

Tailwind CSS **v3** は `tailwind.config.js`（CommonJSの一例）にプラグインを追加：

```js
module.exports = {
  content: ["./index.html", "./src/**/*.{ts,tsx,js,jsx}"],
  theme: { extend: {} },
  plugins: [require("@digital-go-jp/tailwind-theme-plugin")],
};
```

Tailwind CSS **v4** の場合は公式が提示するCSSエントリー方式：

```css
@import "tailwindcss";
@import "@digital-go-jp/tailwind-theme-plugin/v4";
```

Tailwind v3とv4は仕様が異なる。パッケージの最新版/移行ガイドと既存プロジェクトの設定を先に確認する。

## 公式コンポーネントの利用

- Reactサンプル: https://github.com/digital-go-jp/design-system-example-components-react
- HTMLサンプル: https://github.com/digital-go-jp/design-system-example-components-html
- React Storybook: https://design.digital.go.jp/dads/react/
- HTML Storybook: https://design.digital.go.jp/dads/html/

Reactサンプルは **React 19、Tailwind CSS 3、TypeScript** が前提。React 18では `forwardRef` やhooksの型の修正が必要な場合がある（公式READMEの案内を参照）。HTML版はサンプルのCSS、JS、依存関係をHTML版マニフェストから確認する。

**公式コンポーネントは完成品アプリのUIライブラリとして動作保証されるものではなく、設計・実装のサンプルである。** 状態管理、API、科学データの検証はプロジェクト側で行う。移植時はARIA、focus-visible、強制カラーモードの対応を削除しない。

## 検査

ロックファイルを勝手に二重化しない。React型検査・コンポーネントの対話テスト・キーボード操作・狭幅・ズーム・強制カラー・コントラスト・エラー表示・読み上げテストを行い、確認方法と未確認事項を明示する。
