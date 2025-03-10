from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEnumRfpCustomerStatu(Base):
    __tablename__ = 'oro_enum_rfp_customer_status'

    id = Column(String(32), primary_key=True)
    name = Column(String(255), nullable=False)
    priority = Column(Integer, nullable=False)
    is_default = Column(Boolean, nullable=False)


