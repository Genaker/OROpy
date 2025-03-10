from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmbPlToPl(Base):
    __tablename__ = 'oro_cmb_pl_to_pl'
    __table_args__ = (
        Index('cmb_pl_to_pl_cmb_prod_sort_idx', 'combined_price_list_id', 'sort_order'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cmb_pl_to_pl_id_seq'::regclass)"))
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(Integer, nullable=False)
    merge_allowed = Column(Boolean, nullable=False)

    combined_price_list = relationship('OroPriceListCombined')
    price_list = relationship('OroPriceList')


