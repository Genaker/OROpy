from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTaxRule(Base):
    __tablename__ = 'oro_tax_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tax_rule_id_seq'::regclass)"))
    tax_jurisdiction_id = Column(ForeignKey('oro_tax_jurisdiction.id', ondelete='CASCADE'), index=True)
    customer_tax_code_id = Column(ForeignKey('oro_tax_customer_tax_code.id', ondelete='CASCADE'), index=True)
    product_tax_code_id = Column(ForeignKey('oro_tax_product_tax_code.id', ondelete='CASCADE'), index=True)
    tax_id = Column(ForeignKey('oro_tax.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    description = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    customer_tax_code = relationship('OroTaxCustomerTaxCode')
    organization = relationship('OroOrganization')
    product_tax_code = relationship('OroTaxProductTaxCode')
    tax = relationship('OroTax')
    tax_jurisdiction = relationship('OroTaxJurisdiction')


