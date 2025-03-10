from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductRelatedProduct(Base):
    __tablename__ = 'oro_product_related_products'
    __table_args__ = (
        Index('idx_oro_product_related_products_unique', 'product_id', 'related_item_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_related_products_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    related_item_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)

    product = relationship('OroProduct', primaryjoin='OroProductRelatedProduct.product_id == OroProduct.id')
    related_item = relationship('OroProduct', primaryjoin='OroProductRelatedProduct.related_item_id == OroProduct.id')


