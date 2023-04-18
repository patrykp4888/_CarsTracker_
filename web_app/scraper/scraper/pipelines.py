from sqlalchemy.orm import sessionmaker

from web_app.app import db
from web_app.app.models.offers import Offers


class PostgreSQLPipeline:
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
        self.session = None

    def process_item(self, item):
        self.session = self.Session()
        offer = Offers(name=item["NAME"], url=item["URL"])
        self.session.add(offer)
        self.session.commit()
        return item
