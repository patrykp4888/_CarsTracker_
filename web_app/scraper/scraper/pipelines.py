import psycopg2


class PostgreSQLPipeline:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = psycopg2.connect(
            host="db", database="cars_tracker", user="postgres", password="postgres"
        )

        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        try:
            self.cursor.execute(
                """
                INSERT INTO "ScrapedCarsData" (title, prod_year, price, url) values (%s, %s,%s, %s)""",
                (item["title"], item["prod_year"], item["price"], item["url"]),
            )
        except BaseException as e:
            print(e)
        else:
            self.connection.commit()
