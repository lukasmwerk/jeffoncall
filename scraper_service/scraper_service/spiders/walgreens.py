import scrapy


class WalgreensSpider(scrapy.Spider):
    name = "walgreens"
    allowed_domains = ["walgreens.com"]
    start_urls = ["https://walgreens.com"]

    def parse(self, response):
        pass
