from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCategoryDefProdOpt(Base):
    __tablename__ = 'oro_category_def_prod_opts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_category_def_prod_opts_id_seq'::regclass)"))
    product_unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    product_unit_precision = Column(Integer)

    oro_product_unit = relationship('OroProductUnit')


