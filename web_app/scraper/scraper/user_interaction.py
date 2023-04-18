class UserInteraction:
    def choose_cars_to_track():
        brand = str(input("Brand: "))
        model = str(input("Model: "))
        min_price = str(input("Minimal price: "))
        max_price = str(input("Maximal price: "))
        min_production_year = str(input("Minimal production year: "))
        max_production_year = str(input("Maximal production year: "))
        min_mileage = str(input("Minimal mileage: "))
        max_mileage = str(input("Maximal mileage: "))

        data_dict = {
            "brand": brand,
            "model": model,
            "min_price": min_price,
            "max_price": max_price,
            "min_production_year": min_production_year,
            "max_production_year": max_production_year,
            "min_mileage": min_mileage,
            "max_mileage": max_mileage,
        }
        return data_dict
