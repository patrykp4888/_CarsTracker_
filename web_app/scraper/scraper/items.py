# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    NAME = scrapy.Field()
    URL = scrapy.Field()
    # BRAND = scrapy.Field()
    # MODEL = scrapy.Field()
    # PRODUCTION_YEAR = scrapy.Field()
    # MILEAGE = scrapy.Field()
    # PRICE = scrapy.Field()
