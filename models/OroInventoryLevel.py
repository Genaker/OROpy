from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroInventoryLevel(Base):
    __tablename__ = 'oro_inventory_level'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_inventory_level_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    product_unit_precision_id = Column(ForeignKey('oro_product_unit_precision.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    quantity = Column(Numeric(20, 10), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    product = relationship('OroProduct')
    product_unit_precision = relationship('OroProductUnitPrecision')


