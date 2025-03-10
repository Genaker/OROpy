from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionCoupon(Base):
    __tablename__ = 'oro_promotion_coupon'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_coupon_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    promotion_id = Column(ForeignKey('oro_promotion.id', ondelete='SET NULL'), index=True)
    enabled = Column(Boolean, nullable=False, server_default=text("false"))
    code = Column(String(255), nullable=False, unique=True)
    code_uppercase = Column(String(255), nullable=False, index=True)
    uses_per_coupon = Column(Integer, server_default=text("1"))
    uses_per_person = Column(Integer, server_default=text("1"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    valid_from = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    valid_until = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')
    promotion = relationship('OroPromotion')


t_oro_promotion_description = Table(
    'oro_promotion_description', metadata,
    Column('promotion_id', ForeignKey('oro_promotion.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_promotion_label = Table(
    'oro_promotion_label', metadata,
    Column('promotion_id', ForeignKey('oro_promotion.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


