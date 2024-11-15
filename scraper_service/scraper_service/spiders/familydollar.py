import scrapy


class FamilydollarSpider(scrapy.Spider):
    name = "familydollar"
    allowed_domains = ["familydollar.com"]
    start_urls = ["https://familydollar.com"]

    def parse(self, response):
        pass
