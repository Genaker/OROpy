from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceAttributePrice(Base):
    __tablename__ = 'oro_price_attribute_price'
    __table_args__ = (
        Index('oro_pricing_price_attribute_uidx', 'product_id', 'price_attribute_pl_id', 'quantity', 'unit_code', 'currency', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_attribute_price_id_seq'::regclass)"))
    price_attribute_pl_id = Column(ForeignKey('oro_price_attribute_pl.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), nullable=False, index=True)
    product_sku = Column(String(255), nullable=False)
    quantity = Column(Float(53), nullable=False)
    value = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money)')
    currency = Column(String(3), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    price_attribute_pl = relationship('OroPriceAttributePl')
    product = relationship('OroProduct')
    oro_product_unit = relationship('OroProductUnit')


