import scrapy


class StopandshopSpider(scrapy.Spider):
    name = "stopandshop"
    allowed_domains = ["stopandshop.com"]
    start_urls = ["https://stopandshop.com"]

    def parse(self, response):
        pass
