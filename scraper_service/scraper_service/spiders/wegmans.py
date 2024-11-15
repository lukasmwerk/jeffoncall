import scrapy


class WegmansSpider(scrapy.Spider):
    name = "wegmans"
    allowed_domains = ["wegmans.com"]
    start_urls = ["https://wegmans.com"]

    def parse(self, response):
        pass
