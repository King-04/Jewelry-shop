# app.py

from flask import Flask, render_template
from models import db, Jewelry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry.db'
db.init_app(app)

@app.route('/')
def index():
    # Fetch some example jewelry items from the database
    jewelry_items = Jewelry.query.all()
    return render_template('index.html', jewelry_items=jewelry_items)

if __name__ == '__main__':
    app.run(debug=True)
