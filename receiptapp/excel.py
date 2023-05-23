import pandas as pd
from openpyxl import Workbook

def convert_to_excel(data):
    # データをDataFrameに変換
    df = pd.DataFrame(data['items'])

    # エクセルファイルを作成し、データを書き込む
    workbook = Workbook()
    sheet = workbook.active

    # カラム名を設定
    sheet['A1'] = '商品名'
    sheet['B1'] = '価格'

    # データを書き込む
    for i, row in df.iterrows():
        sheet[f'A{i+2}'] = row['item']
        sheet[f'B{i+2}'] = row['price']

    # ファイルを保存
    filename = 'receipt_data.xlsx'
    workbook.save(filename)

    return filename

# レシートの情報（サンプルデータ）
data = {
    'date': '05/22/2023',
    'items': [
        {'item': 'りんご', 'price': '1.99'},
        {'item': 'バナナ', 'price': '0.99'},
        {'item': 'パン', 'price': '2.49'}
    ]
}

# データをエクセル形式に変換
excel_file = convert_to_excel(data)
print('エクセルファイルが作成されました:', excel_file)
