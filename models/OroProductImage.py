from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductImage(Base):
    __tablename__ = 'oro_product_image'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_image_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    image_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    image = relationship('OroAttachmentFile')
    product = relationship('OroProduct')


