from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmbPriceListToW(Base):
    __tablename__ = 'oro_cmb_price_list_to_ws'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cmb_price_list_to_ws_id_seq'::regclass)"))
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, unique=True)
    full_combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    version = Column(Integer)

    combined_price_list = relationship('OroPriceListCombined', primaryjoin='OroCmbPriceListToW.combined_price_list_id == OroPriceListCombined.id')
    full_combined_price_list = relationship('OroPriceListCombined', primaryjoin='OroCmbPriceListToW.full_combined_price_list_id == OroPriceListCombined.id')
    website = relationship('OroWebsite')


