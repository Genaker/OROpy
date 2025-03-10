from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URL
DATABASE_URL = 'postgresql://postgres:postgres@127.0.0.1:5432/oro'

# Create an engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()