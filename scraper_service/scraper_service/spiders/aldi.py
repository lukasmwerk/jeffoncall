import scrapy


class AldiSpider(scrapy.Spider):
    name = "aldi"
    allowed_domains = ["aldi.us"]
    start_urls = ["https://aldi.us"]

    def parse(self, response):
        pass
