from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    store = db.relationship('StoreModel', back_populates='items')
    tags = db.relationship('TagModel', back_populates='items', secondary='items_tags')
