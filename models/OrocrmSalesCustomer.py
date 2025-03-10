from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmSalesCustomer(Base):
    __tablename__ = 'orocrm_sales_customer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_sales_customer_id_seq'::regclass)"))
    account_id = Column(ForeignKey('orocrm_account.id', ondelete='CASCADE'), nullable=False, index=True)
    b2b_customer_188b774c_id = Column(ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='SET NULL'), index=True)
    customer_e197f906_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)

    account = relationship('OrocrmAccount')
    b2b_customer_188b774c = relationship('OrocrmSalesB2bcustomer')
    customer_e197f906 = relationship('OroCustomer')


