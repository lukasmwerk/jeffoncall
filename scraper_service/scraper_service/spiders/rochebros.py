import scrapy


class RochebrosSpider(scrapy.Spider):
    name = "rochebros"
    allowed_domains = ["rochebros.com"]
    start_urls = ["https://rochebros.com/weekly-add/"]

    def parse(self, response):
        pass
