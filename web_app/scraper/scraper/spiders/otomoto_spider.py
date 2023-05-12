import scrapy

from ..params import UrlParameters


class OtomotoSpider(scrapy.Spider):
    name = "otomoto_spider"
    allowed_domains = ["otomoto.pl"]
    start_urls = [
        f"https://www.otomoto.pl/osobowe{UrlParameters.URL_BRAND}{UrlParameters.URL_MODEL}{UrlParameters.URL_MIN_PRODUCTION_YEAR}{UrlParameters.URL_MIN_PRICE}{UrlParameters.URL_MAX_PRICE}{UrlParameters.URL_MAX_PRODUCTION_YEAR}{UrlParameters.URL_MIN_MILEAGE}{UrlParameters.URL_MAX_MILEAGE}"
    ]

    def parse(self, response):
        cars = response.css("article.ooa-dmrg7i")

        for car in cars:
            yield {
                "title": car.css(".ooa-10p8u4x a::text").get(),
                "prod_year": car.css("li.ooa-1k7nwcr.e19ivbs0::text").get(),
                # "mileage": car.css("li.ooa-1k7nwcr.e19ivbs0::text").get(),
                "price": car.css("span.ooa-1bmnxg7.evg565y11::text").get(),
                "url": car.css(".ooa-10p8u4x a").attrib["href"],
            }
