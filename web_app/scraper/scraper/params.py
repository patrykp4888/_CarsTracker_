from .searching_data import SearchingData


class UrlParameters:
    @staticmethod
    def produce_params(searching_data: SearchingData):
        URL_BRAND = f"/{searching_data.brand}"
        URL_MODEL = f"/{searching_data.model}"
        URL_MIN_PRICE = (
            f"?search%5Bfilter_float_price%3Afrom%5D={searching_data.min_price}"
        )
        URL_MAX_PRICE = (
            f"&search%5Bfilter_float_price%3Ato%5D={searching_data.max_price}"
        )
        URL_MIN_PRODUCTION_YEAR = f"/od-{searching_data.min_production_year}"
        URL_MAX_PRODUCTION_YEAR = (
            f"&search%5Bfilter_float_year%3Ato%5D={searching_data.max_production_year}"
        )
        URL_MIN_MILEAGE = (
            f"&search%5Bfilter_float_mileage%3Afrom%5D={searching_data.min_mileage}"
        )
        URL_MAX_MILEAGE = (
            f"&search%5Bfilter_float_mileage%3Ato%5D={searching_data.max_mileage}"
        )

        return {
            "url_brand": URL_BRAND,
            "url_model": URL_MODEL,
            "url_min_price": URL_MIN_PRICE,
            "url_max_price": URL_MAX_PRICE,
            "url_min_production_year": URL_MIN_PRODUCTION_YEAR,
            "url_max_production_year": URL_MAX_PRODUCTION_YEAR,
            "url_min_mileage": URL_MIN_MILEAGE,
            "url_max_mileage": URL_MAX_MILEAGE,
        }
