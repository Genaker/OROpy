from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductUnitPrecision(Base):
    __tablename__ = 'oro_product_unit_precision'
    __table_args__ = (
        Index('uidx_oro_product_unit_precision', 'product_id', 'unit_code', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_unit_precision_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    unit_precision = Column(Integer, nullable=False)
    conversion_rate = Column(Float(53))
    sell = Column(Boolean, nullable=False)

    product = relationship('OroProduct', primaryjoin='OroProductUnitPrecision.product_id == OroProduct.id')
    oro_product_unit = relationship('OroProductUnit')


