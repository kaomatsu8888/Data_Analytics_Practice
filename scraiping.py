from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# chromedriverのパスを指定
driver_path = "/path/to/your/chromedriver"
chrome_service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)

# ローソンの商品情報ページへアクセス
url = "https://www.lawson.co.jp/recommend/allergy/detail/index.html"
driver.get(url)

# ここで適切なセレクターを使って商品情報を取得
# 例えば、商品名、タンパク質、カロリーの情報を含む要素を指定する
# 以下のセレクターは仮のものなので、実際のページの構造に合わせて変更してください。
products = driver.find_elements(By.CSS_SELECTOR, 'div.product_info')

for product in products:
    # 商品名、タンパク質、カロリーの情報を抽出
    name = product.find_element(By.CSS_SELECTOR, 'p.product_name').text
    protein = product.find_element(By.CSS_SELECTOR, 'span.protein_content').text
    calories = product.find_element(By.CSS_SELECTOR, 'span.calories_content').text
    print(name, protein, calories)

# ブラウザを閉じる
driver.quit()
