from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductKitItem(Base):
    __tablename__ = 'oro_product_kit_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_kit_item_id_seq'::regclass)"))
    unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    product_kit_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    optional = Column(Boolean, nullable=False, server_default=text("false"))
    sort_order = Column(Integer, nullable=False, server_default=text("0"))
    minimum_quantity = Column(Float(53))
    maximum_quantity = Column(Float(53))
    serialized_data = Column(JSONB(astext_type=Text()))

    product_kit = relationship('OroProduct')
    oro_product_unit = relationship('OroProductUnit')


