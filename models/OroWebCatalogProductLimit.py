from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebCatalogProductLimit(Base):
    __tablename__ = 'oro_web_catalog_product_limit'

    id = Column(UUID, primary_key=True)
    product_id = Column(Integer, nullable=False)
    version = Column(Integer, nullable=False)


