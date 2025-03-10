from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerGroup(Base):
    __tablename__ = 'oro_customer_group'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_group_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False, index=True)
    payment_term_7c4f1e8e_id = Column(ForeignKey('oro_payment_term.id', ondelete='SET NULL'), index=True)
    taxcode_id = Column(ForeignKey('oro_tax_customer_tax_code.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    payment_term_7c4f1e8e = relationship('OroPaymentTerm')
    taxcode = relationship('OroTaxCustomerTaxCode')
    user_owner = relationship('OroUser')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552a16cbf45882508f')


