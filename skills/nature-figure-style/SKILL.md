---
name: nature-figure-style
description: 出版社Natureの公開Figure Guidelinesを参考に、編集可能な論文図版・多パネル科学グラフ・SEM/XPS/XRD/EIS/結晶構造図を制作し、サイズ・DPIを簡易検査する。投稿先の固有規定を最優先し、学会スライド用には可読性を別途最適化する。
metadata:
  version: "0.1.0"
  origin: "assb-lab-original-publisher-research-style"
---

# Nature Figure Style

**出版社公式スキルではない。** Nature本誌のFigure Guide（Nature Portfolio全誌へ一括適用しない）を読み、研究グラフ、論文図版、図中注釈、化学構造を整理する独自のAgent Skill。出版社のロゴ・公式テンプレート・ブランド素材は含めない。

- 公式参照: https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/
- 投稿・図版の厳密な条件は**出版社名だけで決めず、対象誌、記事種別、査読段階を確認する**。出版社の一般規定と個別ジャーナルの条件が異なれば、対象誌の最新版を優先する。
- 参照した寸法や解像度の根拠: [publisher-requirements.md](references/publisher-requirements.md)
- 自動化の範囲: Figureの最終幅とラスター画像の**実効DPI**の簡易チェック。図の意味、全フォント、各画像パネルのDPI、著作権、投稿先への適合性は別途確認が必要。

## 何に使えるか

- 論文Figures、Multi-panel（a/b/c）のXPS/UPS、XRD、EIS、SEM/TEM、Raman、結晶構造図、反応スキーム
- 原データに忠実なmatplotlibスタイルと、投稿先の物理寸法・画像書き出し形式の初期値
- TOC Graphic/Graphical Abstractを作る際の**投稿先規定の確認作業**
- 学会PPTX/HTMLではデータ解釈・構図のみ再利用し、文字サイズと画像配置は投影向けに作り直す

## 出版社特有の注意点

本誌図版は一般の図中文字5–7 pt、パネルラベルは8 ptの太字小文字。標準的なサンセリフ（Arial/Helvetica等）を使い、フォントをアウトライン化せず編集可能にする。

グラフの軸・目盛・単位を必ず表示し、余計なグリッド、影、装飾を避ける。印刷時は1段89 mm／2段183 mm、高さ最大170 mm。写真は最低300 dpi、450 dpiを高品質目標とし、線・文字はベクターで渡す。色はRGB推奨。

結晶構造やスペクトルは元データと単位を保持する。SEM/TEM画像のスケールバーと文字は独立した編集可能レイヤーにする。

Natureの図版本体の規定とカバーデザイン・Research Briefing等の規定を混同しない。Graphical Abstractが必要かは対象誌・記事種別ごとに再確認する。

## 制作の実行手順

1. **必須確認:** 投稿先の正確な誌名、Article Type、初稿/採択後/最終製版、1段/2段幅、図の種類（写真・モノクロ線画・カラー・ベクター）を特定する。曖昧なら図版は暫定版と明記し、提出条件を断定しない。
2. **データ・倫理:** 元の数値、解析・前処理、スケールバー、誤差、n数、校正と出典を保持。不都合なデータの隠蔽、恣意的な画像加工、AIによる測定データ・顕微鏡画像の創作を行わない。
3. **配置:** [figure-workflow.md](references/figure-workflow.md)を参照し、最終印刷幅をmmで決めてから各パネルの比率、共通軸、凡例、a/b/cラベルを整理する。
4. **図表:** `assets/scientific.mplstyle` をスコープ付きで使い、描画時に最終物理サイズを指定する。線/矢印/文字/スケールバーはできる限り編集可能なベクターとして保存する。
5. **書き出し:** PDF/SVGなどの編集可能な原本と、投稿誌の指示に合う最終ファイルを用意。必要に応じて写真を原解像度のまま合成する。
6. **事前チェック:** 対象の**最終印刷サイズ**で、実効DPI・文字・線・パネルの読みやすさを確認する。チェックツールを合格しただけでは投稿適合と呼ばない。

## スタイルと検査

```python
from pathlib import Path
import matplotlib.pyplot as plt

skill = Path("/path/to/installed/nature-figure-style")  # 実際のスキル配置に置換
width_mm, height_mm = 89, 65
with plt.style.context(str(skill / "assets/scientific.mplstyle")):
    fig, ax = plt.subplots(figsize=(width_mm / 25.4, height_mm / 25.4))
    # ax.plot(actual_x, actual_y)  # 必ず実データを使用
    ax.set(xlabel="Potential (V)", ylabel="Current (A)")
    fig.savefig("Figure_1.pdf")
    plt.close(fig)
```

```bash
# PNG等の実効解像度（単一画像の画素を最終図幅に割り付けて概算）
python scripts/preflight.py Figure_1.png --width-mm 89 --kind photo --column single

# スクリプトはPillowがインストールされていればTIFF/JPEG/WebPも検査する
# PDF/SVG内の埋め込みラスター、実寸、フォント・色域・線の検証は別途必要
```

- [figure-presets.json](assets/figure-presets.json) は**公式原本ではなく**、引用した基準の抜粋と独自の制作初期値。
- matplotlibスタイルの配色は**出版社指定色ではない**。色覚多様性への配慮を出発点とし、線種・マーカー・直接ラベルを併用する。
- PDFのベクター部分に「DPI」を強制しない。ラスター画像のDPIは縮尺後の実効値で評価する。

## 学会発表・Web・Node.js

論文用の5–7ptの図中文字をそのまま投影しない。PPTXなら軸ラベル・注記を最低16–20pt程度から検討し、会場の投影距離で実際に確認する。

Node.jsのツール・変換を使う場合、**pnpmがある新規プロジェクトではpnpmを優先**（`pnpm add` / `pnpm run` / `pnpm dlx`）。pnpmがなければnpm。既存のpackageManagerやロックファイルが他のマネージャーを示す場合は、無断変更せず従う。

## 権利と限界

出典は各referenceに掲載。出版社のガイドは許諾なしに全文複製しない。第三者図版は適切な転載許諾とクレジットを確認する。投稿先の最新要件・グラフィカルアブストラクトの制約を最終提出直前に再確認する。
