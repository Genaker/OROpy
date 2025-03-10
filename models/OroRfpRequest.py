from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRfpRequest(Base):
    __tablename__ = 'oro_rfp_request'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_rfp_request_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='SET NULL'), index=True)
    customer_status_id = Column(ForeignKey('oro_enum_rfp_customer_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    internal_status_id = Column(ForeignKey('oro_enum_rfp_internal_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    cancellation_reason = Column(Text)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), server_default=text("NULL::character varying"))
    company = Column(String(255), nullable=False)
    role = Column(String(255), server_default=text("NULL::character varying"))
    note = Column(Text)
    po_number = Column(String(255), server_default=text("NULL::character varying"))
    ship_until = Column(Date)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    deleted_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    customer = relationship('OroCustomer')
    customer_status = relationship('OroEnumRfpCustomerStatu')
    customer_user = relationship('OroCustomerUser')
    internal_status = relationship('OroEnumRfpInternalStatu')
    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')
    website = relationship('OroWebsite')
    users = relationship('OroUser', secondary='oro_rfp_assigned_users')


