from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSaleQuote(Base):
    __tablename__ = 'oro_sale_quote'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_sale_quote_id_seq'::regclass)"))
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    request_id = Column(ForeignKey('oro_rfp_request.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    shipping_address_id = Column(ForeignKey('oro_quote_address.id', ondelete='SET NULL'), unique=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='SET NULL'), index=True)
    customer_status_id = Column(ForeignKey('oro_enum_quote_customer_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    internal_status_id = Column(ForeignKey('oro_enum_quote_internal_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    payment_term_7c4f1e8e_id = Column(ForeignKey('oro_payment_term.id', ondelete='SET NULL'), index=True)
    guest_access_id = Column(UUID)
    qid = Column(String(255), server_default=text("NULL::character varying"))
    po_number = Column(String(255), server_default=text("NULL::character varying"))
    ship_until = Column(Date)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    valid_until = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    expired = Column(Boolean, nullable=False, server_default=text("false"))
    prices_changed = Column(Boolean, nullable=False, server_default=text("false"))
    shipping_method = Column(String(255), server_default=text("NULL::character varying"))
    shipping_method_type = Column(String(255), server_default=text("NULL::character varying"))
    estimated_shipping_cost_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    override_shipping_cost_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(3), server_default=text("NULL::character varying"))
    shipping_method_locked = Column(Boolean, nullable=False, server_default=text("false"))
    allow_unlisted_shipping_method = Column(Boolean, nullable=False, server_default=text("false"))
    opportunity_id = Column(ForeignKey('orocrm_sales_opportunity.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    customer = relationship('OroCustomer')
    customer_status = relationship('OroEnumQuoteCustomerStatu')
    customer_user = relationship('OroCustomerUser')
    internal_status = relationship('OroEnumQuoteInternalStatu')
    opportunity = relationship('OrocrmSalesOpportunity')
    organization = relationship('OroOrganization')
    payment_term_7c4f1e8e = relationship('OroPaymentTerm')
    request = relationship('OroRfpRequest')
    shipping_address = relationship('OroQuoteAddres')
    user_owner = relationship('OroUser')
    website = relationship('OroWebsite')
    users = relationship('OroUser', secondary='oro_quote_assigned_users')


