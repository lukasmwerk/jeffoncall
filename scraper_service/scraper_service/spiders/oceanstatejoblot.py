import scrapy


class OceanstatejoblotSpider(scrapy.Spider):
    name = "oceanstatejoblot"
    allowed_domains = ["oceanstatejoblot.com"]
    start_urls = ["https://oceanstatejoblot.com"]

    def parse(self, response):
        pass
