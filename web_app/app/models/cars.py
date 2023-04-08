from app import db


class Brands(db.Model):
    __tablename__ = "Brands"

    brand_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)

    models = db.relationship("Models", backref="brand")


class Models(db.Model):
    __tablename__ = "Models"

    model_id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(120), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey("Brands.brand_id"))


