from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListToProduct(Base):
    __tablename__ = 'oro_price_list_to_product'
    __table_args__ = (
        Index('oro_price_list_to_product_uidx', 'product_id', 'price_list_id', unique=True),
    )

    id = Column(UUID, primary_key=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    is_manual = Column(Boolean, nullable=False)

    price_list = relationship('OroPriceList')
    product = relationship('OroProduct')


