from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusUsrAdrToAdrType(Base):
    __tablename__ = 'oro_cus_usr_adr_to_adr_type'
    __table_args__ = (
        Index('oro_customer_user_adr_id_type_name_idx', 'customer_user_address_id', 'type_name', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cus_usr_adr_to_adr_type_id_seq'::regclass)"))
    type_name = Column(ForeignKey('oro_address_type.name', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    customer_user_address_id = Column(ForeignKey('oro_customer_user_address.id', ondelete='CASCADE'), index=True)
    is_default = Column(Boolean)

    customer_user_address = relationship('OroCustomerUserAddres')
    oro_address_type = relationship('OroAddressType')


