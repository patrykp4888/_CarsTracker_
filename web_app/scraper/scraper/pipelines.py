import psycopg2


class PostgreSQLPipeline:
    def __init__(self):
        hostname = "db"
        username = "postgres"
        password = "postgres"
        database = "cars_tracker"
        port = "5432"

        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database, port=port
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """INSERT INTO Offers (name, url) values (%s, %s)""",
            (item[NAME], item[URL]),
        )
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
