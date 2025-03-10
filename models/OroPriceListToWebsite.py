from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListToWebsite(Base):
    __tablename__ = 'oro_price_list_to_website'
    __table_args__ = (
        Index('uniq_2073faf95688ded718f45c82', 'price_list_id', 'website_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_to_website_id_seq'::regclass)"))
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(Integer, nullable=False)
    merge_allowed = Column(Boolean, nullable=False, server_default=text("true"))

    price_list = relationship('OroPriceList')
    website = relationship('OroWebsite')


