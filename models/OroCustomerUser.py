from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerUser(Base):
    __tablename__ = 'oro_customer_user'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_user_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='SET NULL'), index=True)
    auth_status_id = Column(ForeignKey('oro_enum_cu_auth_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    email_lowercase = Column(String(255), nullable=False, index=True)
    name_prefix = Column(String(255), server_default=text("NULL::character varying"))
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    middle_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    name_suffix = Column(String(255), server_default=text("NULL::character varying"))
    birthday = Column(Date)
    enabled = Column(Boolean, nullable=False)
    confirmed = Column(Boolean, nullable=False)
    is_guest = Column(Boolean, nullable=False, server_default=text("false"))
    salt = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    confirmation_token = Column(String(255), server_default=text("NULL::character varying"))
    password_requested = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    password_changed = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    last_login = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    last_duplicate_notification_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    login_count = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    cookies_accepted = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    auth_status = relationship('OroEnumCuAuthStatu')
    customer = relationship('OroCustomer')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser')
    website = relationship('OroWebsite')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552a3708e583c5ba51')
    emails = relationship('OroEmail', secondary='oro_rel_265353703708e583c5ba51')
    customer_user_roles = relationship('OroCustomerUserRole', secondary='oro_cus_user_access_role')
    users = relationship('OroUser', secondary='oro_customer_user_sales_reps')
    requests = relationship('OroRfpRequest', secondary='oro_rfp_assigned_cus_users')
    quotes = relationship('OroSaleQuote', secondary='oro_quote_assigned_cus_users')


