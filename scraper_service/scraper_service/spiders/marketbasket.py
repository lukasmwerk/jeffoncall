import scrapy


class MarketbasketSpider(scrapy.Spider):
    name = "marketbasket"
    allowed_domains = ["shopmarketbasket.com"]
    start_urls = ["https://shopmarketbasket.com"]

    def parse(self, response):
        pass
