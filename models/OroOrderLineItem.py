from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOrderLineItem(Base):
    __tablename__ = 'oro_order_line_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_order_line_item_id_seq'::regclass)"))
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    parent_product_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    order_id = Column(ForeignKey('oro_order.id', ondelete='CASCADE'), index=True)
    product_sku = Column(String(255), server_default=text("NULL::character varying"))
    product_name = Column(String(255), server_default=text("NULL::character varying"))
    product_variant_fields = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    free_form_product = Column(String(255), server_default=text("NULL::character varying"))
    quantity = Column(Float(53))
    product_unit_code = Column(String(255), server_default=text("NULL::character varying"))
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(255), server_default=text("NULL::character varying"))
    price_type = Column(Integer, nullable=False)
    ship_by = Column(Date, comment='(DC2Type:date)')
    from_external_source = Column(Boolean, nullable=False)
    comment = Column(Text)
    shipping_method = Column(String(255), server_default=text("NULL::character varying"))
    shipping_method_type = Column(String(255), server_default=text("NULL::character varying"))
    shipping_estimate_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    checksum = Column(String(40), nullable=False, server_default=text("''::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    order = relationship('OroOrder')
    parent_product = relationship('OroProduct', primaryjoin='OroOrderLineItem.parent_product_id == OroProduct.id')
    product = relationship('OroProduct', primaryjoin='OroOrderLineItem.product_id == OroProduct.id')
    product_unit = relationship('OroProductUnit')


