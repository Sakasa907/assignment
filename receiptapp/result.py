from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    # エクセルデータを読み込み
    df = pd.read_excel('receipt_data.xlsx')

    # HTMLテーブルに変換
    html_table = df.to_html(index=False, classes='table table-striped')

    return render_template('result.html', table=html_table)

if __name__ == '__main__':
    app.run()
