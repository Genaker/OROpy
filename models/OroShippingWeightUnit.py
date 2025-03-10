from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShippingWeightUnit(Base):
    __tablename__ = 'oro_shipping_weight_unit'

    code = Column(String(255), primary_key=True)
    conversion_rates = Column(Text, comment='(DC2Type:array)(DC2Type:array)')


