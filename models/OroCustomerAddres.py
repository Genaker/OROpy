from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerAddres(Base):
    __tablename__ = 'oro_customer_address'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_address_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    system_org_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    frontend_owner_id = Column(ForeignKey('oro_customer.id', ondelete='CASCADE'), index=True)
    region_code = Column(ForeignKey('oro_dictionary_region.combined_code'), index=True, server_default=text("NULL::character varying"))
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), index=True, server_default=text("NULL::character varying"))
    is_primary = Column(Boolean)
    label = Column(String(255), server_default=text("NULL::character varying"))
    street = Column(String(500), server_default=text("NULL::character varying"))
    street2 = Column(String(500), server_default=text("NULL::character varying"))
    city = Column(String(255), server_default=text("NULL::character varying"))
    postal_code = Column(String(255), server_default=text("NULL::character varying"))
    organization = Column(String(255), server_default=text("NULL::character varying"))
    region_text = Column(String(255), server_default=text("NULL::character varying"))
    name_prefix = Column(String(255), server_default=text("NULL::character varying"))
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    middle_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    name_suffix = Column(String(255), server_default=text("NULL::character varying"))
    phone = Column(String(255), server_default=text("NULL::character varying"))
    created = Column(TIMESTAMP(precision=0), nullable=False)
    updated = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    oro_dictionary_country = relationship('OroDictionaryCountry')
    frontend_owner = relationship('OroCustomer')
    owner = relationship('OroUser')
    oro_dictionary_region = relationship('OroDictionaryRegion')
    system_org = relationship('OroOrganization')


t_oro_customer_sales_reps = Table(
    'oro_customer_sales_reps', metadata,
    Column('customer_id', ForeignKey('oro_customer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


