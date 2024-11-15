import scrapy


class ShawsSpider(scrapy.Spider):
    name = "shaws"
    allowed_domains = ["shaws.com"]
    start_urls = ["https://shaws.com"]

    def parse(self, response):
        pass
