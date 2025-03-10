from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerAdrAdrType(Base):
    __tablename__ = 'oro_customer_adr_adr_type'
    __table_args__ = (
        Index('oro_customer_adr_id_type_name_idx', 'customer_address_id', 'type_name', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_adr_adr_type_id_seq'::regclass)"))
    type_name = Column(ForeignKey('oro_address_type.name', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    customer_address_id = Column(ForeignKey('oro_customer_address.id', ondelete='CASCADE'), index=True)
    is_default = Column(Boolean)

    customer_address = relationship('OroCustomerAddres')
    oro_address_type = relationship('OroAddressType')


t_oro_email_mailbox_roles = Table(
    'oro_email_mailbox_roles', metadata,
    Column('mailbox_id', ForeignKey('oro_email_mailbox.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('role_id', ForeignKey('oro_access_role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_email_mailbox_users = Table(
    'oro_email_mailbox_users', metadata,
    Column('mailbox_id', ForeignKey('oro_email_mailbox.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


