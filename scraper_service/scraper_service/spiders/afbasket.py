import scrapy


class AfbasketSpider(scrapy.Spider):
    name = "afbasket"
    allowed_domains = ["afbasket.com"]
    start_urls = ["https://afbasket.com"]

    def parse(self, response):
        pass
