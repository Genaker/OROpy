from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPlistCurrCombined(Base):
    __tablename__ = 'oro_plist_curr_combined'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_plist_curr_combined_id_seq'::regclass)"))
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    currency = Column(String(3), nullable=False)

    combined_price_list = relationship('OroPriceListCombined')


