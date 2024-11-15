import scrapy


class CostcoSpider(scrapy.Spider):
    name = "costco"
    allowed_domains = ["costco.com"]
    start_urls = ["https://costco.com"]

    def parse(self, response):
        pass
