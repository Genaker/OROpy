from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTaxZipCode(Base):
    __tablename__ = 'oro_tax_zip_code'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tax_zip_code_id_seq'::regclass)"))
    tax_jurisdiction_id = Column(ForeignKey('oro_tax_jurisdiction.id'), nullable=False, index=True)
    zip_code = Column(String(255), server_default=text("NULL::character varying"))
    zip_range_start = Column(String(255), server_default=text("NULL::character varying"))
    zip_range_end = Column(String(255), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    tax_jurisdiction = relationship('OroTaxJurisdiction')


