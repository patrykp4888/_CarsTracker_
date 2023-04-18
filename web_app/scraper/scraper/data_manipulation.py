from .user_interaction import UserInteraction


class DataManipulation:
    def __init__(self):
        self.data_dict = UserInteraction.choose_cars_to_track()

        self.brand = self.data_dict["brand"]
        self.model = self.data_dict["model"]
        self.min_price = self.data_dict["min_price"]
        self.max_price = self.data_dict["max_price"]
        self.min_production_year = self.data_dict["min_production_year"]
        self.max_production_year = self.data_dict["max_production_year"]
        self.min_mileage = self.data_dict["min_mileage"]
        self.max_mileage = self.data_dict["max_mileage"]
