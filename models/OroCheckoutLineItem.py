from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCheckoutLineItem(Base):
    __tablename__ = 'oro_checkout_line_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_checkout_line_item_id_seq'::regclass)"))
    checkout_id = Column(ForeignKey('oro_checkout.id', ondelete='CASCADE'), index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    parent_product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    product_sku = Column(String(255), server_default=text("NULL::character varying"))
    free_form_product = Column(String(255), server_default=text("NULL::character varying"))
    quantity = Column(Float(53))
    product_unit_code = Column(String(255), server_default=text("NULL::character varying"))
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(255), server_default=text("NULL::character varying"))
    price_type = Column(Integer, nullable=False)
    from_external_source = Column(Boolean, nullable=False)
    comment = Column(Text)
    is_price_fixed = Column(Boolean, nullable=False)
    shipping_method = Column(String(255), server_default=text("NULL::character varying"))
    shipping_method_type = Column(String(255), server_default=text("NULL::character varying"))
    shipping_estimate_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    checksum = Column(String(40), nullable=False, server_default=text("''::character varying"))

    checkout = relationship('OroCheckout')
    parent_product = relationship('OroProduct', primaryjoin='OroCheckoutLineItem.parent_product_id == OroProduct.id')
    product = relationship('OroProduct', primaryjoin='OroCheckoutLineItem.product_id == OroProduct.id')
    product_unit = relationship('OroProductUnit')


