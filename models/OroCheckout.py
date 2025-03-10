from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCheckout(Base):
    __tablename__ = 'oro_checkout'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_checkout_id_seq'::regclass)"))
    source_id = Column(ForeignKey('oro_checkout_source.id'), nullable=False, unique=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    registered_customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), unique=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    billing_address_id = Column(ForeignKey('oro_order_address.id', ondelete='SET NULL'), unique=True)
    shipping_address_id = Column(ForeignKey('oro_order_address.id', ondelete='SET NULL'), unique=True)
    uuid = Column(UUID, nullable=False, unique=True)
    po_number = Column(String(255), server_default=text("NULL::character varying"))
    customer_notes = Column(Text)
    currency = Column(String(3), server_default=text("NULL::character varying"))
    ship_until = Column(Date, comment='(DC2Type:date)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    shipping_estimate_amount = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    shipping_estimate_currency = Column(String(3), server_default=text("NULL::character varying"))
    payment_method = Column(String(255), server_default=text("NULL::character varying"))
    save_billing_address = Column(Boolean, nullable=False, server_default=text("true"))
    ship_to_billing_address = Column(Boolean, nullable=False, server_default=text("false"))
    save_shipping_address = Column(Boolean, nullable=False, server_default=text("true"))
    shipping_method = Column(String(255), server_default=text("NULL::character varying"))
    shipping_method_type = Column(String(255), server_default=text("NULL::character varying"))
    deleted = Column(Boolean, nullable=False, server_default=text("false"))
    completed = Column(Boolean, nullable=False, server_default=text("false"))
    completed_data = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    line_item_group_shipping_data = Column(JSON, comment='(DC2Type:json)')
    serialized_data = Column(JSONB(astext_type=Text()))

    billing_address = relationship('OroOrderAddres', primaryjoin='OroCheckout.billing_address_id == OroOrderAddres.id')
    customer = relationship('OroCustomer')
    customer_user = relationship('OroCustomerUser', primaryjoin='OroCheckout.customer_user_id == OroCustomerUser.id')
    organization = relationship('OroOrganization')
    registered_customer_user = relationship('OroCustomerUser', primaryjoin='OroCheckout.registered_customer_user_id == OroCustomerUser.id')
    shipping_address = relationship('OroOrderAddres', primaryjoin='OroCheckout.shipping_address_id == OroOrderAddres.id')
    source = relationship('OroCheckoutSource')
    user_owner = relationship('OroUser')
    website = relationship('OroWebsite')


