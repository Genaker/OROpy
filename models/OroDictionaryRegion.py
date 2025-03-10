from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDictionaryRegion(Base):
    __tablename__ = 'oro_dictionary_region'

    combined_code = Column(String(16), primary_key=True)
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), index=True, server_default=text("NULL::character varying"))
    code = Column(String(32), nullable=False)
    name = Column(String(255), nullable=False, index=True)

    oro_dictionary_country = relationship('OroDictionaryCountry')


