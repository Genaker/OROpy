from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmbPlistToCusGr(Base):
    __tablename__ = 'oro_cmb_plist_to_cus_gr'
    __table_args__ = (
        Index('oro_cpl_to_cus_gr_ws_unq', 'customer_group_id', 'website_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cmb_plist_to_cus_gr_id_seq'::regclass)"))
    customer_group_id = Column(ForeignKey('oro_customer_group.id', ondelete='CASCADE'), nullable=False, index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, index=True)
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    full_combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    version = Column(Integer)

    combined_price_list = relationship('OroPriceListCombined', primaryjoin='OroCmbPlistToCusGr.combined_price_list_id == OroPriceListCombined.id')
    customer_group = relationship('OroCustomerGroup')
    full_combined_price_list = relationship('OroPriceListCombined', primaryjoin='OroCmbPlistToCusGr.full_combined_price_list_id == OroPriceListCombined.id')
    website = relationship('OroWebsite')


