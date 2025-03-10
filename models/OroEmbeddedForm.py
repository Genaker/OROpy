from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmbeddedForm(Base):
    __tablename__ = 'oro_embedded_form'

    id = Column(String(255), primary_key=True)
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    title = Column(Text, nullable=False)
    css = Column(Text, nullable=False)
    form_type = Column(String(255), nullable=False)
    success_message = Column(Text, nullable=False)
    allowed_domains = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    datachannel_id = Column(ForeignKey('orocrm_channel.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    datachannel = relationship('OrocrmChannel')
    owner = relationship('OroOrganization')


t_oro_fedex_transport_label = Table(
    'oro_fedex_transport_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_fixed_product_transp_label = Table(
    'oro_fixed_product_transp_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_flat_rate_transport_label = Table(
    'oro_flat_rate_transport_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_localization_title = Table(
    'oro_localization_title', metadata,
    Column('localization_id', ForeignKey('oro_localization.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_money_order_short_label = Table(
    'oro_money_order_short_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_money_order_trans_label = Table(
    'oro_money_order_trans_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_payment_term_short_label = Table(
    'oro_payment_term_short_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_payment_term_trans_label = Table(
    'oro_payment_term_trans_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_paypal_credit_card_lbl = Table(
    'oro_paypal_credit_card_lbl', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_paypal_credit_card_sh_lbl = Table(
    'oro_paypal_credit_card_sh_lbl', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_paypal_xprss_chkt_lbl = Table(
    'oro_paypal_xprss_chkt_lbl', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_paypal_xprss_chkt_shrt_lbl = Table(
    'oro_paypal_xprss_chkt_shrt_lbl', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_product_slug = Table(
    'oro_product_slug', metadata,
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('slug_id', ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_product_slug_prototype = Table(
    'oro_product_slug_prototype', metadata,
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


