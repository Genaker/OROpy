from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotion(Base):
    __tablename__ = 'oro_promotion'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    discount_config_id = Column(ForeignKey('oro_promotion_discount_config.id', ondelete='CASCADE'), nullable=False, unique=True)
    rule_id = Column(ForeignKey('oro_rule.id', ondelete='CASCADE'), nullable=False, index=True)
    products_segment_id = Column(ForeignKey('oro_segment.id', ondelete='CASCADE'), nullable=False, index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    use_coupons = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    discount_config = relationship('OroPromotionDiscountConfig')
    organization = relationship('OroOrganization')
    products_segment = relationship('OroSegment')
    rule = relationship('OroRule')
    user_owner = relationship('OroUser')
    scopes = relationship('OroScope', secondary='oro_promotion_scope')


