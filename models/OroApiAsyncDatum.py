from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroApiAsyncDatum(Base):
    __tablename__ = 'oro_api_async_data'

    name = Column(String(255), primary_key=True)
    content = Column(Text, nullable=False)
    updated_at = Column(Integer, nullable=False)
    checksum = Column(String(32), nullable=False)


