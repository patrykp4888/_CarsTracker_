from dataclasses import dataclass


@dataclass
class SearchingData:
    brand: str = "Ford"
    model: str = "Kuga"
    min_price: str = "0"
    max_price: str = "100000"
    min_production_year: str = "2017"
    max_production_year: str = "2020"
    min_mileage: str = "0"
    max_mileage: str = "150000"
