# OROpy: Python SQLAlchemy Database-First ORM for OroCommerce

OROpy is a Python library that provides an SQLAlchemy ORM interface for interacting with an OroCommerce database. It allows you to perform operations such as querying and manipulating data within your OroCommerce instance using Python.

![OROpy](https://github.com/user-attachments/assets/5963177d-79ad-4b1f-813f-8acd04f5644c)

## Features

- Define ORM models for OroCommerce entities.
- Perform CRUD operations on OroCommerce data.
- Integrate with OroCommerce's database using SQLAlchemy.

## Requirements

- Python 3.6+
- SQLAlchemy
- Tabulate (for displaying query results in a table format)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/oropy.git
   cd oropy
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that your `requirements.txt` includes:
   ```
   sqlalchemy
   tabulate
   ```

## Usage

### Setup

1. **Configure Database Access**: Set up your database connection in `db.py`.

   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.orm import sessionmaker

   DATABASE_URL = 'postgresql://username:password@localhost:5432/orocommerce'

   engine = create_engine(DATABASE_URL)
   Session = sessionmaker(bind=engine)
   session = Session()
   ```

2. **Import ORM Models**: Use OROpy to import models for your OroCommerce entities.

   ```python
   from models.OroProduct import OroProduct
   configure_mappers()
   ```

### Querying Data

To query data from the OroCommerce database:

```python
from db import session
from models.OroProduct import OroProduct
configure_mappers()
products = session.query(OroProduct).all()
for product in products:
print(f"ID: {product.id}, Name: {product.name}, SKU: {product.sku}")
```

## Using AI with OROpy

Integrating AI with OROpy can enhance your data analysis capabilities:

- **Predictive Analytics**: Use machine learning models to predict sales trends and customer behavior.
- **Automated Insights**: Generate insights from your data using AI algorithms.

### Potential Uses of Python Modules in OroCommerce

- **Data Integration and ETL**: Automate data workflows between OroCommerce and other systems.
- **Custom Scripts and Automation**: Automate tasks such as data imports and exports.
- **API Interactions**: Manage OroCommerce data programmatically.
- **Machine Learning and Analytics**: Analyze and visualize data to support business decisions.

## Example of a Flask API for OroCommerce
```python
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
# Import the OroProduct model from your OROpy module
from models import OroProduct  


# Database configuration
DATABASE_URL = 'postgresql://username:password@localhost:5432/orocommerce'

# Set up the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = scoped_session(sessionmaker(bind=engine))

# Create a base class for declarative class definitions
Base = declarative_base()

# Create the Flask application
app = Flask(__name__)

# API endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    session = Session()
    products = session.query(OroProduct).all()
    session.close()
    return jsonify([{'id': p.id, 'name': p.name, 'sku': p.sku} for p in products])

# API endpoint to get a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    session = Session()
    product = session.query(OroProduct).get(product_id)
    session.close()
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'sku': product.sku})
    return jsonify({'error': 'Product not found'}), 404

# API endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    session = Session()
    data = request.json
    new_product = OroProduct(name=data['name'], sku=data['sku'])
    session.add(new_product)
    session.commit()
    session.close()
    return jsonify({'id': new_product.id, 'name': new_product.name, 'sku': new_product.sku}), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
