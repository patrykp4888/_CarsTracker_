from celery import Celery
from scrapy.crawler import CrawlerProcess

from scraper.spiders.otomoto_spider import OtomotoSpider
from scraper.params import UrlParameters
from scraper.searching_data import SearchingData
from web.config import Config

celery_app = Celery(
    "scraper", broker=Config.CELERY_BROKER, backend=Config.CELERY_BACKEND
)


@celery_app.task
def scraping_task(params):
    searching_data = SearchingData(**params)
    prepared_params = UrlParameters.produce_params(searching_data)

    URI = f"https://www.otomoto.pl/osobowe{prepared_params['url_brand']}{prepared_params['url_model']}{prepared_params['url_min_production_year']}{prepared_params['url_min_price']}{prepared_params['url_max_price']}{prepared_params['url_max_production_year']}{prepared_params['url_min_mileage']}{prepared_params['url_max_mileage']}"

    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        }
    )
    process.crawl(
        OtomotoSpider,
        my_urls=[
            URI,
        ],
    )
    process.start()
