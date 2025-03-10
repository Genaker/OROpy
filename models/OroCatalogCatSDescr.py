from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCatalogCatSDescr(Base):
    __tablename__ = 'oro_catalog_cat_s_descr'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_catalog_cat_s_descr_id_seq'::regclass)"))
    category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), index=True)
    fallback = Column(String(64), index=True, server_default=text("NULL::character varying"))
    text = Column(Text)

    category = relationship('OroCatalogCategory')
    localization = relationship('OroLocalization')


