import scrapy


class WalmartSpider(scrapy.Spider):
    name = "walmart"
    allowed_domains = ["walmart.com"]
    start_urls = ["https://walmart.com"]

    def parse(self, response):
        pass
