import scrapy


class CvsSpider(scrapy.Spider):
    name = "cvs"
    allowed_domains = ["cvs.com"]
    start_urls = ["https://cvs.com"]

    def parse(self, response):
        pass
