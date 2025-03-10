from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListCurrency(Base):
    __tablename__ = 'oro_price_list_currency'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_currency_id_seq'::regclass)"))
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    currency = Column(String(3), nullable=False)

    price_list = relationship('OroPriceList')


