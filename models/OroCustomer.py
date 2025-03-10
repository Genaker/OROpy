from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomer(Base):
    __tablename__ = 'oro_customer'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_id_seq'::regclass)"))
    parent_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    group_id = Column(ForeignKey('oro_customer_group.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    internal_rating_id = Column(ForeignKey('oro_enum_acc_internal_rating.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False, index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    payment_term_7c4f1e8e_id = Column(ForeignKey('oro_payment_term.id', ondelete='SET NULL'), index=True)
    taxcode_id = Column(ForeignKey('oro_tax_customer_tax_code.id', ondelete='SET NULL'), index=True)
    previous_account_id = Column(ForeignKey('orocrm_account.id', ondelete='SET NULL'), index=True)
    lifetime = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)')
    datachannel_id = Column(ForeignKey('orocrm_channel.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    datachannel = relationship('OrocrmChannel')
    group = relationship('OroCustomerGroup')
    internal_rating = relationship('OroEnumAccInternalRating')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser')
    parent = relationship('OroCustomer', remote_side=[id])
    payment_term_7c4f1e8e = relationship('OroPaymentTerm')
    previous_account = relationship('OrocrmAccount')
    taxcode = relationship('OroTaxCustomerTaxCode')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552a784fec5f9c970f')
    users = relationship('OroUser', secondary='oro_customer_sales_reps')


t_oro_digital_asset_title = Table(
    'oro_digital_asset_title', metadata,
    Column('digital_asset_id', ForeignKey('oro_digital_asset.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


