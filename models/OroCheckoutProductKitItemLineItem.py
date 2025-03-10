from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCheckoutProductKitItemLineItem(Base):
    __tablename__ = 'oro_checkout_product_kit_item_line_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_checkout_product_kit_item_line_item_id_seq'::regclass)"))
    line_item_id = Column(ForeignKey('oro_checkout_line_item.id', ondelete='CASCADE'), nullable=False, index=True)
    product_kit_item_id = Column(ForeignKey('oro_product_kit_item.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), nullable=False, index=True)
    quantity = Column(Float(53), nullable=False)
    sort_order = Column(Integer, nullable=False, server_default=text("0"))
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(255), server_default=text("NULL::character varying"))
    is_price_fixed = Column(Boolean, nullable=False, server_default=text("false"))

    line_item = relationship('OroCheckoutLineItem')
    product = relationship('OroProduct')
    product_kit_item = relationship('OroProductKitItem')
    product_unit = relationship('OroProductUnit')
