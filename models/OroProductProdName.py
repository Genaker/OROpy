from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductProdName(Base):
    __tablename__ = 'oro_product_prod_name'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_prod_name_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), index=True)
    fallback = Column(String(64), index=True, server_default=text("NULL::character varying"))
    string = Column(String(255), index=True, server_default=text("NULL::character varying"))

    localization = relationship('OroLocalization')
    product = relationship('OroProduct')


