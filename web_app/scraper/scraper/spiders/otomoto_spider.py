import scrapy

from ..params import UrlParameters
from ..items import ScraperItem


class OtomotoSpider(scrapy.Spider):
    name = "otomoto_spider"

    start_urls = [
        f"https://www.otomoto.pl/osobowe\
            {UrlParameters.URL_BRAND}{UrlParameters.URL_MODEL}\
            {UrlParameters.URL_MIN_PRODUCTION_YEAR}{UrlParameters.URL_MIN_PRICE}\
            {UrlParameters.URL_MAX_PRICE}{UrlParameters.URL_MAX_PRODUCTION_YEAR}\
            {UrlParameters.URL_MIN_MILEAGE}{UrlParameters.URL_MAX_MILEAGE}"
    ]

    def parse(self, response):
        items = ScraperItem()

        NAME = response.css(".ooa-10p8u4x a::text").extract()
        URL = response.css(".ooa-10p8u4x a::attr(href)").extract()
        pagination_count = response.css(".e8b33l72::text").extract()
        print(pagination_count)

        items["NAME"] = NAME
        items["URL"] = URL

        yield items
