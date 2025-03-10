from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDictionaryCountry(Base):
    __tablename__ = 'oro_dictionary_country'

    iso2_code = Column(String(2), primary_key=True)
    iso3_code = Column(String(3), nullable=False)
    name = Column(String(255), nullable=False, index=True)
    serialized_data = Column(JSONB(astext_type=Text()))


