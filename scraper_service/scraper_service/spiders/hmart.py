import scrapy


class HmartSpider(scrapy.Spider):
    name = "hmart"
    allowed_domains = ["hmart.com"]
    start_urls = ["https://hmart.com"]

    def parse(self, response):
        pass
