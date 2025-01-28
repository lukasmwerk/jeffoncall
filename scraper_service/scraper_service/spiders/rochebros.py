import scrapy
from typing import List

MAX_PAGES = 38  # Safety guard


# Used for crawling search terms within the store, the default use.
class RochebrosSpider(scrapy.Spider):
    name = "rochebros"
    allowed_domains = ["rochebros.com"]
    start_urls = ["https://shopping.rochebros.com/shop/categories?tags=on_sale&page=1"]
    
    def parse(self, response):
        ol_elements = response.css("body div.sidecart-padding").getall()
        # Parse items on the current page
        for product in ol_elements.css("ol.cell-container"):  # Adjust CSS selector
            print(div.cell-content-wrapper > button::text)
            # yield {
            #     "name": product.css("li.div.product-name::text").get(),
            #     "price": product.css("span.product-price::text").get(),
            #     "url": response.urljoin(product.css("a.product-link::attr(href)").get()),
            # }


        # OR Incrementing the Page Manually
        current_page = int(response.url.split("page=")[-1])  # Extract the current page number
        if current_page < MAX_PAGES:
            print(f"page {current_page + 1}")
            next_page_url = f"https://shopping.rochebros.com/shop/categories?tags=on_sale&page={current_page + 1}"
            yield scrapy.Request(next_page_url, callback=self.parse)
