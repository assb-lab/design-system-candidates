# 基本デザインとアクセシビリティ

出典：デジタル庁デザインシステム https://design.digital.go.jp/dads/ を参考にassb-labが独自に要約。

| 領域 | 採用する方針 | 公式 |
| --- | --- | --- |
| 色 | キーカラーと意味色を分離し、ローカルブランドに合わせて調整。コントラストは再計算する | https://design.digital.go.jp/dads/foundations/color/ |
| 文字 | 日本語本文・UIは16 CSS px以上を基準、読み物は行高1.5倍以上 | https://design.digital.go.jp/dads/foundations/typography/ |
| 余白 | 規則的な余白スケールで意味的グループを表現。空白文字をレイアウトに使わない | https://design.digital.go.jp/dads/foundations/spacing/ |
| レイアウト | リキッドレイアウトと一貫したDOM順、横幅の変化に追従 | https://design.digital.go.jp/dads/foundations/layout/ |
| リンク | 下線等も使い、色だけでリンクを判別させない | https://design.digital.go.jp/dads/foundations/link-text/ |
| アイコン | 必要ならラベル・代替テキストを伴わせる | https://design.digital.go.jp/dads/foundations/icon/ |
| ローカル化 | ブランド、トークン、コンポーネント、状態のルールを導入先用に定義する | https://design.digital.go.jp/dads/guidance/local-design-system/ |

## 改変しても守るチェックリスト

- [ ] 通常の文字：4.5:1以上のコントラスト。意味を持つ非テキスト要素・境界：3:1以上。
- [ ] 本文・UIは16 CSS px以上を基準。読み物の本文行高は1.5倍以上。
- [ ] インタラクティブ要素の操作対象は44 CSS px以上を基準。
- [ ] 黒・黄色の二重フォーカスインジケーターを改変せず、キーボードから確認できる。
- [ ] 強制カラーモードでも入力の枠・状態・フォーカスを判別できる。
- [ ] ラベル、必須表示、説明文、エラーの理由・復旧策を表示する。
- [ ] 意味色は文字やアイコンでも伝え、色のみに依存しない。
- [ ] リンクは下線等で認知でき、タブ操作も可能。
- [ ] 見た目の順序と読み上げ順が一致し、ズームや狭幅でも機能を失わない。

公式の個別コンポーネントの注意点・JIS X 8341-3:2016 / WCAG 2.2の対象要件は、各コンポーネントページで参照する。
https://design.digital.go.jp/dads/guidance/accessibility/

## Science Tokyo等のブランドへの応用

組織のロゴ・キーカラー・正式表記は公式ブランド規定を優先。DADSのキーカラー階調を上書きしても、hover/active、文字・背景、意味色、フォーカスの可読性を独立に検証する。ブランド色のHEXを一括置換するだけで完成とはしない。
