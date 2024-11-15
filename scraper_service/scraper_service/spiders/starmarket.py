import scrapy


class StarmarketSpider(scrapy.Spider):
    name = "starmarket"
    allowed_domains = ["starmarket.com"]
    start_urls = ["https://starmarket.com"]

    def parse(self, response):
        pass
