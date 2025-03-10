from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductImageType(Base):
    __tablename__ = 'oro_product_image_type'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_image_type_id_seq'::regclass)"))
    product_image_id = Column(ForeignKey('oro_product_image.id', ondelete='CASCADE'), nullable=False, index=True)
    type = Column(String(255), nullable=False, index=True)

    product_image = relationship('OroProductImage')


