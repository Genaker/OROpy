from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerUserRole(Base):
    __tablename__ = 'oro_customer_user_role'
    __table_args__ = (
        Index('uniq_552b533832c8a3de9395c3f3e', 'organization_id', 'customer_id', 'label', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_user_role_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    role = Column(String(255), nullable=False, unique=True)
    label = Column(String(255), nullable=False)
    self_managed = Column(Boolean, nullable=False, server_default=text("false"))
    public = Column(Boolean, nullable=False, server_default=text("true"))
    serialized_data = Column(JSONB(astext_type=Text()))

    customer = relationship('OroCustomer')
    organization = relationship('OroOrganization')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552ad7fa01cde46c56')


