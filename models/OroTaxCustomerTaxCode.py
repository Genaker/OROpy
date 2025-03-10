from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTaxCustomerTaxCode(Base):
    __tablename__ = 'oro_tax_customer_tax_code'
    __table_args__ = (
        Index('oro_customer_tax_code_organization_unique_index', 'code', 'organization_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tax_customer_tax_code_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    code = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


