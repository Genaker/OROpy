from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, configure_mappers
from tabulate import tabulate
from models.OroProduct import OroProduct
configure_mappers()

from db import session

# Define the base class
#Base = declarative_base()

# Query to get all slides
products = session.query(OroProduct).all()

# Prepare data for tabulate
headers = ["ID", "SKU", "Name"]
data = [[product.id, product.sku, product.name] for product in products]

# Print the table
print(tabulate(data, headers=headers, tablefmt="grid"))

# Close the session
session.close()