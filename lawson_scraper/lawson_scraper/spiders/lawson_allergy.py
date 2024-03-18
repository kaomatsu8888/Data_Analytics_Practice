import scrapy
import json

class LawsonAllergySpider(scrapy.Spider):
    name = 'lawson_allergy'
    allowed_domains = ['www.lawson.co.jp']
    start_urls = ['https://www.lawson.co.jp/recommend/allergy/detail/index.html']

    def start_requests(self):
        url = 'https://www.lawson.co.jp/recommend/allergy/result.js'
        # 例としてアレルギー品目「卵」を指定
        data = {'allergyItems': '3'}
        yield scrapy.FormRequest(url, formdata=data, callback=self.parse)

    def parse(self, response):
        # JSON形式のレスポンスをデコード
        products = json.loads(response.text)

        # 商品情報を抽出
        for product in products:
            yield {
                'product_number': product.get('pdctNo'),
                'product_name': product.get('pdctNm'),
                'allergy_summary': product.get('allergyItemSumry'),
            }
