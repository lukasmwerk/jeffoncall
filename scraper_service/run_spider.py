from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper_service.spiders.rochebros import RochebrosSpider  # Replace with your spider import

if __name__ == "__main__":
    product_urls = ["https://shopping.rochebros.com/product/1873584/wholly-guacamole-100-cal-snack-packs-4-count"]
    search_terms = []

    process = CrawlerProcess(get_project_settings())
    process.crawl(RochebrosSpider)
    process.start()
