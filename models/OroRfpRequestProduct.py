from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRfpRequestProduct(Base):
    __tablename__ = 'oro_rfp_request_product'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_rfp_request_product_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    request_id = Column(ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), index=True)
    product_sku = Column(String(255), nullable=False)
    comment = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    product = relationship('OroProduct')
    request = relationship('OroRfpRequest')


