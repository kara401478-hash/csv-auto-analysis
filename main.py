import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(filepath):
    """CSVファイルを読み込む"""
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        print(f"✅ CSVファイルを読み込みました: {filepath}")
        return df
    except Exception as e:
        print(f"❌ 読み込みエラー: {e}")
        return None

def analyze(df):
    """数値データを集計する"""
    print("\n📊 集計結果")
    print("=" * 40)
    numeric_cols = df.select_dtypes(include='number')
    summary = numeric_cols.agg(['sum', 'mean', 'max', 'min'])
    print(summary)
    return summary

def plot_graph(df, output_dir):
    """グラフを生成して保存する"""
    os.makedirs(output_dir, exist_ok=True)
    numeric_cols = df.select_dtypes(include='number')

    # 棒グラフ
    ax = numeric_cols.mean().plot(kind='bar', color='steelblue', figsize=(10, 5))
    plt.title('平均値 棒グラフ')
    plt.ylabel('値')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/bar_graph.png")
    plt.close()
    print(f"✅ 棒グラフを保存しました: {output_dir}/bar_graph.png")

    # 折れ線グラフ
    numeric_cols.plot(kind='line', figsize=(10, 5))
    plt.title('折れ線グラフ')
    plt.ylabel('値')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/line_graph.png")
    plt.close()
    print(f"✅ 折れ線グラフを保存しました: {output_dir}/line_graph.png")

def save_summary(summary, output_dir):
    """集計結果をCSVに保存する"""
    os.makedirs(output_dir, exist_ok=True)
    summary.to_csv(f"{output_dir}/summary.csv")
    print(f"✅ 集計結果を保存しました: {output_dir}/summary.csv")

def main():
    # サンプルCSVを生成
    sample_data = {
        '月': ['1月', '2月', '3月', '4月', '5月', '6月'],
        '売上': [150000, 180000, 210000, 195000, 220000, 250000],
        '経費': [80000, 90000, 95000, 88000, 100000, 110000],
        '利益': [70000, 90000, 115000, 107000, 120000, 140000]
    }
    os.makedirs('data', exist_ok=True)
    df_sample = pd.DataFrame(sample_data)
    df_sample.to_csv('data/sample.csv', index=False, encoding='utf-8')
    print("✅ サンプルCSVを生成しました: data/sample.csv")

    # メイン処理
    df = load_csv('data/sample.csv')
    if df is not None:
        summary = analyze(df)
        plot_graph(df, 'output')
        save_summary(summary, 'output')
        print("\n🎉 完了！outputフォルダを確認してください。")

if __name__ == "__main__":
    main()
