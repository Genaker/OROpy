from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerUserApi(Base):
    __tablename__ = 'oro_customer_user_api'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_user_api_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), nullable=False, index=True)
    api_key = Column(String(255), nullable=False, unique=True, comment='(DC2Type:crypted_string)')

    user = relationship('OroCustomerUser')


