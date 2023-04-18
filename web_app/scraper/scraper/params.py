from .data_manipulation import DataManipulation


class UrlParameters:
    data_manipulation = DataManipulation()

    URL_BRAND = f"/{data_manipulation.brand}"
    URL_MODEL = f"/{data_manipulation.model}"
    URL_MIN_PRICE = (
        f"?search%5Bfilter_float_price%3Afrom%5D={data_manipulation.min_price}"
    )
    URL_MAX_PRICE = (
        f"&search%5Bfilter_float_price%3Ato%5D={data_manipulation.max_price}"
    )
    URL_MIN_PRODUCTION_YEAR = f"/od-{data_manipulation.min_production_year}"
    URL_MAX_PRODUCTION_YEAR = (
        f"&search%5Bfilter_float_year%3Ato%5D={data_manipulation.max_production_year}"
    )
    URL_MIN_MILEAGE = (
        f"&search%5Bfilter_float_mileage%3Afrom%5D={data_manipulation.min_mileage}"
    )
    URL_MAX_MILEAGE = (
        f"&search%5Bfilter_float_mileage%3Ato%5D={data_manipulation.max_mileage}"
    )
