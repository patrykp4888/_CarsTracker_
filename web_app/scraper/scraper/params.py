from .searching_data import SearchingData


class UrlParameters:
    URL_BRAND = f"/{SearchingData.BRAND}"
    URL_MODEL = f"/{SearchingData.MODEL}"
    URL_MIN_PRICE = f"?search%5Bfilter_float_price%3Afrom%5D={SearchingData.MIN_PRICE}"
    URL_MAX_PRICE = f"&search%5Bfilter_float_price%3Ato%5D={SearchingData.MAX_PRICE}"
    URL_MIN_PRODUCTION_YEAR = f"/od-{SearchingData.MIN_PRODUCTION_YEAR}"
    URL_MAX_PRODUCTION_YEAR = (
        f"&search%5Bfilter_float_year%3Ato%5D={SearchingData.MAX_PRODUCTION_YEAR}"
    )
    URL_MIN_MILEAGE = (
        f"&search%5Bfilter_float_mileage%3Afrom%5D={SearchingData.MIN_MILEAGE}"
    )
    URL_MAX_MILEAGE = (
        f"&search%5Bfilter_float_mileage%3Ato%5D={SearchingData.MAX_MILEAGE}"
    )
