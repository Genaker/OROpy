from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListCusFb(Base):
    __tablename__ = 'oro_price_list_cus_fb'
    __table_args__ = (
        Index('oro_price_list_cus_fb_unq', 'customer_id', 'website_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_cus_fb_id_seq'::regclass)"))
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='CASCADE'), nullable=False, index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, index=True)
    fallback = Column(Integer, nullable=False)

    customer = relationship('OroCustomer')
    website = relationship('OroWebsite')


