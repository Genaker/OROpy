from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceProduct(Base):
    __tablename__ = 'oro_price_product'
    __table_args__ = (
        Index('oro_pricing_price_list_uidx', 'product_id', 'price_list_id', 'quantity', 'unit_code', 'currency', unique=True),
        Index('oro_price_version_idx', 'price_list_id', 'version', 'product_id')
    )

    id = Column(UUID, primary_key=True)
    price_rule_id = Column(ForeignKey('oro_price_rule.id', ondelete='CASCADE'), index=True)
    unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    product_sku = Column(String(255), nullable=False)
    quantity = Column(Float(53), nullable=False)
    value = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(3), nullable=False)
    version = Column(Integer)
    serialized_data = Column(JSONB(astext_type=Text()))

    price_list = relationship('OroPriceList')
    price_rule = relationship('OroPriceRule')
    product = relationship('OroProduct')
    oro_product_unit = relationship('OroProductUnit')


