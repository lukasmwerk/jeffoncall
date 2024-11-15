import scrapy


class WholefoodsSpider(scrapy.Spider):
    name = "wholefoods"
    allowed_domains = ["wholefoodsmarket.com"]
    start_urls = ["https://wholefoodsmarket.com"]

    def parse(self, response):
        pass
