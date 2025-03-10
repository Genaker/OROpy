from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductAttrCurrency(Base):
    __tablename__ = 'oro_product_attr_currency'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_attr_currency_id_seq'::regclass)"))
    price_attribute_pl_id = Column(ForeignKey('oro_price_attribute_pl.id', ondelete='CASCADE'), nullable=False, index=True)
    currency = Column(String(3), nullable=False)

    price_attribute_pl = relationship('OroPriceAttributePl')


