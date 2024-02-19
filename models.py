# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jewelry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image_url = db.Column(db.String(200))

    def __repr__(self):
        return f"<Jewelry {self.name}>"
