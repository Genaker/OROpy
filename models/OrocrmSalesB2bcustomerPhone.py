from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmSalesB2bcustomerPhone(Base):
    __tablename__ = 'orocrm_sales_b2bcustomer_phone'
    __table_args__ = (
        Index('primary_b2bcustomer_phone_idx', 'phone', 'is_primary'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_sales_b2bcustomer_phone_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='CASCADE'), index=True)
    phone = Column(String(255), nullable=False, index=True)
    is_primary = Column(Boolean)
    serialized_data = Column(JSONB(astext_type=Text()))

    owner = relationship('OrocrmSalesB2bcustomer')


