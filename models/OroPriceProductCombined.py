from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceProductCombined(Base):
    __tablename__ = 'oro_price_product_combined'
    __table_args__ = (
        Index('oro_combined_price_idx', 'combined_price_list_id', 'product_id', 'currency', 'unit_code', 'quantity'),
        Index('oro_cmb_price_product_currency_idx', 'product_id', 'currency'),
        Index('oro_cmb_price_mrg_idx', 'combined_price_list_id', 'product_id', 'merge_allowed')
    )

    id = Column(UUID, primary_key=True)
    unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    origin_price_id = Column(UUID)
    product_sku = Column(String(255), nullable=False)
    quantity = Column(Float(53), nullable=False)
    value = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(3), nullable=False)
    merge_allowed = Column(Boolean, nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    combined_price_list = relationship('OroPriceListCombined')
    product = relationship('OroProduct')
    oro_product_unit = relationship('OroProductUnit')


