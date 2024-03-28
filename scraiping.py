import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://www.lawson.co.jp/recommend/allergy/detail/index.html"
html = requests.get(url) # ページの情報を取得
html.encoding = html.apparent_encoding # 文字コードを自動判定
soup = bs(html.content, 'html.parser') # BeautifulSoupで扱えるようにパースする

soups = soup.find_all(class_="col-4 heightLineParent") # classが"col-4 heightLineParent"の要素を取得

with open("C:/Users/frontier-Python/Desktop/aaa.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for s in soups:
        writer.writerow([s.text.strip()])
