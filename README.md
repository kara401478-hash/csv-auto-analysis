# CSV自動集計・グラフ出力ツール

CSVファイルを読み込み、自動で集計してグラフを出力するツールです。

## 機能
- CSVファイルの自動読み込み
- 数値データの集計（合計・平均・最大・最小）
- グラフの自動生成・保存（棒グラフ・折れ線グラフ）

## 使用技術
- Python 3.x
- pandas
- matplotlib

## 使い方
1. リポジトリをクローン
2. 必要なライブラリをインストール
```bash
pip install pandas matplotlib
```
3. CSVファイルをdataフォルダに配置
4. スクリプトを実行
```bash
python main.py
```

## 出力例
- `output/summary.csv` - 集計結果
- `output/graph.png` - グラフ画像
