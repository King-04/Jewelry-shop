# app.py

from flask import Flask, render_template
from models import db, Jewelry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry.db'
db.init_app(app)
