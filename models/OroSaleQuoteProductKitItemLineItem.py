from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSaleQuoteProductKitItemLineItem(Base):
    __tablename__ = 'oro_sale_quote_product_kit_item_line_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_sale_quote_product_kit_item_line_item_id_seq'::regclass)"))
    quote_product_id = Column(ForeignKey('oro_sale_quote_product.id', ondelete='CASCADE'), nullable=False, index=True)
    product_kit_item_id = Column(ForeignKey('oro_product_kit_item.id', ondelete='SET NULL'), index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    product_kit_item_id_fallback = Column(Integer, nullable=False)
    product_kit_item_label = Column(String(255), nullable=False)
    optional = Column(Boolean, nullable=False, server_default=text("false"))
    product_id_fallback = Column(Integer, nullable=False)
    product_sku = Column(String(255), nullable=False)
    product_name = Column(String(255), nullable=False)
    product_unit_code = Column(String(255), nullable=False)
    product_unit_precision = Column(Integer, nullable=False)
    quantity = Column(Float(53), nullable=False)
    minimum_quantity = Column(Float(53))
    maximum_quantity = Column(Float(53))
    sort_order = Column(Integer, nullable=False, server_default=text("0"))
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(255), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    product = relationship('OroProduct')
    product_kit_item = relationship('OroProductKitItem')
    product_unit = relationship('OroProductUnit')
    quote_product = relationship('OroSaleQuoteProduct')


