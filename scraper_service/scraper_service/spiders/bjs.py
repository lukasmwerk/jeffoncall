import scrapy


class BjsSpider(scrapy.Spider):
    name = "bjs"
    allowed_domains = ["bjs.com"]
    start_urls = ["https://bjs.com"]

    def parse(self, response):
        pass
