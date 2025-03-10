from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListToCustomer(Base):
    __tablename__ = 'oro_price_list_to_customer'
    __table_args__ = (
        Index('uniq_7b51afcd9395c3f35688ded71', 'customer_id', 'price_list_id', 'website_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_to_customer_id_seq'::regclass)"))
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(Integer, nullable=False)
    merge_allowed = Column(Boolean, nullable=False, server_default=text("true"))

    customer = relationship('OroCustomer')
    price_list = relationship('OroPriceList')
    website = relationship('OroWebsite')


