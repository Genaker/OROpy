from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTaxJurisdiction(Base):
    __tablename__ = 'oro_tax_jurisdiction'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tax_jurisdiction_id_seq'::regclass)"))
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), index=True, server_default=text("NULL::character varying"))
    region_code = Column(ForeignKey('oro_dictionary_region.combined_code'), index=True, server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    code = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    region_text = Column(String(255), server_default=text("NULL::character varying"))

    oro_dictionary_country = relationship('OroDictionaryCountry')
    oro_dictionary_region = relationship('OroDictionaryRegion')


t_oro_tax_prod_tax_code_prod = Table(
    'oro_tax_prod_tax_code_prod', metadata,
    Column('product_tax_code_id', ForeignKey('oro_tax_product_tax_code.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


