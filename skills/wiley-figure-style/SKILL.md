---
name: wiley-figure-style
description: 出版社Wileyの公開Figure Guidelinesを参考に、編集可能な論文図版・多パネル科学グラフ・SEM/XPS/XRD/EIS/結晶構造図を制作し、サイズ・DPIを簡易検査する。投稿先の固有規定を最優先し、学会スライド用には可読性を別途最適化する。
metadata:
  version: "0.1.0"
  origin: "assb-lab-original-publisher-research-style"
---

# Wiley Figure Style

**出版社公式スキルではない。** Wiley Author Servicesの一般的Figure Preparation Guide（Advanced Materials等は各誌の現行規定を優先）を読み、研究グラフ、論文図版、図中注釈、化学構造を整理する独自のAgent Skill。出版社のロゴ・公式テンプレート・ブランド素材は含めない。

- 公式参照: https://authorservices-ppd.wiley.com/author-resources/Journal-Authors/Prepare/manuscript-preparation-guidelines.html/figure-preparation.html
- 投稿・図版の厳密な条件は**出版社名だけで決めず、対象誌、記事種別、査読段階を確認する**。出版社の一般規定と個別ジャーナルの条件が異なれば、対象誌の最新版を優先する。
- 参照した寸法や解像度の根拠: [publisher-requirements.md](references/publisher-requirements.md)
- 自動化の範囲: Figureの最終幅とラスター画像の**実効DPI**の簡易チェック。図の意味、全フォント、各画像パネルのDPI、著作権、投稿先への適合性は別途確認が必要。

## 何に使えるか

- 論文Figures、Multi-panel（a/b/c）のXPS/UPS、XRD、EIS、SEM/TEM、Raman、結晶構造図、反応スキーム
- 原データに忠実なmatplotlibスタイルと、投稿先の物理寸法・画像書き出し形式の初期値
- TOC Graphic/Graphical Abstractを作る際の**投稿先規定の確認作業**
- 学会PPTX/HTMLではデータ解釈・構図のみ再利用し、文字サイズと画像配置は投影向けに作り直す

## 出版社特有の注意点

Wileyの一般的な図版ガイドは画像の最終判読性を重視。図中文字の統一書体、キャプション分離、引用順、元ファイルの保管が大切。8 ptは本スキルの開始値で、Wiley全誌の規定ではない。

推奨幅80–180 mm、個別ファイル10 MB未満。線画はPDF/EPSが推奨、ラスターなら600 dpi、写真/画像は300 dpiでPNG/TIFF等。初回査読と採択後に認められる形式は変わる。

XPS、EIS、結晶構造、SEMなど異なる画像を同一figureに組む場合は、画像パネルのみ元画素を保持して周囲の文字・線画はベクターで統合。混合図の出力形式も投稿先の詳細指示を優先する。

Graphical Abstract・Cover Art・TOC Graphicの要否・アスペクト比・提出先はAdvanced Materialsなど個別誌のAuthor Guidelinesを確認。一般ガイドの80–180 mmを全GAに流用しない。

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

skill = Path("/path/to/installed/wiley-figure-style")  # 実際のスキル配置に置換
width_mm, height_mm = 80, 65
with plt.style.context(str(skill / "assets/scientific.mplstyle")):
    fig, ax = plt.subplots(figsize=(width_mm / 25.4, height_mm / 25.4))
    # ax.plot(actual_x, actual_y)  # 必ず実データを使用
    ax.set(xlabel="Potential (V)", ylabel="Current (A)")
    fig.savefig("Figure_1.pdf")
    plt.close(fig)
```

```bash
# PNG等の実効解像度（単一画像の画素を最終図幅に割り付けて概算）
python scripts/preflight.py Figure_1.png --width-mm 80 --kind photo

# スクリプトはPillowがインストールされていればTIFF/JPEG/WebPも検査する
# PDF/SVG内の埋め込みラスター、実寸、フォント・色域・線の検証は別途必要
```

- [figure-presets.json](assets/figure-presets.json) は**公式原本ではなく**、引用した基準の抜粋と独自の制作初期値。
- matplotlibスタイルの配色は**出版社指定色ではない**。色覚多様性への配慮を出発点とし、線種・マーカー・直接ラベルを併用する。
- PDFのベクター部分に「DPI」を強制しない。ラスター画像のDPIは縮尺後の実効値で評価する。

## 学会発表・Web・Node.js

論文向けの小さな文字・少ない余白をそのままPPTXにコピーしない。文字・パネル比率を投影向けに作り直す。

Node.jsのツール・変換を使う場合、**pnpmがある新規プロジェクトではpnpmを優先**（`pnpm add` / `pnpm run` / `pnpm dlx`）。pnpmがなければnpm。既存のpackageManagerやロックファイルが他のマネージャーを示す場合は、無断変更せず従う。

## 権利と限界

出典は各referenceに掲載。出版社のガイドは許諾なしに全文複製しない。第三者図版は適切な転載許諾とクレジットを確認する。投稿先の最新要件・グラフィカルアブストラクトの制約を最終提出直前に再確認する。
