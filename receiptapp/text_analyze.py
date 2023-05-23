import re

def extract_information(text):
    # 日付の抽出
    date_pattern = r'\d{2}/\d{2}/\d{4}'  # 日付の正規表現パターンを指定
    date_match = re.search(date_pattern, text)
    date = date_match.group() if date_match else ''

    # 商品名と価格の抽出
    items = []
    price_pattern = r'\d+\.\d+'  # 価格の正規表現パターンを指定
    item_lines = text.split('\n')
    for line in item_lines:
        # 行に商品名が含まれている場合に抽出
        if re.search(price_pattern, line):
            item = re.split(price_pattern, line)[0].strip()
            price = re.search(price_pattern, line).group()
            items.append({'item': item, 'price': price})

    return {'date': date, 'items': items}

# テキストのサンプル
text = """
店名: ABC スーパーマーケット
日付: 05/22/2023
------------------------------
商品　　　　　　価格
------------------------------
りんご　　　　　　$1.99
バナナ　　　　　　$0.99
パン　　　　　　　$2.49
------------------------------
合計: $5.47
"""

# レシートの情報を抽出
receipt_info = extract_information(text)
print(receipt_info)
