The scraper service grabs grocery data from local stores and adds them to time series databases. Since the app is designed to be used by a small user-base, the scrapers only access items that are included in user profiles. 

Staple items are tracked on a weekly basis, as most price changes in supermarkets occur on a weekly basis. Wishlist items are tracked until the item leaves the wishlist. 

This results in a few hundred items being queried weekly rather than all item pages on a website. Since many items overlap, we end up with (including throttling and other delays) a few minutes of processing per week on the first day of each grocery store's price updates. Optimizations and further processing of this time-series price data is handled by other services later in the pipeline.

The scrapers are implemented using scrapy spiders.