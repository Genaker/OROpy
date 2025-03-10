from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerUserSdbarSt(Base):
    __tablename__ = 'oro_customer_user_sdbar_st'
    __table_args__ = (
        Index('oro_cus_sdbar_st_unq_idx', 'customer_user_id', 'position', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_user_sdbar_st_id_seq'::regclass)"))
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), nullable=False, index=True)
    position = Column(String(13), nullable=False)
    state = Column(String(17), nullable=False)

    customer_user = relationship('OroCustomerUser')


