from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusPagestate(Base):
    __tablename__ = 'oro_cus_pagestate'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cus_pagestate_id_seq'::regclass)"))
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), nullable=False, index=True)
    page_id = Column(String(10920), nullable=False)
    page_hash = Column(String(32), nullable=False, unique=True)
    data = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    customer_user = relationship('OroCustomerUser')


