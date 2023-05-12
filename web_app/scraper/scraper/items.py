import scrapy


class ScraperItem(scrapy.Item):
    title = scrapy.Field()
    prod_year = scrapy.Field()
    # mileage = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
