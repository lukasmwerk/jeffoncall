import scrapy


class TraderjoesSpider(scrapy.Spider):
    name = "traderjoes"
    allowed_domains = ["traderjoes.com"]
    start_urls = ["https://traderjoes.com"]

    def parse(self, response):
        pass
