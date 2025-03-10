from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentTransaction(Base):
    __tablename__ = 'oro_payment_transaction'
    __table_args__ = (
        Index('oro_pay_trans_access_uidx', 'access_identifier', 'access_token', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_transaction_id_seq'::regclass)"))
    source_payment_transaction = Column(ForeignKey('oro_payment_transaction.id', ondelete='CASCADE'), index=True)
    frontend_owner_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    entity_class = Column(String(255), nullable=False)
    entity_identifier = Column(Integer, nullable=False)
    access_identifier = Column(String(255), nullable=False)
    access_token = Column(String(255), nullable=False)
    payment_method = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    reference = Column(String(255), server_default=text("NULL::character varying"))
    amount = Column(String(255), nullable=False)
    currency = Column(String(3), nullable=False)
    active = Column(Boolean, nullable=False)
    successful = Column(Boolean, nullable=False)
    request = Column(Text, comment='(DC2Type:secure_array)(DC2Type:secure_array)')
    response = Column(Text, comment='(DC2Type:secure_array)(DC2Type:secure_array)')
    transaction_options = Column(Text, comment='(DC2Type:secure_array)(DC2Type:secure_array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    frontend_owner = relationship('OroCustomerUser')
    organization = relationship('OroOrganization')
    parent = relationship('OroPaymentTransaction', remote_side=[id])
    user_owner = relationship('OroUser')


