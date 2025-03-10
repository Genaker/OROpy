from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOrder(Base):
    __tablename__ = 'oro_order'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_order_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    created_by_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    shipping_address_id = Column(ForeignKey('oro_order_address.id', ondelete='SET NULL'), unique=True)
    billing_address_id = Column(ForeignKey('oro_order_address.id', ondelete='SET NULL'), unique=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='SET NULL'), index=True)
    parent_id = Column(ForeignKey('oro_order.id', ondelete='CASCADE'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    internal_status_id = Column(ForeignKey('oro_enum_order_internal_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    status_id = Column(ForeignKey('oro_enum_order_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    payment_term_7c4f1e8e_id = Column(ForeignKey('oro_payment_term.id', ondelete='SET NULL'), index=True)
    uuid = Column(UUID, nullable=False, unique=True)
    identifier = Column(String(255), unique=True, server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    po_number = Column(String(255), server_default=text("NULL::character varying"))
    customer_notes = Column(Text)
    ship_until = Column(Date)
    currency = Column(String(3), server_default=text("NULL::character varying"))
    shipping_method = Column(String(255), server_default=text("NULL::character varying"))
    shipping_method_type = Column(String(255), server_default=text("NULL::character varying"))
    subtotal_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money_value)(DC2Type:money_value)')
    subtotal_currency = Column(String(3), server_default=text("NULL::character varying"), comment='(DC2Type:currency)(DC2Type:currency)')
    base_subtotal_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    subtotal_with_discounts = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    total_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money_value)(DC2Type:money_value)')
    total_currency = Column(String(3), server_default=text("NULL::character varying"), comment='(DC2Type:currency)(DC2Type:currency)')
    base_total_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    estimated_shipping_cost_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    override_shipping_cost_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    total_discounts_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    source_entity_class = Column(String(255), server_default=text("NULL::character varying"))
    source_entity_id = Column(Integer)
    source_entity_identifier = Column(String(255), server_default=text("NULL::character varying"))
    disablepromotions = Column(Boolean, index=True)
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    billing_address = relationship('OroOrderAddres', primaryjoin='OroOrder.billing_address_id == OroOrderAddres.id')
    created_by_user = relationship('OroUser', primaryjoin='OroOrder.created_by_user_id == OroUser.id')
    customer = relationship('OroCustomer')
    customer_user = relationship('OroCustomerUser')
    internal_status = relationship('OroEnumOrderInternalStatu')
    organization = relationship('OroOrganization')
    parent = relationship('OroOrder', remote_side=[id])
    payment_term_7c4f1e8e = relationship('OroPaymentTerm')
    shipping_address = relationship('OroOrderAddres', primaryjoin='OroOrder.shipping_address_id == OroOrderAddres.id')
    status = relationship('OroEnumOrderStatu')
    user_owner = relationship('OroUser', primaryjoin='OroOrder.user_owner_id == OroUser.id')
    website = relationship('OroWebsite')


