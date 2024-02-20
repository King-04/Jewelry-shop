# app.py

from flask import Flask, render_template
from models import db, Jewelry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry.db'
db.init_app(app)

# Function to clear the database tables
def clear_tables():
    with app.app_context():
        db.drop_all()
        db.create_all()

# Function to add sample jewelry items to the database
def add_sample_data():
    with app.app_context():
        # Check if items already exist
        existing_items = Jewelry.query.all()
        if not existing_items:
            # Add sample jewelry items
            items = [
                Jewelry(name='Diamond Ring', description='Elegant diamond ring', price=999.99, image_url='https://images.unsplash.com/photo-1589674668791-4889d2bba4c6?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
                Jewelry(name='Sapphire Necklace', description='Beautiful sapphire necklace', price=1299.99, image_url='https://images.unsplash.com/photo-1676296227411-1a46a0bdb4fd?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
                # Add more items as needed
            ]

            # Add items to the database
            db.session.add_all(items)
            db.session.commit()

# Call the function to clear tables and add sample data
clear_tables()
add_sample_data()

@app.route('/')
def index():
    # Fetch all jewelry items from the database
    jewelry_items = Jewelry.query.all()
    return render_template('index.html', jewelry_items=jewelry_items)

if __name__ == '__main__':
    app.run(debug=True)
